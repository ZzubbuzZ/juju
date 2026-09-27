"""Assemble les folios SVG en une page HTML consultable (build/schemas.html).

Usage : python Electricité/outils/page.py

La page reprend, dans l'ordre : les folios du relevé (schemas/), puis ceux des
hypothèses présentes sur la branche courante (etudes/*/H*/), puis les listes
d'anomalies et de questions. Les SVG restent la source : la page se régénère.
"""
from __future__ import annotations

import html
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "build" / "schemas.html"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=RACINE, capture_output=True, text=True,
                              encoding="utf-8", check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "?"


def folio(chemin: Path, contexte: str) -> str:
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
    <p>{html.escape(contexte)} · <code>{html.escape(chemin.relative_to(RACINE).as_posix())}</code></p>
  </div>
  <figure>
    <div class="sheet">{svg}</div>
    <figcaption>{desc.group(1).strip() if desc else ""}</figcaption>
  </figure>
</section>"""


def liste_md(chemin: Path, prefixe: str, classe: str) -> str:
    if not chemin.exists():
        return ""
    items = []
    for ident, texte in re.findall(rf"^- \*\*({prefixe}\d+)\*\* (.*)$", chemin.read_text(encoding="utf-8"), re.M):
        texte = re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(texte))
        items.append(f'<li><span class="tag {classe}">{ident}</span><span>{texte}</span></li>')
    return "\n".join(items)


def main() -> None:
    folios = [folio(c, "Relevé") for c in sorted((RACINE / "schemas").glob("*.svg"))]
    for c in sorted((RACINE / "etudes").glob("*/H*/*.svg")):
        folios.append(folio(c, f"Étude {c.parent.parent.name} · hypothèse {c.parent.name}"))

    branche, commit = git("rev-parse", "--abbrev-ref", "HEAD"), git("rev-parse", "--short", "HEAD")
    anomalies = liste_md(RACINE / "releve/anomalies.md", "A", "tag-a")
    questions = liste_md(RACINE / "releve/questions.md", "Q", "tag-q")

    page = GABARIT.format(
        branche=html.escape(branche), commit=html.escape(commit), date=date.today().strftime("%d/%m/%Y"),
        folios="\n".join(folios), anomalies=anomalies, questions=questions)
    SORTIE.parent.mkdir(exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8", newline="\n")
    print(f"{len(folios)} folio(s) -> {SORTIE.relative_to(RACINE.parent).as_posix()}")


GABARIT = """<title>Schémas 12 V de Juju</title>
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
.tag{{font-family:var(--mono);font-size:11px;font-weight:500;text-align:center;border-radius:999px;padding:1px 0;line-height:1.5}}
.tag-a{{background:var(--warn);color:var(--on-warn)}}
.tag-q{{border:1.5px solid var(--unk);color:var(--unk)}}
code{{font-family:var(--mono);font-size:.88em}}
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
    <div><dt>Branche</dt><dd><code>{branche}</code></dd></div>
    <div><dt>Commit</dt><dd><code>{commit}</code></dd></div>
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
</header>
{folios}
<section class="folio">
  <div class="folio-head"><span class="folio-no">RELEVÉ</span><h2>Anomalies et questions ouvertes</h2></div>
  <div class="notes">
    <div><h3>Anomalies</h3><ol>
{anomalies}
    </ol></div>
    <div><h3>Questions à relever</h3><ol>
{questions}
    </ol></div>
  </div>
</section>
</div>
"""

if __name__ == "__main__":
    main()
