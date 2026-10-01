"""Assemble le relevé et toutes les études en une seule page HTML (build/juju.html).

Usage : python Electricité/outils/page.py

Un menu en tête de page choisit la vue :
- « Relevé » (branche main) : folios de l'existant et des études fusionnées,
  comparaisons des hypothèses présentes sur main, anomalies et questions ;
- une vue par branche d'étude (etude/<axe>) : le README de l'étude (cadrage),
  les folios de ses hypothèses et leur comparaison.

Chaque branche est lue avec `git archive`, sans changer de branche ; la branche
courante est lue sur le disque, modifications non commitées comprises. Une branche
d'étude dont le dossier Electricité/ est identique à celui de main (étude fusionnée)
n'a pas de vue propre. Les fichiers du dépôt restent la source : la page se régénère.
"""
from __future__ import annotations

import html
import io
import posixpath
import re
import subprocess
import sys
import tarfile
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import quote

import yaml

RACINE = Path(__file__).resolve().parent.parent
BUILD = RACINE / "build"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=RACINE, capture_output=True, text=True,
                              encoding="utf-8", check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "?"


def extraire(branche: str, destination: Path) -> Path:
    """Copie le dossier Electricité/ de la branche dans destination ; renvoie sa racine."""
    depot = Path(git("rev-parse", "--show-toplevel"))
    prefixe = RACINE.relative_to(depot).as_posix()
    archive = subprocess.run(["git", "archive", "--format=tar", branche, "--", prefixe],
                             cwd=depot, capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(destination, filter="data")
    return destination / prefixe


def folio(chemin: Path, contexte: str, racine: Path) -> str:
    svg = chemin.read_text(encoding="utf-8")
    titre = re.search(r"<title>(.*?)</title>", svg, re.S)
    desc = re.search(r"<desc>(.*?)</desc>", svg, re.S)
    svg = re.sub(r"\s*<style>.*?</style>", "", svg, flags=re.S)
    svg = re.sub(r"\s*<title>.*?</title>|\s*<desc>.*?</desc>", "", svg, flags=re.S)
    numero, _, nom = (titre.group(1) if titre else chemin.stem).partition(" · ")
    return f"""
<section class="folio">
  <div class="folio-head">
    <span class="folio-no">{html.escape(numero.upper())}</span>
    <h2>{html.escape(nom or numero)}</h2>
    <p>{html.escape(contexte)} · <code>{html.escape(chemin.relative_to(racine).as_posix())}</code></p>
  </div>
  <figure>
    <div class="sheet">{svg}</div>
    <figcaption>{desc.group(1).strip() if desc else ""}</figcaption>
  </figure>
</section>"""


def inline(texte: str) -> str:
    texte = html.escape(texte)
    texte = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", texte)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", texte)


def liste_md(texte: str, prefixe: str, classe: str) -> str:
    """Liste « - **Xn** texte » avec ses lignes en retrait : sous-points (« - ») et réponses (« → »)."""
    items = []
    for bloc in re.finditer(rf"^- \*\*({prefixe}\d+)\*\* (.*)\n((?:[ \t]+\S.*\n?)*)", texte, re.M):
        ident, tete, suite = bloc.groups()
        sous, reponses = [], []
        for ligne in suite.splitlines():
            ligne = ligne.strip()
            if ligne.startswith(("→", "->")):
                reponses.append(f'<p class="rep">{inline(ligne.lstrip("→->").strip())}</p>')
            elif ligne.startswith("- "):
                sous.append(f"<li>{inline(ligne[2:])}</li>")
        corps = inline(tete) + (f'<ul class="sous">{"".join(sous)}</ul>' if sous else "") + "".join(reponses)
        items.append(f'<li><span class="tag {classe}">{ident}</span><div>{corps}</div></li>')
    return "\n".join(items) or '<li class="vide">Aucune.</li>'


def scinder(chemin: Path, titre: str) -> tuple[str, str]:
    """Sépare un fichier Markdown en deux au niveau du titre « ## titre »."""
    texte = chemin.read_text(encoding="utf-8") + "\n" if chemin.exists() else ""
    texte = re.sub(r"^```.*?^```", "", texte, flags=re.S | re.M)  # les exemples ne sont pas des entrées
    avant, _, apres = texte.partition(f"\n## {titre}")
    return avant, apres


