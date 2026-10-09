"""Vérificateur de cohérence des données électriques de Juju.

Usage (depuis la racine du dépôt ou n'importe où) :
    python Electricité/outils/verifier.py

Contrôles :
  1. syntaxe YAML, clés en double comprises (PyYAML les écrase sans prévenir) ;
  2. conformité aux schémas JSON de outils/schema/ ;
  3. identifiants uniques, références existantes (nœuds, équipements, questions) ;
  4. règles électriques : pas de fil entre un + et un -, couleur cohérente,
     section normalisée, pas deux fils en parallèle sur les mêmes nœuds ;
  5. chaque fil des données figure sur les schémas SVG, et inversement ;
     chaque équipement placé dans une zone figure sur le plan d'implantation ;
  6. hypothèses des études : application du delta sur leur base, puis mêmes contrôles ;
     installation cible (cible/cible.yaml) : hypothèses retenues appliquées dans l'ordre,
     et chaque fil 12 V du résultat présent sur le folio de cible/ ;
  7. en-tête YAML de chaque proposition.md (outils/schema/proposition.schema.json) ;
  8. bilan énergétique : Ah consommés par jour pour chaque profil.
Les questions traitées (section « Réponses » de questions.md) ne doivent plus
être citées par les données ni par les schémas.

Code de retour : 1 s'il y a au moins une erreur, 0 sinon (les avertissements ne bloquent pas).
"""
from __future__ import annotations

import copy
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft7Validator
except ImportError:
    sys.exit("Modules manquants : lancer « python -m pip install -r Electricité/outils/requirements.txt »")

RACINE = Path(__file__).resolve().parent.parent  # dossier Electricité/
RELEVE = RACINE / "releve"
FICHIERS_RELEVE = ["amenagement.yaml", "equipements.yaml", "netlist.yaml", "wirelist.yaml"]
CATEGORIES = ("zones", "equipements", "nodes", "fils")
POLARITES_12V = {"+", "-"}
POLARITES_230V = {"230V-phase", "230V-neutre", "230V-terre"}
SECTIONS_NORMALISEES = {0.75, 1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120}
COULEURS_230V = {"230V-phase": {"marron", "noir", "gris", "rouge"}, "230V-neutre": {"bleu"},
                 "230V-terre": {"vert-jaune"}}
IMPLANTATION = RACINE / "schemas" / "folio-0-implantation.svg"
CIBLE = RACINE / "cible"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# --------------------------------------------------------------------------- rapport
class Rapport:
    def __init__(self) -> None:
        self.erreurs = 0
        self.avertissements = 0

    def section(self, titre: str) -> None:
        print(f"\n== {titre} ==")

    def erreur(self, ou: str, msg: str) -> None:
        self.erreurs += 1
        print(f"  ERREUR     {ou} : {msg}")

    def avert(self, ou: str, msg: str) -> None:
        self.avertissements += 1
        print(f"  ATTENTION  {ou} : {msg}")

    def info(self, msg: str) -> None:
        print(f"  info       {msg}")

    def ok(self, msg: str) -> None:
        print(f"  ok         {msg}")


# --------------------------------------------------------------------------- lecture
class ChargeurStrict(yaml.SafeLoader):
    """SafeLoader qui refuse les clés en double."""


def _mapping_strict(loader, node, deep=False):
    vues = set()
    for cle_node, _ in node.value:
        cle = loader.construct_object(cle_node, deep=deep)
        if cle in vues:
            raise yaml.constructor.ConstructorError(
                None, None, f"clé en double « {cle} »", cle_node.start_mark)
        vues.add(cle)
    return loader.construct_mapping(node, deep=deep)


ChargeurStrict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping_strict)


def rel(chemin: Path) -> str:
    return chemin.relative_to(RACINE.parent).as_posix()


def lire_yaml(chemin: Path, r: Rapport) -> dict | None:
    try:
        with chemin.open(encoding="utf-8") as f:
            data = yaml.load(f, Loader=ChargeurStrict)
    except yaml.YAMLError as e:
        r.erreur(rel(chemin), f"YAML invalide : {e}")
        return None
    if not isinstance(data, dict):
        r.erreur(rel(chemin), "le fichier doit contenir un objet YAML (clé: valeur)")
        return None
    return data


