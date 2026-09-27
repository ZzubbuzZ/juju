"""Vérificateur de cohérence des données électriques de Juju.

Usage (depuis la racine du dépôt ou n'importe où) :
    python Electricité/outils/verifier.py

Contrôles :
  1. syntaxe YAML, clés en double comprises (PyYAML les écrase sans prévenir) ;
  2. conformité aux schémas JSON de outils/schema/ ;
  3. identifiants uniques, références existantes (nœuds, équipements, questions) ;
  4. règles électriques : pas de fil entre un + et un -, couleur cohérente ;
  5. chaque fil des données figure sur les schémas SVG, et inversement ;
  6. hypothèses des études : application du delta sur leur base, puis mêmes contrôles ;
  7. bilan énergétique : Ah consommés par jour pour chaque profil.

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
FICHIERS_RELEVE = ["equipements.yaml", "netlist.yaml", "wirelist.yaml"]
POLARITES_12V = {"+", "-"}
POLARITES_230V = {"230V-phase", "230V-neutre", "230V-terre"}

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
    return set(re.findall(rf"^- \*\*({prefixe}\d+)\*\*", chemin.read_text(encoding="utf-8"), re.M))


def ids_svg(chemins: list[Path]) -> tuple[set[str], set[str], set[str]]:
    fils, questions, anomalies = set(), set(), set()
    for c in chemins:
        txt = c.read_text(encoding="utf-8")
        fils |= set(re.findall(r"wire\d{3}", txt))
        questions |= set(re.findall(r">(Q\d+)<", txt))
        anomalies |= set(re.findall(r">(A\d+)<", txt))
    return fils, questions, anomalies


# --------------------------------------------------------------------------- modèle
@dataclass
class Modele:
    nom: str
    equipements: dict = field(default_factory=dict)
    nodes: dict = field(default_factory=dict)
    fils: dict = field(default_factory=dict)

    def ajouter(self, data: dict, source: str, r: Rapport) -> None:
        for cle in ("equipements", "nodes", "fils"):
            cible = getattr(self, cle)
            for elem in data.get(cle, []):
                if elem["id"] in cible:
                    r.erreur(source, f"identifiant en double : {elem['id']}")
                cible[elem["id"]] = elem


def appliquer_delta(base: Modele, delta: dict, nom: str, source: str, r: Rapport) -> Modele:
    m = Modele(nom, copy.deepcopy(base.equipements), copy.deepcopy(base.nodes), copy.deepcopy(base.fils))
    supprime = delta.get("supprime", {})
    for cle in ("equipements", "nodes", "fils"):
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


def controler(m: Modele, questions: set[str], r: Rapport) -> None:
    ou = m.nom
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
            if pols == {"+"} and f["couleur"] != "rouge":
                r.avert(ou, f"{f['id']} : fil positif de couleur {f['couleur']} (rouge attendu)")
            if pols == {"-"} and f["couleur"] not in ("noir", "jaune"):
                r.avert(ou, f"{f['id']} : fil négatif de couleur {f['couleur']} (noir ou jaune attendu)")

    for cle in ("equipements", "nodes", "fils"):
        for elem in getattr(m, cle).values():
            for q in elem.get("questions", []):
                if q not in questions:
                    r.erreur(ou, f"{elem['id']} : question {q} absente de releve/questions.md")

    relies = {f[b] for f in m.fils.values() for b in ("de", "vers")}
    relies |= {n["id"] for n in m.nodes.values() if "monte_sur" in n}
    relies |= {n["monte_sur"] for n in m.nodes.values() if "monte_sur" in n}
    orphelins = sorted(set(m.nodes) - relies)
    if orphelins:
        r.info(f"{len(orphelins)} nœud(s) sans fil (câblage non relevé ou non décrit) : {', '.join(orphelins)}")
    sans_node = sorted(set(m.equipements) - {n["equipement"] for n in m.nodes.values()})
    if sans_node:
        r.info(f"{len(sans_node)} équipement(s) sans nœud : {', '.join(sans_node)}")
    r.ok(f"{len(m.equipements)} équipements, {len(m.nodes)} nœuds, {len(m.fils)} fils")


def controler_svg(svgs: list[Path], fils_attendus: set[str], fils_existants: set[str],
                  questions: set[str], anomalies: set[str], ou: str, r: Rapport) -> None:
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
    for a in sorted(ans - anomalies):
        r.erreur(ou, f"pastille {a} sur un schéma, absente de releve/anomalies.md")
    r.ok(f"{len(svgs)} schéma(s), {len(dessin & fils_existants)} fils dessinés")


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
    controler(releve, questions, r)
    r.info(f"{len(questions)} questions ouvertes ou traitées, {len(anomalies)} anomalies")

    r.section("Schémas du relevé (schemas/)")
    controler_svg(sorted((RACINE / "schemas").glob("*.svg")), set(releve.fils), set(releve.fils),
                  questions, anomalies, "schemas", r)

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
        controler(m, questions, r)
        ajoutes = {f["id"] for f in data.get("fils", [])}
        controler_svg(sorted(chemin.parent.glob("*.svg")), ajoutes, set(m.fils),
                      questions, anomalies, rel(chemin.parent), r)

    # ---- Bilan
    r.section("Bilan énergétique (commun/bilan-energetique.yaml)")
    bilan(RACINE / "commun/bilan-energetique.yaml", schema_bilan, releve.equipements, r)

    print(f"\n{r.erreurs} erreur(s), {r.avertissements} avertissement(s)")
    return 1 if r.erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