ETATS = {"a_etudier": "À étudier", "proposee": "Proposée", "recommandee": "Recommandée",
         "retenue": "Retenue", "differee": "Différée", "ecartee_proposee": "À écarter (proposé)",
         "ecartee": "Écartée"}


def entete(chemin: Path) -> dict | None:
    m = re.match(r"---\n(.*?)\n---\n", chemin.read_text(encoding="utf-8"), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else None


def euros(x: float) -> str:
    return f"{x:,.0f} €".replace(",", " ")


def carte(dossier: Path, e: dict) -> str:
    total, estimes, a_chiffrer, produits = 0.0, 0, 0, []
    chemin = dossier / "nomenclature.yaml"
    if chemin.exists():
        for art in (yaml.safe_load(chemin.read_text(encoding="utf-8")) or {}).get("articles", []):
            total += art["quantite"] * art.get("prix_unitaire", 0)
            estimes += art["statut"] == "estimation"
            a_chiffrer += art["statut"] == "a_chiffrer"
            source = art.get("source", "")
            if source.startswith("http"):
                infos = [euros(art["prix_unitaire"])] if "prix_unitaire" in art else []
                if "date_prix" in art:
                    infos.append(f"relevé le {date.fromisoformat(art['date_prix']).strftime('%d/%m/%Y')}")
                produits.append(f'<li><a href="{html.escape(source)}" target="_blank" rel="noopener">'
                                f'{inline(art["designation"])}</a><span>{" · ".join(infos)}</span></li>')
    if chemin.exists():
        detail = [f"{estimes} prix estimé(s)" if estimes else "prix relevés",
                  f"{a_chiffrer} article(s) à chiffrer" if a_chiffrer else ""]
        cout = (f'<p class="hyp-cout"><strong>≈ {euros(total)}</strong>'
                f'<span>nomenclature · {", ".join(d for d in detail if d)}</span></p>')
    else:
        cout = '<p class="hyp-cout"><span>pas de nomenclature</span></p>'
    plus = "".join(f"<li>{inline(x)}</li>" for x in e.get("points_forts", []))
    moins = "".join(f"<li>{inline(x)}</li>" for x in e.get("points_faibles", []))
    return f"""
<article class="hyp etat-{e['etat']}">
  <div class="hyp-head"><span class="hyp-id">{html.escape(e['hypothese'])}</span><span class="etat">{ETATS[e['etat']]}</span></div>
  <h3>{inline(e['titre'])}</h3>
  <p class="hyp-resume">{inline(e['resume'])}</p>
  {cout}
  {f'<ul class="plus">{plus}</ul>' if plus else ''}{f'<ul class="moins">{moins}</ul>' if moins else ''}
  {f'<div class="produits"><h4>Produits</h4><ul>{"".join(produits)}</ul></div>' if produits else ''}
  {f'<p class="hyp-decision">{inline(e["decision"])}</p>' if e.get("decision") else ''}
</article>"""


def comparaisons(racine: Path, seulement: str = "") -> list[str]:
    sections = []
    etudes = racine / "etudes"
    for axe in sorted(d for d in etudes.iterdir() if d.is_dir() and (not seulement or d.name == seulement)) if etudes.exists() else []:
        dossiers = sorted(axe.glob("H*/proposition.md"), key=lambda c: int(re.match(r"H(\d+)", c.parent.name).group(1)))
        cartes = [carte(c.parent, e) for c in dossiers if (e := entete(c))]
        if not cartes:
            continue
        readme = axe / "README.md"
        titre = readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ") if readme.exists() else axe.name
        numero, _, nom = titre.partition(" · ")
        sections.append(f"""
<section class="folio">
  <div class="folio-head">
    <span class="folio-no">{html.escape(numero.upper())}</span>
    <h2>{html.escape(nom or numero)} · comparaison des hypothèses</h2>
    <p>Coûts : totaux des nomenclatures. Liens : relevés en ligne à la date indiquée, prix à confirmer avant achat. <code>{html.escape(axe.relative_to(racine).as_posix())}/H*/</code></p>
  </div>
  <div class="hyps">{"".join(cartes)}
  </div>
</section>""")
    return sections


DEPOT = "https://github.com/ZzubbuzZ/juju/blob"


def lien(texte: str, cible: str, base: str) -> str:
    """Lien Markdown : une adresse web est gardée ; un chemin relatif pointe vers le dépôt GitHub."""
    if not cible.startswith(("http://", "https://")):
        if not base:
            return texte
        cible = posixpath.normpath(posixpath.join(base, cible.split("#")[0]))
        cible = f"{DEPOT}/{quote(cible, safe='/')}"
    return f'<a href="{cible}" target="_blank" rel="noopener">{texte}</a>'


def en_ligne(texte: str, base: str = "") -> str:
    """Mise en forme d'une ligne : échappement, gras, code, liens."""
    morceaux = re.split(r"(`[^`]+`)", texte)
    sortie = []
    for m in morceaux:
        if m.startswith("`") and m.endswith("`") and len(m) > 1:
            sortie.append(f"<code>{html.escape(m[1:-1])}</code>")
            continue
        m = html.escape(m, quote=False)
        m = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", m)
        m = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", m)
        m = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda x: lien(x.group(1), x.group(2), base), m)
        sortie.append(m)
    return "".join(sortie)