def valider(data: dict, schema: dict, chemin: Path, r: Rapport) -> bool:
    erreurs = sorted(Draft7Validator(schema).iter_errors(data), key=lambda e: list(e.absolute_path))
    for e in erreurs:
        ou = "/".join(str(p) for p in e.absolute_path) or "(racine)"
        # Retrouver l'id de l'élément fautif pour un message lisible
        elem = data
        for p in list(e.absolute_path)[:2]:
            try:
                elem = elem[p]
            except (KeyError, IndexError, TypeError):
                break
        ident = f" [{elem.get('id')}]" if isinstance(elem, dict) and "id" in elem else ""
        r.erreur(rel(chemin), f"{ou}{ident} : {e.message}")
    return not erreurs


def lire_ids_md(chemin: Path, prefixe: str) -> set[str]:
    if not chemin.exists():
        return set()
    return set(re.findall(rf"^- \*\*({prefixe}\d+)\*\*", lire_md(chemin), re.M))


def lire_md(chemin: Path) -> str:
    """Texte Markdown sans ses blocs de code : les exemples ne sont pas des entrées."""
    return re.sub(r"^```.*?^```", "", chemin.read_text(encoding="utf-8"), flags=re.S | re.M)


def lire_ids_section(chemin: Path, prefixe: str, titre: str) -> set[str]:
    """Identifiants listés sous le titre « ## titre » (questions traitées, anomalies levées)."""
    if not chemin.exists():
        return set()
    _, _, section = lire_md(chemin).partition(f"\n## {titre}")
    return set(re.findall(rf"^- \*\*({prefixe}\d+)\*\*", section, re.M))


def fils_svg(txt: str) -> set[str]:
    """Fils cités dans un folio, en entier (wire234) ou en abrégé (w234)."""
    return {f"wire{n}" for n in re.findall(r"\b(?:wire|w)(\d{3})\b", txt)}


def ids_svg(chemins: list[Path]) -> tuple[set[str], set[str], set[str]]:
    fils, questions, anomalies = set(), set(), set()
    for c in chemins:
        txt = c.read_text(encoding="utf-8")
        fils |= fils_svg(txt)
        questions |= set(re.findall(r">(Q\d+)<", txt))
        anomalies |= set(re.findall(r">(A\d+)<", txt))
    return fils, questions, anomalies


# --------------------------------------------------------------------------- modèle
@dataclass
class Modele:
    nom: str
    zones: dict = field(default_factory=dict)
    equipements: dict = field(default_factory=dict)
    nodes: dict = field(default_factory=dict)
    fils: dict = field(default_factory=dict)

    def ajouter(self, data: dict, source: str, r: Rapport) -> None:
        for cle in CATEGORIES:
            cible = getattr(self, cle)
            for elem in data.get(cle, []):
                if elem["id"] in cible:
                    r.erreur(source, f"identifiant en double : {elem['id']}")
                cible[elem["id"]] = elem


def appliquer_delta(base: Modele, delta: dict, nom: str, source: str, r: Rapport) -> Modele:
    m = Modele(nom, *(copy.deepcopy(getattr(base, c)) for c in CATEGORIES))
    supprime = delta.get("supprime", {})
    for cle in CATEGORIES:
        cible = getattr(m, cle)
        for ident in supprime.get(cle, []):
            if ident not in cible:
                r.erreur(source, f"supprime.{cle} : {ident} n'existe pas dans la base ({base.nom})")
            cible.pop(ident, None)
        for elem in delta.get(cle, []):
            if elem["id"] in cible:
                r.erreur(source, f"{elem['id']} existe déjà dans la base ({base.nom}) : "
                                 f"le déclarer dans supprime.{cle} ou changer de numéro")
            cible[elem["id"]] = elem
    for f in delta.get("fils", []):
        if "remplace" in f and f["remplace"] not in supprime.get("fils", []):
            r.avert(source, f"{f['id']} remplace {f['remplace']}, mais {f['remplace']} n'est pas dans supprime.fils")
    return m


