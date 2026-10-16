"""Brouillon du folio « plan de bord » (phase 1 : fond de plan vide).

Coordonnées relevées sur le plan d'emménagement du constructeur (agrandi ×3),
puis converties en coordonnées SVG par P(). Avant à droite, bâbord en haut.
"""
import re
from pathlib import Path

ICI = Path(__file__).parent
# même bloc <style> que le folio 0
FOLIO0 = ICI.parent.parent / "Electricité" / "schemas" / "folio-0-implantation.svg"
STYLE = re.search(r"  <style>.*?</style>\n", FOLIO0.read_text(encoding="utf-8"), re.S).group(0)
# classes propres au fond de plan (à reporter dans tous les folios à l'intégration)
STYLE = STYLE.replace("  </style>", """    .amg{fill:none;stroke:var(--ink);stroke-width:1.1;stroke-linejoin:round}
    .amg-f{fill:var(--zone);stroke:var(--ink);stroke-width:1.1;stroke-linejoin:round}
    .amg-l{fill:none;stroke:var(--muted);stroke-width:.8}
    .deck{fill:none;stroke:var(--muted);stroke-width:1}
    .halo{paint-order:stroke;stroke:var(--sheet);stroke-width:4px;stroke-linejoin:round}
  </style>""")

K, OX, OY, CY = 0.75, 80, 196.25, 322   # X = OX + K·zx ; Y = OY + K·zy ; axe à zy = 322


def P(x, y):
    return f"{OX + K * x:.1f} {OY + K * y:.1f}"


def M(y):            # symétrique par rapport à l'axe
    return 2 * CY - y


def path(cls, *pts, close=False, extra=""):
    d = "M" + " L".join(P(*p) for p in pts) + (" Z" if close else "")
    return f'<path class="{cls}" d="{d}"{extra}/>'


def rect(cls, x0, y0, x1, y1, rx=0, extra=""):
    X0, Y0 = OX + K * x0, OY + K * y0
    return (f'<rect class="{cls}" x="{X0:.1f}" y="{Y0:.1f}" width="{K*(x1-x0):.1f}" '
            f'height="{K*(y1-y0):.1f}"' + (f' rx="{rx}"' if rx else "") + f"{extra}/>")


def circle(cls, x, y, r):
    return f'<circle class="{cls}" cx="{OX+K*x:.1f}" cy="{OY+K*y:.1f}" r="{K*r:.1f}"/>'


def ellipse(cls, x, y, rx, ry):
    return f'<ellipse class="{cls}" cx="{OX+K*x:.1f}" cy="{OY+K*y:.1f}" rx="{K*rx:.1f}" ry="{K*ry:.1f}"/>'


def text(cls, x, y, s, rot=None):
    X, Y = OX + K * x, OY + K * y
    tr = f' transform="rotate({rot} {X:.1f} {Y:.1f})"' if rot is not None else ""
    return f'<text class="{cls}" x="{X:.1f}" y="{Y:.1f}"{tr}>{s}</text>'


def bezier_hull(y_sign):
    """Demi-coque : tableau arrière → étrave (y_sign = 1 bâbord, -1 tribord)."""
    f = (lambda y: y) if y_sign == 1 else M
    return [(70, f(125)), (250, f(70)), (600, f(45)), (760, f(52)),
            (1000, f(62)), (1350, f(200)), (1645, CY)]


h = bezier_hull(1)
b = bezier_hull(-1)
coque = (f"M{P(15, CY)} C{P(15, 250)}, {P(30, 150)}, {P(*h[0])} "
         f"C{P(*h[1])}, {P(*h[2])}, {P(*h[3])} C{P(*h[4])}, {P(*h[5])}, {P(*h[6])} "
         f"C{P(*b[5])}, {P(*b[4])}, {P(*b[3])} C{P(*b[2])}, {P(*b[1])}, {P(*b[0])} "
         f"C{P(30, M(150))}, {P(15, M(250))}, {P(15, CY)} Z")