def markdown(texte: str, base: str = "") -> str:
    """Convertisseur Markdown réduit, suffisant pour les README d'étude :
    titres, paragraphes, listes, tableaux, blocs de code, gras, barré, code et liens."""
    blocs, lignes, i = [], texte.splitlines(), 0
    while i < len(lignes):
        ligne = lignes[i]
        if not ligne.strip():
            i += 1
        elif ligne.startswith("```"):
            j = i + 1
            while j < len(lignes) and not lignes[j].startswith("```"):
                j += 1
            blocs.append(f"<pre>{html.escape(chr(10).join(lignes[i + 1:j]))}</pre>")
            i = j + 1
        elif m := re.match(r"(#{1,4}) (.*)", ligne):
            niveau = min(len(m.group(1)) + 1, 4)
            blocs.append(f"<h{niveau}>{en_ligne(m.group(2), base)}</h{niveau}>")
            i += 1
        elif ligne.startswith("|"):
            rangs = []
            while i < len(lignes) and lignes[i].startswith("|"):
                cellules = [c.strip() for c in lignes[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cellules):
                    rangs.append(cellules)
                i += 1
            tete, *corps = rangs
            th = "".join(f"<th>{en_ligne(c, base)}</th>" for c in tete)
            tr = "".join("<tr>" + "".join(f"<td>{en_ligne(c, base)}</td>" for c in r) + "</tr>" for r in corps)
            blocs.append(f'<div class="table"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
        elif re.match(r"(- |\d+\. )", ligne):
            balise = "ol" if ligne[0].isdigit() else "ul"
            items = []
            while i < len(lignes) and (re.match(r"(- |\d+\. )", lignes[i]) or (lignes[i].startswith("  ") and items)):
                if lignes[i].startswith("  "):
                    items[-1] += " " + lignes[i].strip()
                else:
                    items.append(re.sub(r"^(- |\d+\. )", "", lignes[i]))
                i += 1
            blocs.append(f"<{balise}>" + "".join(f"<li>{en_ligne(x, base)}</li>" for x in items) + f"</{balise}>")
        else:
            para = []
            while i < len(lignes) and lignes[i].strip() and not re.match(r"(#|\||```|- |\d+\. )", lignes[i]):
                para.append(lignes[i].strip())
                i += 1
            blocs.append(f"<p>{en_ligne(' '.join(para), base)}</p>")
    return "\n".join(blocs)


def cadrage(racine: Path, branche: str, dossier: str) -> str:
    """Section « cadrage » d'une vue d'étude : le README de l'étude, mis en forme."""
    readme = racine / "etudes" / dossier / "README.md"
    if not readme.exists():
        return ""
    texte = readme.read_text(encoding="utf-8")
    base = f"{branche}/{racine.name}/etudes/{dossier}"
    corps = re.sub(r"^<h2>.*?</h2>\n?", "", markdown(texte, base))
    titre = re.match(r"# (.*)", texte)
    return f"""
<section class="folio">
  <div class="folio-head">
    <span class="folio-no">CADRAGE</span>
    <h2>{html.escape(titre.group(1)) if titre else html.escape(dossier)}</h2>
    <p>README de l'étude · <code>etudes/{html.escape(dossier)}/README.md</code></p>
  </div>
  <div class="readme">
{corps}
  </div>
</section>"""


def notes(racine: Path) -> str:
    """Anomalies et questions du relevé."""
    actives, levees = scinder(racine / "releve/anomalies.md", "Levées")
    ouvertes, traitees = scinder(racine / "releve/questions.md", "Réponses")
    return NOTES.format(anomalies=liste_md(actives, "A", "tag-a"), levees=liste_md(levees, "A", "tag-a"),
                        questions=liste_md(ouvertes, "Q", "tag-q"), reponses=liste_md(traitees, "Q", "tag-q"))


def entete_vue(branche: str, commit: str) -> str:
    return (f'<p class="vue-source">Branche <code>{html.escape(branche)}</code> · '
            f'commit <code>{html.escape(commit)}</code></p>')


def vue_releve(racine: Path, branche: str, commit: str) -> str:
    folios = [folio(c, "Relevé", racine) for c in sorted((racine / "schemas").glob("*.svg"))]
    for c in sorted((racine / "etudes").glob("*/H*/*.svg")):
        folios.append(folio(c, f"Étude {c.parent.parent.name} · hypothèse {c.parent.name}", racine))
    return "\n".join([entete_vue(branche, commit), *folios, *comparaisons(racine), notes(racine)])


def vue_etude(racine: Path, branche: str, commit: str, dossier: str) -> str:
    folios = [folio(c, f"Étude {dossier} · hypothèse {c.parent.name}", racine)
              for c in sorted((racine / "etudes" / dossier).glob("H*/*.svg"))]
    renvoi = ('<p class="vue-renvoi">Folios de l\'existant, anomalies et questions : '
              'voir la vue <a href="#releve">Relevé</a>.</p>')
    return "\n".join([entete_vue(branche, commit), cadrage(racine, branche, dossier), *folios,
                      *comparaisons(racine, dossier), renvoi])


def dossier_etude(racine: Path, branche: str) -> tuple[str, str]:
    """Dossier etudes/<X-axe> d'une branche etude/<axe>, et libellé court « X · Titre »."""
    axe = branche.removeprefix("etude/")
    for d in sorted((racine / "etudes").glob(f"?-{axe}")):
        readme = d / "README.md"
        titre = readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ") if readme.exists() else d.name
        return d.name, f"{d.name[0]} · {titre.partition(' · ')[2] or axe}"
    return "", axe


def main() -> None:
    courante = git("rev-parse", "--abbrev-ref", "HEAD")
    etudes = [b for b in git("for-each-ref", "--format=%(refname:short)", "refs/heads/etude").splitlines() if b]
    arbre_main = git("rev-parse", "main:" + RACINE.name)
    vues, menu = [], []
    with tempfile.TemporaryDirectory() as tmp:
        def racine_de(branche: str) -> Path:
            if branche == courante:
                return RACINE
            return extraire(branche, Path(tmp) / branche.replace("/", "_"))

        racine = racine_de("main")
        vues.append(("releve", "Relevé", vue_releve(racine, "main", git("rev-parse", "--short", "main"))))
        for branche in etudes:
            if branche != courante and git("rev-parse", f"{branche}:{RACINE.name}") == arbre_main:
                continue  # étude fusionnée : déjà dans la vue Relevé
            racine = racine_de(branche)
            dossier, libelle = dossier_etude(racine, branche)
            if not dossier:
                continue
            vues.append((f"etude-{dossier[0]}", libelle,
                         vue_etude(racine, branche, git("rev-parse", "--short", branche), dossier)))

    vues[1:] = sorted(vues[1:])
    menu = "".join(f'<a href="#{i}" data-vue="{i}">{html.escape(l)}</a>' for i, l, _ in vues)
    sections = "\n".join(f'<div class="vue" id="{i}" data-titre="{html.escape(l)}">\n{c}\n</div>' for i, l, c in vues)
    page = GABARIT.format(date=date.today().strftime("%d/%m/%Y"), menu=menu, vues=sections)
    sortie = BUILD / "juju.html"
    sortie.parent.mkdir(exist_ok=True)
    sortie.write_text(page, encoding="utf-8", newline="\n")
    print(f"{len(vues)} vue(s) : {', '.join(l for _, l, _ in vues)} -> {sortie.relative_to(RACINE.parent).as_posix()}")


GABARIT = """<title>Juju · schémas électriques</title>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@400;500;600&display=swap">
<style>
:root{{
  --bg:#eef1f4; --sheet:#fbfcfd; --ink:#18212b; --muted:#5a6776; --grid:#e3e8ee; --line:#c9d1da;
  --pos:#c8231c; --unk:#1f6fbf; --warn:#e58a00; --on-warn:#1a1206; --new:#1d8a4a; --new-soft:#e2f3e8;
  --zone:#e8edf2; --ph:#8a5a2b; --ne:#2563c4; --pe:#2f9e44; --pey:#e6b800;
  --font:"IBM Plex Sans Condensed","Arial Narrow","Roboto Condensed",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Consolas,monospace;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --bg:#0f1419; --sheet:#151b22; --ink:#e3e8ee; --muted:#93a1b0; --grid:#1d252e; --line:#2c3743;
    --pos:#ff5a4f; --unk:#5aa9f5; --warn:#ffa53d; --on-warn:#1a1206; --new:#4fcf85; --new-soft:#15301f;
    --zone:#1f2832; --ph:#c8915a; --ne:#6aa7ff; --pe:#51cf66; --pey:#ffd43b;
    color-scheme:dark;
  }}
}}
:root[data-theme="dark"]{{
  --bg:#0f1419; --sheet:#151b22; --ink:#e3e8ee; --muted:#93a1b0; --grid:#1d252e; --line:#2c3743;
  --pos:#ff5a4f; --unk:#5aa9f5; --warn:#ffa53d; --on-warn:#1a1206; --new:#4fcf85; --new-soft:#15301f;
    --zone:#1f2832; --ph:#c8915a; --ne:#6aa7ff; --pe:#51cf66; --pey:#ffd43b;
  color-scheme:dark;
}}
body{{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:15px;line-height:1.55;padding-inline:clamp(16px,4vw,48px);padding-block:32px 64px}}
.wrap{{max-width:1240px;margin:0 auto;display:grid;gap:48px}}
header{{display:grid;gap:18px}}
.eyebrow{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
h1{{font-size:clamp(30px,4.2vw,42px);font-weight:600;letter-spacing:-.01em;line-height:1.1;margin:0;text-wrap:balance}}
.lede{{max-width:68ch;color:var(--muted);margin:0}}
.cartouche{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));border:1.5px solid var(--ink);background:var(--sheet);margin:0}}
.cartouche div{{padding:8px 12px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);display:grid;gap:2px}}
.cartouche dt{{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.cartouche dd{{margin:0;font-weight:500}}
.legend{{display:flex;flex-wrap:wrap;gap:10px 28px;font-size:13.5px;color:var(--muted)}}
.legend span{{display:inline-flex;align-items:center;gap:8px}}
.legend svg{{flex:none}}
section.folio{{display:grid;gap:18px}}
.folio-head{{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 16px;border-bottom:1.5px solid var(--ink);padding-bottom:8px}}
.folio-no{{font-family:var(--mono);font-size:13px;color:var(--muted);letter-spacing:.06em}}
h2{{font-size:23px;font-weight:600;margin:0;text-wrap:balance}}
.folio-head p{{margin:0;color:var(--muted);font-size:14px;flex-basis:100%}}
figure{{margin:0;display:grid;gap:10px}}
.sheet{{background-color:var(--sheet);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:20px 20px;border:1px solid var(--line);overflow-x:auto}}
.sheet svg{{display:block;width:100%;min-width:980px;height:auto}}
figcaption{{font-size:14px;color:var(--muted);max-width:85ch}}
.notes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px 40px}}
.notes h3{{font-family:var(--mono);font-size:12px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}}
.notes ol{{list-style:none;padding:0;margin:0;display:grid;gap:9px}}
.notes li{{display:grid;grid-template-columns:38px 1fr;gap:10px;align-items:baseline}}
.notes li.vide{{display:block;color:var(--muted)}}
.notes ul.sous{{margin:4px 0 0;padding-left:18px;display:grid;gap:3px}}
.notes ul.sous li{{display:list-item}}
.notes .rep{{margin:4px 0 0;padding-left:10px;border-left:2px solid var(--line);color:var(--muted)}}
.notes.traitees{{padding-top:20px;border-top:1px solid var(--line)}}
.tag{{font-family:var(--mono);font-size:11px;font-weight:500;text-align:center;border-radius:999px;padding:1px 0;line-height:1.5}}
.tag-a{{background:var(--warn);color:var(--on-warn)}}
.tag-q{{border:1.5px solid var(--unk);color:var(--unk)}}
code{{font-family:var(--mono);font-size:.88em}}
.hyps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,270px),1fr));gap:16px;align-items:start}}
.hyp{{background:var(--sheet);border:1px solid var(--line);padding:14px 16px 16px;display:grid;gap:10px;min-width:0}}
.hyp.etat-recommandee,.hyp.etat-retenue{{border:1.5px solid var(--new);box-shadow:inset 0 3px 0 var(--new)}}
.hyp.etat-ecartee,.hyp.etat-ecartee_proposee{{opacity:.78}}
.hyp-head{{display:flex;justify-content:space-between;align-items:center;gap:8px}}
.hyp-id{{font-family:var(--mono);font-size:12px;color:var(--muted);letter-spacing:.06em}}
.etat{{font-family:var(--mono);font-size:11px;font-weight:500;border:1.5px solid var(--unk);color:var(--unk);border-radius:999px;padding:0 9px;line-height:1.6;white-space:nowrap}}
.etat-recommandee .etat,.etat-retenue .etat{{border-color:var(--new);background:var(--new-soft);color:var(--new)}}
.etat-differee .etat{{border-color:var(--warn);color:var(--warn)}}
.etat-ecartee .etat,.etat-ecartee_proposee .etat{{border-color:var(--muted);color:var(--muted)}}
.hyp h3{{font-size:17px;font-weight:600;margin:0;line-height:1.25;text-wrap:balance}}
.hyp p{{margin:0}}
.hyp-resume{{color:var(--muted);font-size:14px}}
.hyp-cout{{display:grid;gap:0;border-block:1px solid var(--line);padding-block:6px}}
.hyp-cout strong{{font-size:24px;font-weight:600;font-variant-numeric:tabular-nums}}
.hyp-cout span{{font-size:12px;color:var(--muted)}}
.hyp ul{{list-style:none;margin:0;padding:0;display:grid;gap:4px;font-size:14px}}
.hyp ul.plus li,.hyp ul.moins li{{display:grid;grid-template-columns:16px 1fr;gap:4px}}
.hyp ul.plus li::before{{content:"+";color:var(--new);font-weight:600}}
.hyp ul.moins li::before{{content:"−";color:var(--pos);font-weight:600}}
.produits h4{{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}}
.produits li{{display:grid;gap:0}}
.produits a{{color:var(--ink);text-underline-offset:2px;overflow-wrap:anywhere}}
.produits a:focus-visible{{outline:2px solid var(--unk);outline-offset:2px}}
.produits span{{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}}
.hyp-decision{{font-size:13px;border-left:2px solid var(--line);padding-left:8px;color:var(--muted)}}
.menu{{display:flex;flex-wrap:wrap;gap:8px;position:sticky;top:0;z-index:1;background:var(--bg);padding-block:10px;border-bottom:1.5px solid var(--ink)}}
.menu a{{font-family:var(--mono);font-size:13px;color:var(--ink);text-decoration:none;border:1.5px solid var(--line);background:var(--sheet);padding:5px 12px;border-radius:999px;white-space:nowrap}}
.menu a:hover{{border-color:var(--ink)}}
.menu a:focus-visible{{outline:2px solid var(--unk);outline-offset:2px}}
.menu a[aria-current]{{background:var(--ink);border-color:var(--ink);color:var(--bg)}}
.vue{{display:grid;gap:48px}}
.vue[hidden]{{display:none}}
.vue-source,.vue-renvoi{{margin:0;color:var(--muted);font-size:14px}}
.vue-renvoi a{{color:var(--ink);text-underline-offset:2px}}
.readme{{max-width:85ch;display:grid;gap:12px}}
.readme h2,.readme h3,.readme h4{{margin:14px 0 0;font-weight:600;text-wrap:balance}}
.readme h2{{font-size:19px}}.readme h3{{font-size:16px}}.readme h4{{font-size:15px}}
.readme p,.readme ul,.readme ol{{margin:0}}
.readme ul,.readme ol{{padding-left:22px;display:grid;gap:4px}}
.readme a{{color:var(--ink);text-underline-offset:2px;overflow-wrap:anywhere}}
.readme a:focus-visible{{outline:2px solid var(--unk);outline-offset:2px}}
.readme pre{{margin:0;padding:10px 12px;background:var(--sheet);border:1px solid var(--line);overflow-x:auto;font-family:var(--mono);font-size:12.5px}}
.readme .table{{overflow-x:auto;max-width:100%}}
.readme table{{border-collapse:collapse;font-size:14px;background:var(--sheet)}}
.readme th,.readme td{{border:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}}
.readme th{{font-weight:600}}
/* dessin */
.bg{{fill:transparent}}
svg text{{font-family:var(--font);fill:var(--ink)}}
.t{{font-size:12.5px}}.tb{{font-size:13px;font-weight:600}}.ts{{font-size:11.5px;fill:var(--muted)}}
.id{{font-family:var(--mono);font-size:10.5px;fill:var(--muted)}}.idn{{font-family:var(--mono);font-size:10.5px;fill:var(--new)}}
.pin{{font-family:var(--mono);font-size:8.5px;fill:var(--ink)}}
.tu{{fill:var(--unk)}}.tn{{fill:var(--new)}}.mid{{text-anchor:middle}}.end{{text-anchor:end}}
.p,.n,.u,.lever,.bound,.ph,.ne,.pe,.pey,.leader{{fill:none;stroke-linecap:round;stroke-linejoin:round}}
.ph{{stroke:var(--ph)}}.ne{{stroke:var(--ne)}}.pe{{stroke:var(--pe)}}.pey{{stroke:var(--pey);stroke-dasharray:6 6;stroke-linecap:butt}}
.hull{{fill:var(--sheet);stroke:var(--ink);stroke-width:2}}.zone{{fill:var(--zone);stroke:var(--muted);stroke-width:1}}
.zone-pont{{fill:none;stroke:var(--muted);stroke-width:1.2;stroke-dasharray:4 3}}.leader{{stroke:var(--muted);stroke-width:1}}
.callout{{fill:var(--sheet);stroke:var(--ink);stroke-width:1.2}}
.p{{stroke:var(--pos)}}.n{{stroke:var(--ink)}}
.u{{stroke:var(--unk);stroke-width:1.6;stroke-dasharray:6 4}}
.bound{{stroke:var(--muted);stroke-width:1;stroke-dasharray:2 4}}
.w1{{stroke-width:1.3}}.w2{{stroke-width:2}}.w3{{stroke-width:2.8}}.w4{{stroke-width:4}}.w5{{stroke-width:5.5}}
.box{{fill:var(--sheet);stroke:var(--ink);stroke-width:1.4}}
.box-new{{fill:var(--new-soft);stroke:var(--new);stroke-width:1.6}}
.box-unk{{fill:var(--sheet);stroke:var(--unk);stroke-width:1.5;stroke-dasharray:6 4}}
.fuse{{fill:var(--sheet);stroke:var(--ink);stroke-width:1.3}}
.fuse-new{{fill:var(--new-soft);stroke:var(--new);stroke-width:1.6}}
.dp{{fill:var(--pos)}}.dn{{fill:var(--ink)}}
.term{{fill:var(--sheet);stroke:var(--ink);stroke-width:1.4}}
.lever{{stroke:var(--ink);stroke-width:2}}
.flag{{fill:var(--sheet);stroke:var(--ink);stroke-width:1.2}}
.flag-new{{fill:var(--new-soft);stroke:var(--new);stroke-width:1.4}}
.mk-a circle{{fill:var(--warn)}}
.mk-a text{{fill:var(--on-warn);font-family:var(--mono);font-size:9.5px;font-weight:500}}
.mk-q circle{{fill:var(--sheet);stroke:var(--unk);stroke-width:1.5}}
.mk-q text{{fill:var(--unk);font-family:var(--mono);font-size:9.5px;font-weight:500}}
</style>

<div class="wrap">
<header>
  <div class="eyebrow">Juju · Gib'Sea 31 · 1984 · électricité</div>
  <h1>Schémas électriques de Juju</h1>
  <p class="lede">Page générée à partir des folios SVG du dépôt. Les données de câblage (YAML) et les schémas sont contrôlés par <code>outils/verifier.py</code>.</p>
  <dl class="cartouche">
    <div><dt>Navire</dt><dd>Juju · Gib'Sea 31</dd></div>
    <div><dt>Contenu</dt><dd>relevé et études en cours</dd></div>
    <div><dt>Générée le</dt><dd>{date}</dd></div>
  </dl>
  <div class="legend" aria-label="Légende">
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--pos);stroke-width:3"/></svg>positif</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--ink);stroke-width:3"/></svg>négatif</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--ph);stroke-width:3"/></svg>230 V phase</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--ne);stroke-width:3"/></svg>neutre</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--pe);stroke-width:3"/><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--pey);stroke-width:3;stroke-dasharray:6 6"/></svg>terre</span>
    <span><svg width="34" height="12"><line x1="2" y1="6" x2="32" y2="6" style="stroke:var(--muted);stroke-width:5.5"/></svg>35–50 mm²</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--muted);stroke-width:2.5"/></svg>4–10 mm²</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--muted);stroke-width:1.3"/></svg>1,5–2,5 mm²</span>
    <span><svg width="34" height="10"><line x1="2" y1="5" x2="32" y2="5" style="stroke:var(--unk);stroke-width:1.6;stroke-dasharray:6 4"/></svg>zone d'ombre</span>
    <span><svg width="22" height="22"><circle cx="11" cy="11" r="9" style="fill:var(--warn)"/></svg>anomalie (A)</span>
    <span><svg width="22" height="22"><circle cx="11" cy="11" r="9" style="fill:var(--sheet);stroke:var(--unk);stroke-width:1.5"/></svg>question à relever (Q)</span>
    <span><svg width="30" height="16"><rect x="1" y="2" width="28" height="12" style="fill:var(--new-soft);stroke:var(--new);stroke-width:1.5"/></svg>nouveau (hypothèse)</span>
    <span><svg width="22" height="12"><circle cx="11" cy="6" r="4" style="fill:var(--ink)"/></svg>point = connexion ; croisement sans point = pas de connexion</span>
  </div>
  <nav class="menu" aria-label="Choix de la vue">{menu}</nav>
</header>
{vues}
</div>
<script>
(function () {{
  var vues = document.querySelectorAll(".vue"), liens = document.querySelectorAll(".menu a");
  function afficher() {{
    var id = location.hash.slice(1), cible = document.getElementById(id);
    if (!cible || !cible.classList.contains("vue")) {{ cible = vues[0]; id = cible.id; }}
    vues.forEach(function (v) {{ v.hidden = v !== cible; }});
    liens.forEach(function (a) {{
      if (a.dataset.vue === id) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    }});
    document.title = "Juju · " + cible.dataset.titre;
  }}
  window.addEventListener("hashchange", function () {{ afficher(); window.scrollTo(0, 0); }});
  afficher();
}})();
</script>
"""

NOTES = """
<section class="folio">
  <div class="folio-head"><span class="folio-no">RELEVÉ</span><h2>Anomalies et questions</h2></div>
  <div class="notes">
    <div><h3>Anomalies en cours</h3><ol>
{anomalies}
    </ol></div>
    <div><h3>Questions à relever</h3><ol>
{questions}
    </ol></div>
  </div>
  <div class="notes traitees">
    <div><h3>Anomalies levées</h3><ol>
{levees}
    </ol></div>
    <div><h3>Réponses reçues</h3><ol>
{reponses}
    </ol></div>
  </div>
</section>"""

if __name__ == "__main__":
    main()