def controler(m: Modele, questions: set[str], traitees: set[str], r: Rapport) -> None:
    ou = m.nom
    for e in m.equipements.values():
        if "zone" in e and e["zone"] not in m.zones:
            r.erreur(ou, f"{e['id']} : zone inconnue « {e['zone']} » (voir releve/amenagement.yaml)")
    for n in m.nodes.values():
        if n["equipement"] not in m.equipements:
            r.erreur(ou, f"{n['id']} : équipement inconnu « {n['equipement']} »")
        if "monte_sur" in n:
            if n["monte_sur"] not in m.nodes:
                r.erreur(ou, f"{n['id']} : monte_sur vers un nœud inconnu ({n['monte_sur']})")
            elif n["monte_sur"] == n["id"]:
                r.erreur(ou, f"{n['id']} : monte_sur ne peut pas pointer sur lui-même")

    for f in m.fils.values():
        extremites = []
        for bout in ("de", "vers"):
            if f[bout] not in m.nodes:
                r.erreur(ou, f"{f['id']} : {bout} = {f[bout]}, nœud inconnu")
            else:
                extremites.append(m.nodes[f[bout]]["polarite"])
        if f["de"] == f["vers"]:
            r.erreur(ou, f"{f['id']} : les deux extrémités sont le même nœud")
        if len(extremites) == 2:
            pols = set(extremites)
            if pols == POLARITES_12V:
                r.erreur(ou, f"{f['id']} relie un + ({f['de']}/{f['vers']}) à un - : court-circuit")
            if pols & POLARITES_230V and pols & (POLARITES_12V | {"commute", "commande"}):
                r.erreur(ou, f"{f['id']} relie le 230 V au circuit 12 V")
            if len(pols & POLARITES_230V) > 1:
                r.erreur(ou, f"{f['id']} relie deux conducteurs 230 V différents ({' / '.join(sorted(pols))})")
            couleur = f.get("couleur")
            if couleur and pols == {"+"} and couleur != "rouge":
                r.avert(ou, f"{f['id']} : fil positif de couleur {couleur} (rouge attendu)")
            if couleur and pols == {"-"} and couleur not in ("noir", "jaune"):
                r.avert(ou, f"{f['id']} : fil négatif de couleur {couleur} (noir ou jaune attendu)")
            if couleur and len(pols) == 1 and (p := next(iter(pols))) in COULEURS_230V \
                    and couleur not in COULEURS_230V[p]:
                r.avert(ou, f"{f['id']} : conducteur {p} de couleur {couleur} "
                            f"({' ou '.join(sorted(COULEURS_230V[p]))} attendu)")
        if "section_mm2" in f and f["section_mm2"] not in SECTIONS_NORMALISEES and not f.get("section_indicative"):
            r.avert(ou, f"{f['id']} : section de {f['section_mm2']} mm² hors série normalisée "
                        f"(câble AWG ou mesure approximative ?)")

    paires = {}
    for f in m.fils.values():
        paires.setdefault(frozenset((f["de"], f["vers"])), []).append(f["id"])
    for ids in paires.values():
        if len(ids) > 1:
            r.avert(ou, f"{' et '.join(sorted(ids))} relient les mêmes nœuds : doublon, ou fil à supprimer ?")

    for cle in CATEGORIES:
        for elem in getattr(m, cle).values():
            for q in elem.get("questions", []):
                if q not in questions:
                    r.erreur(ou, f"{elem['id']} : question {q} absente de releve/questions.md")
                elif q in traitees:
                    r.avert(ou, f"{elem['id']} : cite {q}, déjà traitée (retirer la référence)")

    controler_contournements(m, r)

    sans_section = sorted(f["id"] for f in m.fils.values() if "section_mm2" not in f)
    if sans_section:
        r.info(f"{len(sans_section)} fil(s) de section inconnue : {', '.join(sans_section)}")

    relies = {f[b] for f in m.fils.values() for b in ("de", "vers")}
    relies |= {n["id"] for n in m.nodes.values() if "monte_sur" in n}
    relies |= {n["monte_sur"] for n in m.nodes.values() if "monte_sur" in n}
    orphelins = sorted(set(m.nodes) - relies)
    if orphelins:
        r.info(f"{len(orphelins)} nœud(s) sans fil (câblage non relevé ou non décrit) : {', '.join(orphelins)}")
    sans_node = sorted(set(m.equipements) - {n["equipement"] for n in m.nodes.values()})
    if sans_node:
        r.info(f"{len(sans_node)} équipement(s) sans nœud : {', '.join(sans_node)}")
    sans_zone = sorted(e["id"] for e in m.equipements.values() if "zone" not in e)
    if sans_zone:
        r.info(f"{len(sans_zone)} équipement(s) sans zone (non placés sur le plan) : {', '.join(sans_zone)}")
    r.ok(f"{len(m.zones)} zones, {len(m.equipements)} équipements, {len(m.nodes)} nœuds, {len(m.fils)} fils")


COUPURES = {"coupe-circuit", "fusible", "disjoncteur", "interrupteur"}