# liston intérieur (bord du pont), décalé de ~10 unités
hi = [(75, 140), (250, 85), (600, 60), (760, 66), (1000, 76), (1340, 210), (1610, CY)]
bi = [(x, M(y)) for x, y in hi]
liston = (f"M{P(32, CY)} C{P(32, 255)}, {P(45, 160)}, {P(*hi[0])} "
          f"C{P(*hi[1])}, {P(*hi[2])}, {P(*hi[3])} C{P(*hi[4])}, {P(*hi[5])}, {P(*hi[6])} "
          f"C{P(*bi[5])}, {P(*bi[4])}, {P(*bi[3])} C{P(*bi[2])}, {P(*bi[1])}, {P(*bi[0])} "
          f"C{P(45, M(160))}, {P(32, M(255))}, {P(32, CY)} Z")

el = []
A = el.append

A('<!-- Coque et pont -->')
A(f'<clipPath id="pb-coque"><path d="{coque}"/></clipPath>')
A(f'<path class="hull" d="{coque}"/>')
A('<g clip-path="url(#pb-coque)">')
A(f'<path class="deck" d="{liston}"/>')
A(path("bound", (40, CY), (1600, CY)))

A('<!-- Cockpit : bancs à lattes, barre franche, winches -->')
A(rect("amg", 75, 185, 400, 460))
A(rect("amg", 90, 185, 392, 265))          # banc bâbord
A(rect("amg", 90, 390, 392, 460))          # banc tribord
for x in range(110, 390, 22):
    A(path("amg-l", (x, 190), (x, 260)))
    A(path("amg-l", (x, 395), (x, 455)))
A(path("amg", (60, CY + 8), (200, CY + 8)))   # barre franche
A(circle("amg", 175, CY + 8, 7))             # mèche du safran
for y in (135, 175):
    A(circle("amg", 355, y, 15))
    A(circle("amg", 355, M(y) + 16, 15))
A(path("bound", (175, 190), (430, 125), (430, 280), (175, 345), close=True))  # couchette sous cockpit

A('<!-- Cloisons arrière du carré -->')
A(path("amg", (430, 52), (430, 265), (560, 265), (560, 47)))
A(path("amg", (480, 52), (480, 265)))
A(path("amg", (480, 165), (560, 165)))
A(path("amg", (480, 225), (560, 225)))
A(ellipse("amg", 520, 145, 22, 14))          # lavabo
A(f'<path class="amg-l" d="M{P(435, 85)} Q{P(480, 150)} {P(440, 255)}"/>')  # porte

A('<!-- Table à carte et son siège -->')
A(rect("amg", 565, 55, 640, 230))
A(path("amg", (565, 165), (640, 165)))
A(rect("amg-f", 640, 70, 755, 230))
A(path("amg", (755, 50), (755, 230)))

A('<!-- Descente et capot moteur -->')
A(rect("amg", 470, 265, 545, 390))
for x in (495, 520):
    A(path("amg-l", (x, 265), (x, 390)))
A(rect("amg", 548, 285, 612, 372))

A('<!-- Cabinet de toilette (tribord) -->')
A(path("amg", (400, 390), (580, 390), (580, 598)))
A(path("amg", (400, 390), (400, 598)))
A(path("amg", (480, 500), (580, 500)))
A(path("amg", (480, 500), (480, 598)))
A(circle("amg", 445, 445, 26))               # WC
A(circle("amg", 455, 412, 8))                # pompe
A(ellipse("amg", 530, 545, 38, 26))          # lavabo
A(rect("amg", 405, 545, 475, 590))           # caillebotis
for x in range(412, 475, 9):
    A(path("amg-l", (x, 548), (x, 587)))
A(path("amg-l", (585, 498), (612, 435)))     # porte

A('<!-- Cuisine (tribord) -->')
A(rect("amg", 585, 485, 665, 548))           # réchaud deux feux
A(rect("amg", 595, 495, 622, 538))
A(rect("amg", 628, 495, 655, 538))
A(rect("amg", 675, 505, 752, 582))           # glacière
A(rect("amg", 690, 345, 755, 475))           # bloc évier
A(rect("amg", 698, 352, 748, 405, rx=6))
A(rect("amg", 698, 415, 748, 468, rx=6))
A(rect("amg", 665, 318, 775, 338))           # plan de travail
A(path("amg", (760, 340), (760, 598)))

