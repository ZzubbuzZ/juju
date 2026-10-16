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
    .halo{paint-order:stroke;stroke:var(--sheet);stroke-width:4px;stroke-linejoin:round}
    .amg-b{fill:var(--sheet);stroke:var(--ink);stroke-width:1.1;stroke-linejoin:round}
    svg{--sol-b:#d3d7db;--sol-b-l:#a2a9b0;--sol-h:#e9eaea;--sol-h-l:#c3c6c9;--mat:#f3eee4;--mat-l:#b9b2a5;--mat-b:#8f887c;--vaig:#e6d3b3;--teck:#d8bd8a;--teck-l:#bb9b66;--teck-j:#7a5c35}
    @media (prefers-color-scheme: dark){svg{--sol-b:#2b333b;--sol-b-l:#3f4952;--sol-h:#363d44;--sol-h-l:#4b545d;--mat:#3a3631;--mat-l:#59534a;--mat-b:#736b5f;--vaig:#4b3e2c;--teck:#5a4630;--teck-l:#6e5739;--teck-j:#2b2015}}
    .sol-b{fill:url(#pb-sol-b)}.sol-h{fill:url(#pb-sol-h)}
    .mat{fill:url(#pb-mat);stroke:var(--ink);stroke-width:1.1;stroke-linejoin:round}
    .teck{fill:url(#pb-teck);stroke:var(--ink);stroke-width:1.1;stroke-linejoin:round}
    .teck-j{fill:none;stroke:var(--teck-j);stroke-width:.9}
    .vaig{fill:none;stroke:var(--vaig)}
  </style>""")
# textures (motifs en px)
DEFS = """  <defs>
    <pattern id="pb-sol-b" width="60" height="18" patternUnits="userSpaceOnUse">
      <rect width="60" height="18" style="fill:var(--sol-b)"/>
      <path d="M0 .5H60M0 9.5H60M20 .5V9.5M50 9.5V18" style="stroke:var(--sol-b-l);stroke-width:1"/>
    </pattern>
    <pattern id="pb-sol-h" width="60" height="18" patternUnits="userSpaceOnUse">
      <rect width="60" height="18" style="fill:var(--sol-h)"/>
      <path d="M0 .5H60M0 9.5H60M20 .5V9.5M50 9.5V18" style="stroke:var(--sol-h-l);stroke-width:1"/>
    </pattern>
    <pattern id="pb-mat" width="13" height="13" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="13" height="13" style="fill:var(--mat)"/>
      <path d="M0 0H13M0 0V13" style="stroke:var(--mat-l);stroke-width:1.2"/>
      <circle r="1.3" style="fill:var(--mat-b)"/><circle cx="13" r="1.3" style="fill:var(--mat-b)"/>
      <circle cy="13" r="1.3" style="fill:var(--mat-b)"/><circle cx="13" cy="13" r="1.3" style="fill:var(--mat-b)"/>
    </pattern>
    <pattern id="pb-teck" width="46" height="12" patternUnits="userSpaceOnUse">
      <rect width="46" height="12" style="fill:var(--teck)"/>
      <path d="M2 3.5H20M27 4H42M8 7.5H31M36 8H45M0 10H6M14 10.5H24" style="stroke:var(--teck-l);stroke-width:.7"/>
    </pattern>
  </defs>
"""

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


def bord_babord(n=400):
    """Bord bâbord échantillonné, du tableau arrière à l'étrave."""
    pts = []
    for p0, p1, p2, p3 in ((h[0], h[1], h[2], h[3]), (h[3], h[4], h[5], h[6])):
        for i in range(n):
            t = i / n
            pts.append(tuple((1-t)**3*a + 3*(1-t)**2*t*b_ + 3*(1-t)*t**2*c + t**3*d
                             for a, b_, c, d in zip(p0, p1, p2, p3)))
    return pts + [h[6]]


def dossier(x0, x1, d=60):
    """Trait de dossier bâbord, parallèle au bord à la distance d, de x0 à x1.
    S'arrête sur l'axe s'il l'atteint avant x1 (les deux bords se rejoignent)."""
    bord, out = bord_babord(), []
    for (xa, ya), (xb, yb) in zip(bord, bord[1:]):
        L = ((xb-xa)**2 + (yb-ya)**2) ** .5
        x, y = xa - d*(yb-ya)/L, ya + d*(xb-xa)/L   # normale vers l'intérieur
        if x > x1:
            break
        if y >= CY:
            out.append((out[-1][0] + (CY-out[-1][1]) * (x-out[-1][0]) / (y-out[-1][1]), CY))
            break
        if x0 <= x <= x1:
            out.append((x, y))
    return out


def porte(gond, ferme, ouvert):
    """Vantail (gond → position ouverte) et arc de son ouverture (fermée → ouverte)."""
    r = K * ((ferme[0]-gond[0])**2 + (ferme[1]-gond[1])**2) ** .5
    sens = 1 if ((ferme[0]-gond[0])*(ouvert[1]-gond[1]) - (ferme[1]-gond[1])*(ouvert[0]-gond[0])) > 0 else 0
    return (path("amg", gond, ouvert) +
            f'<path class="amg-l" d="M{P(*ferme)} A{r:.1f} {r:.1f} 0 0 {sens} {P(*ouvert)}"/>')


el = []
A = el.append

A('<!-- Coque et axe du bateau -->')
A(f'<clipPath id="pb-coque"><path d="{coque}"/></clipPath>')
A(f'<path class="hull" d="{coque}"/>')
A('<g clip-path="url(#pb-coque)">')

A('<!-- Vaigrages latéraux, du bord au dossier (carré, cabine de proue) -->')
A(f'<clipPath id="pb-vaig">{rect("", 760, 0, 1090, 700)}{rect("", 1150, 0, 1535, 700)}</clipPath>')
A('<g clip-path="url(#pb-vaig)">')
A(f'<path class="vaig" d="{coque}" stroke-width="{2 * K * 60:.1f}"/>')   # trait centré sur le bord : moitié visible
A('</g>')

A('<!-- Planchers, jusqu’au milieu des assises. Niveau bas : carré, cuisine ; '
  'niveau haut : cabine de poupe, table à carte, cabinet de toilette -->')
A(path("sol-h", (480, 112), (560, 112), (560, 110), (640, 110), (640, 100), (755, 100), (755, 230),
       (640, 230), (640, 265), (430, 265), (430, 165), (480, 165), close=True))
A(path("sol-h", (400, 390), (580, 390), (580, 500), (480, 500), (480, 598), (400, 598), close=True))
db = dossier(760, 1090)
mi = [(x, (y + 226 + (x - 760) * 49 / 330) / 2) for x, y in db]   # milieu entre dossier et bord d'assise
mi = [(760, mi[0][1])] + mi + [(1090, (db[-1][1] + 275) / 2)]
A(path("sol-b", (640, 265), (640, 230), (760, 230), *mi, (1090, 250), (1150, 250), (1150, 395),
       (1090, 395), *[(x, M(y)) for x, y in reversed(mi)], (690, M(mi[0][1])), (690, 485),
       (580, 485), (580, 390), (612, 390), (612, 265), close=True))

A(path("bound", (0, CY), (1700, CY)))

A('<!-- Cockpit : bancs à lattes, coffre tribord, winches, safran -->')
A(rect("amg", 75, 185, 400, 460))
A(rect("teck", 90, 185, 392, 265))         # banc bâbord
A(rect("teck", 90, 390, 392, 460))         # banc tribord
for y0, y1 in ((185, 265), (390, 460)):    # lattes dans la longueur des bancs
    for i in range(1, 5):
        y = y0 + i * (y1 - y0) / 5
        A(path("teck-j", (90, y), (392, y)))
A(rect("amg", 187, 390, 341, 480))         # couvercle du coffre tribord, au-delà du banc
for y in (130, M(130)):                      # winches, symétriques par rapport à l'axe
    A(circle("amg", 360, y, 15))
# safran : axe de rotation à l'arrière, plus large à l'axe que vers l'avant
A(f'<path class="amg" d="M{P(75, CY-10)} L{P(215, CY-3)} Q{P(222, CY)} {P(215, CY+3)} '
  f'L{P(75, CY+10)} A{K*10:.1f} {K*10:.1f} 0 0 1 {P(75, CY-10)} Z"/>')
A(circle("amg", 75, CY, 4))                  # mèche
A(path("bound", (175, 190), (430, 125), (430, 280), (175, 345), close=True))  # couchette sous cockpit

A('<!-- Accès à la cabine de poupe : passage, placard, porte -->')
A(path("amg", (560, 255), (560, 265), (430, 265), (430, 52)))
A(path("amg", (560, 172), (560, 47)))
A(path("amg", (480, 52), (480, 165)))
A(path("amg", (480, 112), (560, 112)))       # placard
A(porte((560, 172), (560, 255), (631.9, 213.5)))

A('<!-- Table à carte et son siège -->')
A(rect("mat", 575, 70, 635, 150))            # siège
A(rect("amg-b", 640, 100, 755, 230))           # table à carte, écartée du bord
A(path("amg", (755, 50), (755, 230)))

A('<!-- Descente et sa partie amovible (accès au moteur) -->')
A(rect("amg", 470, 265, 545, 390))
for x in (495, 520):
    A(path("amg-l", (x, 265), (x, 390)))
A(rect("amg", 548, 285, 612, 372))
A(path("amg-l", (580, 285), (580, 372)))     # marche de la partie amovible

A('<!-- Cabinet de toilette (tribord) -->')
A(path("amg", (400, 598), (400, 390), (580, 390)))
A(path("amg", (580, 472), (580, 598)))
A(path("amg", (480, 500), (580, 500)))
A(path("amg", (480, 500), (480, 598)))
A(circle("amg-b", 445, 445, 26))               # WC
A(circle("amg-b", 455, 412, 8))                # pompe
A(ellipse("amg", 530, 545, 38, 26))          # lavabo
A(rect("amg-b", 405, 545, 475, 590))           # caillebotis
for x in range(412, 475, 9):
    A(path("amg-l", (x, 548), (x, 587)))
A(porte((580, 472), (580, 390), (652, 430)))

A('<!-- Cuisine (tribord) -->')
A(rect("amg-b", 585, 485, 665, 548))           # réchaud deux feux
A(rect("amg", 595, 495, 622, 538))
A(rect("amg", 628, 495, 655, 538))
A(rect("amg-b", 675, 505, 752, 582))           # glacière
A(rect("amg-b", 690, 345, 755, 475))           # bloc évier
A(rect("amg", 698, 352, 748, 405, rx=6))
A(rect("amg", 698, 415, 748, 468, rx=6))
A(rect("amg-b", 665, 318, 775, 338))           # plan de travail
A(path("amg", (760, 340), (760, 598)))

A('<!-- Carré : banquettes (le trait côté bord est le dossier), table repliée, pied de mât -->')
A(path("mat", *db, (1090, 275), (760, 226), close=True))
A(path("mat", *[(x, M(y)) for x, y in db], (1090, M(275)), (760, M(226)), close=True))
A(rect("amg-f", 825, CY-25, 985, CY+25))     # table repliée, sur l'axe
A(circle("amg", 965, CY, 11))                # pied de mât, dans la table, à son bout avant

A('<!-- Cloison avant du carré, penderies, porte de la cabine de proue -->')
A(path("amg", (1090, 40), (1090, 277)))
A(path("amg", (1090, 357), (1090, 604)))
A(path("amg", (1150, 40), (1150, 250), (1090, 250)))
A(path("amg", (1150, 604), (1150, 395), (1090, 395)))
A(porte((1090, 357), (1090, 277), (1146.6, 300.4)))

A('<!-- Cabine de proue : couchette en V entre les dossiers, qui se rejoignent derrière le puits à chaîne -->')
dp = dossier(1150, 1700)
A(path("mat", (1150, dp[0][1]), *dp, *[(x, M(y)) for x, y in reversed(dp[:-1])],
       (1150, M(dp[0][1])), close=True))
A(path("amg", (1150, 287), (1210, 302), (1210, 342), (1150, 357), close=True))  # trapèze, sur le bord de la couchette
A(path("amg", (1535, 150), (1535, 494)))     # cloison du puits à chaîne

A('</g>')
# repères d'orientation et zones (provisoires)
LBL = [
    ("Cockpit", 300, 350),
    ("Cabine de poupe (sous le cockpit)", 300, 300),
    ("Table à carte", 698, 170),
    ("Descente", 512, 328, -90),
    ("Toilette", 520, 480),
    ("Cuisine", 640, 478),
    ("Carré", 1040, 348),
    ("Cabine de proue", 1330, 300),
]
el.append('<!-- Noms de zones (provisoires) -->')
for s, x, y, *r in LBL:
    el.append(text("ts mid halo", x, y, s, *r))
el.append(text("pin mid halo", 520, 87, "placard"))
el.append(text("pin mid halo", 600, 328, "amovible", -90))
el.append(text("pin mid halo", 264, 430, "coffre"))
el.append(text("pin mid halo", 890, 328, "table repliée"))
el.append(text("pin mid halo", 965, 292, "pied de mât"))
el.append(text("pin mid halo", 1580, 410, "puits à chaîne"))
el.append(path("leader", (1580, 395), (1580, 340)))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" role="img" aria-label="Plan de bord vu de dessus : aménagement intérieur et pont du Gib'Sea 31, fond de plan vierge.">
  <title>Folio 6 · Plan de bord</title>
  <desc>Vue de dessus, avant à droite, bâbord en haut, redessinée d'après le plan d'emménagement du constructeur. Fond de plan vierge : les objets du bord (sécurité, armement) y seront placés avec leurs légendes.</desc>
{STYLE}{DEFS}  <rect class="bg" x="0" y="0" width="100%" height="100%"/>
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