def controler_contournements(m: Modele, r: Rapport) -> None:
    """Un coupe-circuit, fusible, disjoncteur ou interrupteur à deux bornes ne doit pas être
    contourné : si ses deux bornes sont reliées par des fils seuls, il ne coupe plus rien."""
    parent = {n: n for n in m.nodes}

    def racine(n):
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n

    liaisons = [(f["de"], f["vers"]) for f in m.fils.values()]
    liaisons += [(n["id"], n["monte_sur"]) for n in m.nodes.values() if "monte_sur" in n]
    for a, b in liaisons:
        if a in parent and b in parent:
            parent[racine(a)] = racine(b)

    bornes = {}
    for n in m.nodes.values():
        bornes.setdefault(n["equipement"], []).append(n["id"])
    for eq, ns in sorted(bornes.items()):
        e = m.equipements.get(eq)
        if e and e["type"] in COUPURES and len(ns) == 2 and racine(ns[0]) == racine(ns[1]):
            r.erreur(m.nom, f"{eq} est contourné : ses bornes {ns[0]} et {ns[1]} sont reliées par des fils, "
                            f"il ne coupe plus rien")


def nodes_svg(txt: str) -> set[str]:
    """Nœuds cités dans un folio, en entier (node006) ou en abrégé (n006)."""
    return {f"node{n}" for n in re.findall(r"\b(?:node|n)(\d{3})\b", txt)}


def controler_nodes_svg(svgs: list[Path], m: "Modele", r: Rapport) -> None:
    """Les deux extrémités de chaque fil dessiné sur un folio doivent être citées sur ce même folio."""
    for c in svgs:
        txt = c.read_text(encoding="utf-8")
        cites = nodes_svg(txt)
        for n in sorted(set(re.findall(r"\bn\d{1,2}\b", txt))):
            r.avert(rel(c), f"{n} : abréger les nœuds sur trois chiffres (n006, pas n6)")
        # Un renvoi vers un autre folio peut citer un nœud d'une autre hypothèse : contrôlé par controler_renvois.
        ailleurs = set()
        for contenu, _ in renvois_svg(txt):
            if folios_cites(contenu):
                ailleurs |= nodes_svg(contenu)
        for n in sorted(cites - ailleurs - set(m.nodes)):
            r.erreur(rel(c), f"{n} figure sur le folio mais n'existe pas dans les données")
        manquants: dict[str, list[str]] = {}
        for w in sorted(fils_svg(txt) & set(m.fils)):
            for bout in ("de", "vers"):
                n = m.fils[w][bout]
                if n not in cites:
                    manquants.setdefault(n, []).append(w)
        for n, ws in sorted(manquants.items()):
            r.avert(rel(c), f"{n} (extrémité de {', '.join(ws)}) n'est pas cité sur le folio")


def renvois_svg(txt: str) -> list[tuple[str, tuple[float, float, float, float]]]:
    """Renvois d'un folio : texte des cadres « flag » (rect class flag ou flag-new) et leur rectangle."""
    textes = [(float(x), float(y), re.sub(r"<[^>]+>", "", t))
              for x, y, t in re.findall(r'<text[^>]* x="([\d.]+)" y="([\d.]+)"[^>]*>(.*?)</text>', txt)]
    renvois = []
    for x, y, w, h in re.findall(r'<rect class="flag(?:-new)?" x="([\d.]+)" y="([\d.]+)" '
                                 r'width="([\d.]+)" height="([\d.]+)"', txt):
        x, y, w, h = float(x), float(y), float(w), float(h)
        contenu = " ".join(t for tx, ty, t in textes if x - 2 <= tx <= x + w + 2 and y <= ty <= y + h + 2)
        renvois.append((contenu, (x, y, w, h)))
    return renvois


def folios_cites(texte: str) -> list[str]:
    """Folios cités dans un renvoi : « folio 2i », « folios 1 et 2c », « folio 2i ou 2k »."""
    folios = []
    for m in re.finditer(r"\bfolios? ((?:\d[a-z]?)(?:(?:, | et | ou )\d[a-z]?)*)\b", texte):
        folios += re.split(r", | et | ou ", m.group(1))
    return folios