A('<!-- Carré : banquettes, table, puits de dérive -->')
A(path("amg-f", (760, 20), (1090, 80), (1090, 265), (760, 225), close=True))
A(path("amg-f", (760, 435), (1090, 385), (1090, 564), (760, 624), close=True))
A(path("amg-f", (820, 258), (978, 258), (985, 400), (828, 400), close=True))   # table
A(path("bound", (760, 345), (1090, 345)))    # puits de dérive (sous la table)

A('<!-- Cloison avant du carré, penderies -->')
A(path("amg", (1090, 116), (1090, 245)))
A(path("amg", (1090, 395), (1090, 528)))
A(path("amg", (1150, 135), (1150, 250)))
A(path("amg", (1150, 395), (1150, 512)))
A(path("amg", (1090, 250), (1150, 250)))
A(path("amg", (1090, 395), (1150, 395)))

A('<!-- Cabine de proue : couchette en V, pied de mât -->')
A(f'<path class="amg-f" d="M{P(1150, 210)} Q{P(1380, 230)} {P(1500, CY)} '
  f'Q{P(1380, M(230))} {P(1150, M(210))} Z"/>')
A(path("amg", (1160, 300), (1222, 312), (1222, 332), (1160, 344), close=True))  # pied de mât
A(path("amg", (1535, 268), (1535, 376)))     # cloison du puits à chaîne

A('</g>')
# repères d'orientation et zones (provisoires)
LBL = [
    ("Cockpit", 300, 350),
    ("Cabine de poupe (sous le cockpit)", 300, 300),
    ("Table à carte", 698, 150),
    ("Descente", 512, 328, -90),
    ("Toilette", 520, 480),
    ("Cuisine", 640, 478),
    ("Carré", 905, 330),
    ("Cabine de proue", 1330, 300),
]
el.append('<!-- Noms de zones (provisoires) -->')
for s, x, y, *r in LBL:
    el.append(text("ts mid halo", x, y, s, *r))
el.append(text("pin mid halo", 905, 372, "puits de dérive"))
el.append(text("pin mid halo", 1580, 410, "puits à chaîne"))
el.append(path("leader", (1580, 395), (1580, 340)))
el.append(text("pin mid halo", 1192, 368, "pied de mât"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" role="img" aria-label="Plan de bord vu de dessus : aménagement intérieur et pont du Gib'Sea 31, fond de plan vierge.">
  <title>Folio 6 · Plan de bord</title>
  <desc>Vue de dessus, avant à droite, bâbord en haut, redessinée d'après le plan d'emménagement du constructeur. Fond de plan vierge : les objets du bord (sécurité, armement) y seront placés avec leurs légendes.</desc>
{STYLE}  <rect class="bg" x="0" y="0" width="100%" height="100%"/>
  ''' + "\n  ".join(el) + f'''
  <text class="ts mid" x="{OX+K*700:.0f}" y="{OY+K*20:.0f}">BÂBORD</text>
  <text class="ts mid" x="{OX+K*700:.0f}" y="{OY+K*635:.0f}">TRIBORD</text>
  <text class="tb" x="{OX+K*1665:.0f}" y="{OY+K*CY+5:.0f}">AV</text>
  <text class="tb end" x="{OX-8:.0f}" y="{OY+K*CY+5:.0f}">AR</text>
  <!-- Zones de légende réservées (phase 3) -->
  <rect class="bound" x="20" y="20" width="1360" height="150"/>
  <text class="pin" x="28" y="34">légendes (bâbord)</text>
  <rect class="bound" x="20" y="700" width="1360" height="180"/>
  <text class="pin" x="28" y="714">légendes (tribord)</text>
</svg>
'''
(ICI / "folio-6-plan-de-bord.svg").write_text(svg, encoding="utf-8")
print("ok")
