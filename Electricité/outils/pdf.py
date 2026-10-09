#!/usr/bin/env python3
"""Imprime la page de consultation (build/juju.html) en PDF A4 paysage : build/juju.pdf.

Usage :
    python Electricité/outils/pdf.py              # régénère la page (page.py), puis le PDF
    python Electricité/outils/pdf.py --sans-page  # imprime build/juju.html tel quel

Toutes les vues sont imprimées à la suite (Relevé, puis chaque étude en cours) : une page de garde
avec la légende, puis un folio par page, réduit pour tenir dans la page ; comparaisons, cadrages,
anomalies et questions suivent sur des pages à elles. Signets du PDF tirés des titres, numéro de
page en pied. Dépendance : playwright (pip install playwright, puis python -m playwright install chromium).
Variable d'environnement CHROMIUM : chemin d'un Chromium déjà installé, à utiliser à la place.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page  # noqa: E402

# Feuille d'impression ajoutée à la page : thème clair, toutes les vues, un folio par page.
IMPRESSION = """
@page { size: A4 landscape; margin: 11mm 12mm 13mm; }
:root, :root[data-theme] {
  --bg:#ffffff; --sheet:#ffffff; --ink:#18212b; --muted:#5a6776; --grid:#eef1f4; --line:#c9d1da;
  --pos:#c8231c; --unk:#1f6fbf; --warn:#e58a00; --on-warn:#1a1206; --new:#1d8a4a; --new-soft:#e2f3e8;
  --zone:#e8edf2; --ph:#8a5a2b; --ne:#2563c4; --pe:#2f9e44; --pey:#e6b800; color-scheme: light;
}
html, body { background: #fff; }
body { padding: 0; font-size: 12.5px; line-height: 1.45; }
.wrap { max-width: none; gap: 0; display: block; }
.menu, script { display: none !important; }
header { gap: 14px; break-after: page; }
h1 { font-size: 30px; }
.vue, .vue[hidden] { display: block !important; }
.vue-titre { break-before: page; font-size: 26px; margin: 0 0 6px; }
.vue-source, .vue-renvoi { margin: 0 0 8px; }
section.folio { break-before: page; display: block; }
.folio-head { margin-bottom: 8px; padding-bottom: 5px; }
h2 { font-size: 18px; }
.folio-head p { font-size: 11.5px; }
figure { display: block; }
.sheet { overflow: visible; border: 1px solid var(--line); text-align: center; }
.sheet svg { display: inline-block; width: 100%; min-width: 0; height: auto; max-height: 148mm; }
figure { break-inside: avoid; }
figcaption { font-size: 11.5px; margin-top: 6px; max-width: none; }
.hyps { display: block; columns: 3; column-gap: 12px; }
.hyps .hyp { margin-bottom: 12px; display: grid; }
.notes li, .readme table, .readme pre { break-inside: avoid; }
.hyp { break-inside: auto; }
.hyp-cout strong { font-size: 19px; }
.notes, .notes > div { display: block; }
.notes > div { margin-bottom: 14px; }
.notes ol { display: block; columns: 2; column-gap: 28px; }
.notes li { margin-bottom: 7px; }
.notes.traitees { break-before: page; }
.readme { max-width: none; }
a { color: inherit; }
"""

PIED = ('<div style="width:100%;font-family:Arial,sans-serif;font-size:8px;color:#5a6776;'
        'padding:0 12mm;display:flex;justify-content:space-between">'
        '<span>Juju · Gib\'Sea 31 · schémas électriques</span>'
        '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')


def imprimer(html: Path, sortie: Path) -> None:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        navigateur = pw.chromium.launch(executable_path=os.environ.get("CHROMIUM") or None)
        p = navigateur.new_page(color_scheme="light")
        p.goto(html.resolve().as_uri(), wait_until="networkidle")
        p.add_style_tag(content=IMPRESSION)
        # un titre par vue (le menu disparaît à l'impression)
        p.evaluate("""() => document.querySelectorAll('.vue').forEach(v => {
            const h = document.createElement('h1'); h.className = 'vue-titre';
            h.textContent = v.dataset.titre; v.prepend(h); v.hidden = false; })""")
        p.emulate_media(media="print")
        p.pdf(path=str(sortie), format="A4", landscape=True, print_background=True,
              display_header_footer=True, header_template="<span></span>", footer_template=PIED,
              margin={"top": "11mm", "bottom": "13mm", "left": "12mm", "right": "12mm"},
              outline=True, tagged=True)
        navigateur.close()


def main(args: list[str]) -> int:
    if "--sans-page" not in args:
        page.main()
    html = page.BUILD / "juju.html"
    sortie = page.BUILD / "juju.pdf"
    imprimer(html, sortie)
    print(f"PDF A4 paysage -> {sortie.relative_to(page.RACINE.parent).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