def controler_renvois(svgs: list[Path], r: Rapport) -> None:
    """Un renvoi (fil raccordé d'un seul côté sur le folio) cite le nœud d'arrivée, et le folio où il est
    représenté s'il est ailleurs ; ce nœud doit être cité hors renvoi sur ce folio-là."""
    tous = {re.match(r"folio-(\w+?)-", c.name).group(1): c for c in RACINE.rglob("folio-*.svg")}
    for c in svgs:
        txt = c.read_text(encoding="utf-8")
        for contenu, _ in renvois_svg(txt):
            nodes = nodes_svg(contenu)
            if not nodes:
                r.avert(rel(c), f"renvoi « {contenu} » : aucun nœud cité")
                continue
            folios = folios_cites(contenu)
            cibles = []
            for f in folios:
                if f not in tous:
                    r.avert(rel(c), f"renvoi « {contenu} » : folio {f} introuvable")
                else:
                    cibles.append(tous[f])
            if not folios:
                cibles = [c]
            if not cibles:
                continue
            represente = set()
            for cible in cibles:
                t = cible.read_text(encoding="utf-8")
                dans_renvois = " ".join(contenu_r for contenu_r, _ in renvois_svg(t))
                hors = [n for n in re.findall(r"\b(?:node|n)\d{3}\b", re.sub(r"<[^>]+>", " ", t))]
                represente |= {f"node{n[-3:]}" for n in hors
                               if hors.count(n) > len(re.findall(rf"\b{n}\b", dans_renvois))}
            if not nodes & represente:
                ou = ", ".join(f"folio {f}" for f in folios) if folios else "ce folio"
                r.avert(rel(c), f"renvoi « {contenu} » : {', '.join(sorted(nodes))} non représenté sur {ou}")


def controler_svg(svgs: list[Path], fils_attendus: set[str], fils_existants: set[str],
                  questions: set[str], traitees: set[str], anomalies: set[str], levees: set[str],
                  ou: str, r: Rapport) -> None:
    if not svgs:
        r.avert(ou, "aucun schéma SVG trouvé")
        return
    dessin, qs, ans = ids_svg(svgs)
    for w in sorted(fils_attendus - dessin):
        r.avert(ou, f"{w} est dans les données mais absent des schémas")
    for w in sorted(dessin - fils_existants):
        r.erreur(ou, f"{w} figure sur un schéma mais n'existe pas dans les données")
    for q in sorted(qs - questions):
        r.erreur(ou, f"pastille {q} sur un schéma, absente de releve/questions.md")
    for q in sorted(qs & traitees):
        r.avert(ou, f"pastille {q} sur un schéma alors que la question est traitée")
    for a in sorted(ans - anomalies):
        r.erreur(ou, f"pastille {a} sur un schéma, absente de releve/anomalies.md")
    for a in sorted(ans & levees):
        r.avert(ou, f"pastille {a} sur un schéma alors que l'anomalie est levée")
    r.ok(f"{len(svgs)} schéma(s), {len(dessin & fils_existants)} fils dessinés")


def controler_implantation(m: Modele, r: Rapport) -> None:
    """Chaque zone et chaque équipement placé doivent figurer sur le plan (attributs data-zone / data-equipement)."""
    ou = rel(IMPLANTATION)
    if not IMPLANTATION.exists():
        r.avert(ou, "plan d'implantation absent")
        return
    txt = IMPLANTATION.read_text(encoding="utf-8")
    zones = set(re.findall(r'data-zone="([a-z0-9-]+)"', txt))
    equip = set(re.findall(r'data-equipement="([a-z0-9-]+)"', txt))
    places = {e["id"] for e in m.equipements.values() if "zone" in e}
    for z in sorted(set(m.zones) - zones):
        r.avert(ou, f"zone {z} absente du plan")
    for z in sorted(zones - set(m.zones)):
        r.erreur(ou, f"zone {z} dessinée mais absente de releve/amenagement.yaml")
    for e in sorted(places - equip):
        r.avert(ou, f"{e} a une zone mais n'est pas sur le plan")
    for e in sorted(equip - set(m.equipements)):
        r.erreur(ou, f"{e} dessiné mais absent des équipements")
    r.ok(f"{len(zones & set(m.zones))} zones et {len(equip & places)} équipements placés sur le plan")


def euros(x: float) -> str:
    return f"{x:,.0f} €".replace(",", " ")


def nomenclature(chemin: Path, schema: dict, attendu: str, m: Modele | None, anomalies: set[str],
                 delta: dict, r: Rapport) -> None:
    """Nomenclature chiffrée : cohérence avec l'hypothèse, prix renseignés, fils couverts, totaux par lot."""
    ou = rel(chemin)
    data = lire_yaml(chemin, r)
    if data is None or not valider(data, schema, chemin, r):
        return
    if data["hypothese"] != attendu:
        r.erreur(ou, f"hypothese = {data['hypothese']}, le dossier indique {attendu}")
    lots = data.get("lots", {})
    for nom, lot in lots.items():
        for a in lot.get("anomalies", []):
            if a not in anomalies:
                r.erreur(ou, f"lot {nom} : anomalie {a} absente de releve/anomalies.md")
    totaux, manquants, estimes = {}, 0, 0
    fils_couverts = set()
    for art in data["articles"]:
        lot = art.get("lot", "")
        nom = f"« {art['designation']} »"
        if lots and lot not in lots:
            r.erreur(ou, f"{nom} : lot « {lot} » non déclaré dans lots")
        if art["statut"] == "a_chiffrer":
            manquants += 1
            if "prix_unitaire" in art:
                r.avert(ou, f"{nom} : statut a_chiffrer mais prix renseigné")
        elif "prix_unitaire" not in art:
            r.erreur(ou, f"{nom} : prix_unitaire manquant (ou statut a_chiffrer)")
        if art["statut"] in ("catalogue", "devis") and not ("source" in art and "date_prix" in art):
            r.avert(ou, f"{nom} : prix {art['statut']} sans source ni date")
        if art["statut"] == "estimation":
            estimes += 1
        totaux[lot] = totaux.get(lot, 0) + art["quantite"] * art.get("prix_unitaire", 0)
        fils = art.get("fils", [])
        fils_couverts |= set(fils)
        if m is not None:
            inconnus = [w for w in fils if w not in m.fils]
            for w in inconnus:
                r.erreur(ou, f"{nom} : {w} n'existe pas dans l'hypothèse")
            if art["unite"] == "m" and fils and not inconnus:
                besoin = sum(m.fils[w].get("longueur_m", 0) for w in fils)
                if art["quantite"] < besoin:
                    r.avert(ou, f"{nom} : {art['quantite']} m commandés pour {besoin:g} m de fils")
    proposes = {f["id"] for f in delta.get("fils", [])}
    for w in sorted(proposes - fils_couverts):
        r.avert(ou, f"{w} est proposé dans cablage.yaml mais absent de la nomenclature")
    for nom in (list(lots) or sorted(totaux)):
        titre = lots.get(nom, {}).get("titre", nom or "sans lot")
        r.info(f"lot {nom or '-':<12} {euros(totaux.get(nom, 0)):>9}  {titre}")
    r.info(f"{'total':<17}{euros(sum(totaux.values())):>9}  "
           f"({estimes} prix estimé(s), {manquants} article(s) à chiffrer)")


def lire_entete(chemin: Path) -> tuple[dict | None, str]:
    """En-tête YAML d'un fichier Markdown (bloc entre deux lignes « --- » en tête), et le reste du texte."""
    texte = chemin.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texte, re.S)
    if not m:
        return None, texte
    return yaml.load(m.group(1), Loader=ChargeurStrict) or {}, texte[m.end():]


def proposition(chemin: Path, schema: dict, r: Rapport) -> None:
    ou = rel(chemin)
    try:
        entete, _ = lire_entete(chemin)
    except yaml.YAMLError as e:
        r.erreur(ou, f"en-tête YAML invalide : {e}")
        return
    if entete is None:
        r.info(f"{ou} : pas d'en-tête YAML (l'hypothèse n'apparaîtra pas dans la comparaison de la page)")
        return
    if not valider(entete, schema, chemin, r):
        return
    attendu = f"{chemin.parent.parent.name[0]}-{chemin.parent.name.split('-')[0]}"
    if entete["hypothese"] != attendu:
        r.erreur(ou, f"hypothese = {entete['hypothese']}, le dossier indique {attendu}")
    r.ok(f"{entete['hypothese']} · {entete['etat']} · {entete['titre']}")


def bilan(chemin: Path, schema: dict, equipements: dict, r: Rapport) -> None:
    data = lire_yaml(chemin, r)
    if data is None or not valider(data, schema, chemin, r):
        return
    profils = list(data["profils"])
    totaux = {p: 0.0 for p in profils}
    for c in data["consommateurs"]:
        if c["equipement"] not in equipements:
            r.erreur(rel(chemin), f"consommateur « {c['equipement']} » absent de releve/equipements.yaml")
        for p in c["heures_par_jour"]:
            if p not in data["profils"]:
                r.erreur(rel(chemin), f"{c['equipement']} : profil inconnu « {p} »")
        for p in profils:
            totaux[p] += c["courant_A"] * c.get("rapport_cyclique", 1) * c["heures_par_jour"].get(p, 0)
    for p in profils:
        wh = totaux[p] * data["tension_V"]
        r.info(f"profil {p:<12} {totaux[p]:6.1f} Ah/jour  ({wh:5.0f} Wh)  {data['profils'][p]['description']}")
    estimes = sum(1 for c in data["consommateurs"] if c.get("statut") == "estime")
    if estimes:
        r.info(f"{estimes}/{len(data['consommateurs'])} consommateurs sont des estimations")


# --------------------------------------------------------------------------- programme
def main() -> int:
    r = Rapport()
    schema = json.loads((RACINE / "outils/schema/donnees.schema.json").read_text(encoding="utf-8"))
    schema_bilan = json.loads((RACINE / "outils/schema/bilan.schema.json").read_text(encoding="utf-8"))
    questions = lire_ids_md(RELEVE / "questions.md", "Q")
    anomalies = lire_ids_md(RELEVE / "anomalies.md", "A")
    traitees = lire_ids_section(RELEVE / "questions.md", "Q", "Réponses")
    levees = lire_ids_section(RELEVE / "anomalies.md", "A", "Levées")

    # ---- Relevé
    r.section("Relevé (releve/)")
    releve = Modele("releve")
    invalides = []
    for nom in FICHIERS_RELEVE:
        chemin = RELEVE / nom
        data = lire_yaml(chemin, r)
        if data is None or not valider(data, schema, chemin, r):
            invalides.append(nom)
            continue
        for interdit in ("hypothese", "base", "supprime"):
            if interdit in data:
                r.erreur(rel(chemin), f"« {interdit} » n'a pas sa place dans le relevé")
        releve.ajouter(data, rel(chemin), r)
    for elem in (*releve.equipements.values(), *releve.nodes.values(), *releve.fils.values()):
        if elem.get("statut") == "propose":
            r.erreur("releve", f"{elem['id']} a le statut « propose » : un élément proposé va dans etudes/")
    for w in releve.fils:
        if int(w[4:]) >= 100:
            r.avert("releve", f"{w} : les numéros wire100+ sont réservés aux propositions")
    if invalides:
        r.info(f"contrôles croisés suspendus tant que {', '.join(invalides)} est invalide : corriger d'abord les erreurs ci-dessus")
        print(f"\n{r.erreurs} erreur(s), {r.avertissements} avertissement(s)")
        return 1
    controler(releve, questions, traitees, r)
    r.info(f"{len(questions) - len(traitees)} questions ouvertes, {len(traitees)} traitées, {len(anomalies) - len(levees)} anomalies en cours, {len(levees)} levées")

    r.section("Schémas du relevé (schemas/)")
    controler_svg(sorted((RACINE / "schemas").glob("*.svg")), set(releve.fils), set(releve.fils),
                  questions, traitees, anomalies, levees, "schemas", r)
    controler_nodes_svg(sorted((RACINE / "schemas").glob("folio-[1-9]*.svg")), releve, r)
    controler_renvois(sorted((RACINE / "schemas").glob("folio-[1-9]*.svg")), r)
    controler_implantation(releve, r)

    # ---- Hypothèses
    hyps = {}
    for chemin in sorted((RACINE / "etudes").glob("*/H*/cablage.yaml")):
        data = lire_yaml(chemin, r)
        if data is None or not valider(data, schema, chemin, r):
            continue
        if "hypothese" not in data or "base" not in data:
            r.erreur(rel(chemin), "les champs « hypothese » et « base » sont obligatoires")
            continue
        if data["hypothese"] in hyps:
            r.erreur(rel(chemin), f"hypothèse {data['hypothese']} déclarée deux fois")
        hyps[data["hypothese"]] = (chemin, data)

    modeles = {"releve": releve}

    def resoudre(ident: str, pile: tuple = ()) -> Modele | None:
        if ident in modeles:
            return modeles[ident]
        if ident in pile:
            r.erreur(ident, f"dépendance circulaire : {' -> '.join(pile + (ident,))}")
            return None
        if ident not in hyps:
            r.erreur(ident, "hypothèse de base introuvable")
            return None
        chemin, data = hyps[ident]
        base = resoudre(data["base"], pile + (ident,))
        if base is None:
            return None
        modeles[ident] = appliquer_delta(base, data, ident, rel(chemin), r)
        return modeles[ident]

    for ident, (chemin, data) in hyps.items():
        r.section(f"Hypothèse {ident} · {data.get('titre', '')} (base : {data['base']})")
        m = resoudre(ident)
        if m is None:
            continue
        controler(m, questions, traitees, r)
        ajoutes = {f["id"] for f in data.get("fils", [])}
        controler_svg(sorted(chemin.parent.glob("*.svg")), ajoutes, set(m.fils),
                      questions, traitees, anomalies, levees, rel(chemin.parent), r)
        controler_nodes_svg(sorted(chemin.parent.glob("*.svg")), m, r)
        controler_renvois(sorted(chemin.parent.glob("*.svg")), r)

    # ---- Installation cible : hypothèses retenues appliquées dans l'ordre (cible/cible.yaml)
    fichier_cible = CIBLE / "cible.yaml"
    if fichier_cible.exists():
        r.section("Installation cible (cible/)")
        data = lire_yaml(fichier_cible, r) or {}
        ids = data.get("hypotheses", [])
        if not ids:
            r.erreur(rel(fichier_cible), "la liste « hypotheses » est vide ou absente")
        m = None
        for i, ident in enumerate(ids):
            if ident not in hyps:
                r.erreur(rel(fichier_cible), f"hypothèse {ident} introuvable")
                m = None
                break
            chemin, delta = hyps[ident]
            m = resoudre(ident) if i == 0 else appliquer_delta(m, delta, "cible", rel(chemin), r)
            if m is None:
                break
            prop = chemin.parent / "proposition.md"
            etat = (lire_entete(prop)[0] or {}).get("etat") if prop.exists() else None
            if etat != "retenue":
                r.avert(rel(fichier_cible), f"{ident} est « {etat} », pas « retenue »")
        if m is not None:
            controler(m, questions, traitees, r)
            douze = {w for w, f in m.fils.items()
                     if not ({m.nodes[f["de"]]["polarite"], m.nodes[f["vers"]]["polarite"]} & POLARITES_230V)}
            controler_svg(sorted(CIBLE.glob("*.svg")), douze, set(m.fils),
                          questions, traitees, anomalies, levees, rel(CIBLE), r)
            controler_nodes_svg(sorted(CIBLE.glob("*.svg")), m, r)
            controler_renvois(sorted(CIBLE.glob("*.svg")), r)

    # ---- Folios générés : règles de dessin et SVG à jour (outils/folio.py)
    dispositions = sorted(RACINE.rglob("folio-*.yaml"))
    if dispositions:
        import folio as generateur
        r.section("Folios générés (folio-*.yaml → outils/folio.py)")
        mods = generateur.modeles()
        for chemin in dispositions:
            texte, err, crois = generateur.generer(chemin, mods, ecrire=False)
            for e in err:
                r.erreur(rel(chemin), e)
            for e in crois:   # croisements permis mais à réduire : admis explicitement dans la mise en page sinon
                r.avert(rel(chemin), e)
            svg = chemin.with_suffix(".svg")
            if not svg.exists() or svg.read_text(encoding="utf-8") != texte:
                r.erreur(rel(svg), "SVG pas à jour : lancer python Electricité/outils/folio.py")
            elif not err:
                r.ok(f"{rel(svg)} : règles de dessin respectées")

    # ---- Nomenclatures chiffrées
    schema_nomenc = json.loads((RACINE / "outils/schema/nomenclature.schema.json").read_text(encoding="utf-8"))
    for chemin in sorted((RACINE / "etudes").glob("*/H*/nomenclature.yaml")):
        attendu = f"{chemin.parent.parent.name[0]}-{chemin.parent.name.split('-')[0]}"
        r.section(f"Nomenclature {attendu} ({rel(chemin)})")
        delta = hyps.get(attendu, (None, {}))[1]
        nomenclature(chemin, schema_nomenc, attendu, modeles.get(attendu), anomalies, delta, r)

    # ---- Propositions
    schema_prop = json.loads((RACINE / "outils/schema/proposition.schema.json").read_text(encoding="utf-8"))
    chemins = sorted((RACINE / "etudes").glob("*/H*/proposition.md"))
    if chemins:
        r.section("Propositions (en-têtes de proposition.md)")
        for chemin in chemins:
            proposition(chemin, schema_prop, r)

    # ---- Bilan
    r.section("Bilan énergétique (commun/bilan-energetique.yaml)")
    bilan(RACINE / "commun/bilan-energetique.yaml", schema_bilan, releve.equipements, r)

    print(f"\n{r.erreurs} erreur(s), {r.avertissements} avertissement(s)")
    return 1 if r.erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
