"""Brouillon du folio « plan de bord » (phase 1 : fond de plan vide).

Coordonnées relevées sur le plan d'emménagement du constructeur (agrandi ×3),
puis converties en coordonnées SVG par P(). Avant à droite, bâbord en haut.
"""
import re
from pathlib import Path

import yaml

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
    .vaig{fill:none;stroke:var(--vaig)}.vaig-f{fill:var(--vaig)}
    .amg-d{fill:none;stroke:var(--muted);stroke-width:1;stroke-dasharray:4 3}
    .amg-p{fill:none;stroke:var(--ink);stroke-width:1.1;stroke-dasharray:2 2.5}
    svg{--ts:#36404b}@media (prefers-color-scheme: dark){svg{--ts:#bcc7d2}}.ts{fill:var(--ts)}
    .axe{fill:none;stroke:var(--muted);stroke-width:.6;stroke-dasharray:18 3 2 3}
    .flot{fill:none;stroke:var(--ink);stroke-width:1.6;stroke-dasharray:18 3 2 3}
    .arr{fill:none;stroke:var(--ink);stroke-width:1.2;stroke-linejoin:round}
    svg{--c-securite:#c8231c;--c-gaz:#d97706;--c-fluides:#0f7f86;--c-moteur:#4b5563;--c-electricite:#7b3fb0;--c-rangement:#8a5a2b}
    @media (prefers-color-scheme: dark){svg{--c-securite:#e5483f;--c-gaz:#f59e0b;--c-fluides:#22a6ad;--c-moteur:#7b8794;--c-electricite:#a46be0;--c-rangement:#b07a45}}
    .obj circle{stroke:var(--sheet);stroke-width:1.2}
    .obj text{fill:#fff;font-family:"IBM Plex Mono",Consolas,monospace;font-size:8.5px;font-weight:600;text-anchor:middle}
    .obj .tr{stroke:var(--sheet);stroke-width:1.2}.leg{font-size:10.5px}
    .ico-mot *{fill:none;stroke:var(--c-moteur);stroke-width:1.3;stroke-linejoin:round;stroke-linecap:round}.ico-mot .f{fill:var(--sheet)}
    .obj .conf{fill:none;stroke:var(--ink);stroke-width:1;stroke-dasharray:2.5 2}
    .securite circle{fill:var(--c-securite)}.gaz circle{fill:var(--c-gaz)}.fluides circle{fill:var(--c-fluides)}
    .moteur circle,.moteur .tr{fill:var(--c-moteur)}.electricite circle{fill:var(--c-electricite)}.rangement circle{fill:var(--c-rangement)}
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


def arc_pts(p0, p1, fleche, n=40):
    """Arc de cercle de p0 à p1, de flèche donnée (positive : bombé à gauche de p0→p1)."""
    import math
    (x0, y0), (x1, y1) = p0, p1
    c = math.hypot(x1-x0, y1-y0)
    R = (c*c/4 + fleche*fleche) / (2*fleche)
    nx, ny = (y1-y0)/c, -(x1-x0)/c                 # normale à gauche
    mx, my = (x0+x1)/2, (y0+y1)/2
    cx, cy = mx - nx*(R-fleche), my - ny*(R-fleche)
    a0, a1 = math.atan2(y0-cy, x0-cx), math.atan2(y1-cy, x1-cx)
    a1 = a0 + (a1 - a0 + math.pi) % (2*math.pi) - math.pi   # petit arc
    return [(cx + R*math.cos(a0 + (a1-a0)*i/n), cy + R*math.sin(a0 + (a1-a0)*i/n)) for i in range(n+1)]


def main_levee(pts, pas=10, amp=1.8):
    """Trait ouvert à main levée passant près des points : légère ondulation, courbes lissées."""
    import math
    ech = []
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        L = math.hypot(xb-xa, yb-ya)
        for i in range(max(1, round(L/pas))):
            t = i / max(1, round(L/pas))
            ech.append((xa + (xb-xa)*t, ya + (yb-ya)*t, (yb-ya)/L, -(xb-xa)/L))
    q = [(x + nx*amp*math.sin(k*1.7)*math.cos(k*.45), y + ny*amp*math.sin(k*1.7)*math.cos(k*.45))
         for k, (x, y, nx, ny) in enumerate(ech)] + [pts[-1]]
    q[0] = pts[0]
    n, d = len(q), f"M{P(*q[0])}"
    for i in range(n - 1):                          # Catmull-Rom → Bézier
        p0, p1, p2, p3 = q[max(i-1, 0)], q[i], q[i+1], q[min(i+2, n-1)]
        c1 = (p1[0] + (p2[0]-p0[0])/6, p1[1] + (p2[1]-p0[1])/6)
        c2 = (p2[0] - (p3[0]-p1[0])/6, p2[1] - (p3[1]-p1[1])/6)
        d += f" C{P(*c1)}, {P(*c2)}, {P(*p2)}"
    return d


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
A(f'<clipPath id="pb-vaig">{rect("", 760, 0, 1090, 700)}{rect("", 1090, CY, 1150, 700)}{rect("", 1150, 0, 1535, 700)}</clipPath>')
A('<g clip-path="url(#pb-vaig)">')
A(f'<path class="vaig" d="{coque}" stroke-width="{2 * K * 60:.1f}"/>')   # trait centré sur le bord : moitié visible
A('</g>')

A('<!-- Planchers, jusqu’au milieu des assises. Niveau bas : carré, cuisine ; '
  'niveau haut : cabine de poupe, table à carte, cabinet de toilette -->')
A(path("sol-h", (480, 165), (560, 165), (560, 100), (760, 100), (760, 230),
       (640, 230), (640, 265), (480, 265), close=True))
A(path("sol-h", (400, 390), (580, 390), (580, 500), (480, 500), (480, 598), (400, 598), close=True))
db = dossier(760, 1090)
# bord des assises du carré et côtés du trapèze de la cabine de proue sur une même droite,
# de l'arrière des banquettes (760, 226) au sommet du trapèze (1210, 302)
def y_assise(x):
    return 226 + (x - 760) * 76 / 450


YA, YT = y_assise(1090), y_assise(1150)   # à la cloison du carré, à la base du trapèze
mi = [(x, (y + y_assise(x)) / 2) for x, y in db]   # milieu entre dossier et bord d'assise
mi = [(760, mi[0][1])] + mi + [(1090, (db[-1][1] + YA) / 2)]
A(path("sol-b", (640, 265), (640, 230), (760, 230), *mi, (1090, 250), (1150, 250), (1150, M(YT)),
       (1090, M(YA)), *[(x, M(y)) for x, y in reversed(mi)], (690, M(mi[0][1])), (690, 485),
       (580, 485), (580, 390), (545, 390), (545, 265), close=True))   # de part et d'autre de la partie amovible

# axe du navire en trait mixte fin (ISO 128), interrompu dans le coffre triangulaire de la cabine de proue,
# séparé en deux le long de l'axe (arête cachée, prioritaire sur l'axe)
XT, XV = 1210, dossier(1150, 1700)[-1][0]    # sommet du trapèze, pointe du V des dossiers
A(path("axe", (0, CY), (XT, CY)))
A(path("axe", (XV, CY), (1700, CY)))

A('<!-- Cockpit : bancs à lattes, coffre tribord, winches, safran -->')
A(rect("amg", 75, 185, 400, 460))
A(rect("teck", 90, 185, 392, 265))         # banc bâbord
A(rect("teck", 90, 390, 392, 460))         # banc tribord
for y0, y1 in ((185, 265), (390, 460)):    # lattes dans la longueur des bancs
    for i in range(1, 5):
        y = y0 + i * (y1 - y0) / 5
        A(path("teck-j", (90, y), (392, y)))
A(rect("amg", 187, 390, 341, 480))         # couvercle du coffre tribord, au-delà du banc
A(path("amg-d", (100, 390), (100, 700)))     # coffre : du bord à la cloison du cabinet de toilette, presque jusqu'à la poupe
for y in (130, M(130)):                      # winches, symétriques par rapport à l'axe
    A(circle("amg", 360, y, 15))
# safran : axe de rotation à l'arrière, plus large à l'axe que vers l'avant
A(f'<path class="amg" d="M{P(75, CY-10)} L{P(215, CY-3)} Q{P(222, CY)} {P(215, CY+3)} '
  f'L{P(75, CY+10)} A{K*10:.1f} {K*10:.1f} 0 0 1 {P(75, CY-10)} Z"/>')
A(circle("amg", 75, CY, 4))                  # mèche
# couchette de la cabine de poupe : bord bâbord en arc jusqu'au placard, vaigrage entre le matelas et le bord
bord_lit = arc_pts((175, 190), (480, 95), 22)
YC = 260                                     # coin avant tribord, en retrait de la descente (y = 265)
lit = [*bord_lit, (480, YC), (175, YC + 80)]
A(path("bound", *lit, close=True))           # couchette, sous le cockpit

A('<!-- Arrachement du cockpit (trait à main levée, fermé par le bord du pont) : couchette de la '
  'cabine de poupe, côté bâbord jusqu’à l’axe, sans toucher la barre -->')
arr = [(430, 79), (400, 82), (320, 93), (230, 112), (160, 150), (162, 200), (158, 250), (163, 303),
       (200, 307), (236, 306), (250, 318), (290, 319), (330, 314), (390, 300), (430, 290)]
d_arr = main_levee(arr)
A(f'<clipPath id="pb-dessous"><path d="{d_arr} Z"/>{rect("", 430, 0, 481, 290)}</clipPath>')
A('<g clip-path="url(#pb-dessous)">')
A(rect("bg", 0, 0, 480, 400))            # le banc du cockpit s'arrête à la ligne de coupe
A(path("vaig-f", *bord_lit, (480, 0), (175, 0), close=True))
A(path("mat", *lit, close=True))
A(path("amg", (175, 0), (175, 200)))         # cloison arrière de la cabine, à travers le vaigrage
# pièce amovible (accès batterie) : deux côtés forment le coin avant tribord de la couchette,
# un sommet à l'angle du meuble du lavabo, un autre au niveau de la paroi arrière du cabinet de toilette
la, lc = (480, 165), (480, YC)
ld = (400, YC + 80 * 80 / 305)               # sur le bord tribord de la couchette
lb = (la[0] + ld[0] - lc[0], la[1] + ld[1] - lc[1])   # côtés opposés parallèles
A(path("amg", la, lc, ld, lb, close=True))
# coffres sous la couchette : côtés de la pièce amovible prolongés vers la poupe et vers bâbord
A(path("amg-d", lb, (175, la[1] + (175 - la[0]) * (lb[1] - la[1]) / (lb[0] - la[0]))))
A(path("amg-d", lb, (lb[0], next(ya + (yb-ya) * (lb[0]-xa) / (xb-xa)
                                  for (xa, ya), (xb, yb) in zip(bord_lit, bord_lit[1:]) if xa <= lb[0] <= xb))))
A('</g>')
A(f'<path class="arr" d="{d_arr}"/>')
A(path("amg", (430, 40), (430, 79)))         # bord du pont, au-dessus de la cabine
A(path("amg-p", (430, 290), (470, 290)))    # cloison du cockpit, de la ligne de coupe à la descente

A('<!-- Cabine de poupe : meuble bas du lavabo déposé, placard, porte -->')
A(rect("amg-b", 480, 112, 560, 165))         # meuble bas
A(ellipse("amg-d", 520, 138, 28, 16))        # emplacement du lavabo déposé
A(path("amg", (560, 255), (560, 265), (480, 265)))
A(path("amg", (560, 172), (560, 47)))
A(path("amg", (480, 52), (480, 165)))
A(path("amg", (480, 112), (560, 112)))       # placard
A(porte((560, 255), (560, 172), (488.1, 213.5)))   # s'ouvre vers la cabine

A('<!-- Table à carte et son siège ; contre le bord, le tableau de servitude -->')
A(rect("mat", 560, 100, 620, 180))           # siège, contre la paroi de la cabine de poupe
A(path("amg", (560, 100), (760, 100)))       # séparation du tableau de servitude
A(rect("amg-b", 640, 100, 760, 230))           # table à carte, écartée du bord, contre la cloison du carré
A(rect("amg-d", 700, 180, 760, 230))         # équipet sous la table, contre la banquette, ouvert côté puits de dérive
A(path("amg", (760, 50), (760, 230)))        # cloison alignée sur celle de la cuisine

A('<!-- Descente et sa partie amovible (accès au moteur) -->')
A(rect("amg", 470, 265, 545, 390))
for x in (495, 520):
    A(path("amg-l", (x, 265), (x, 390)))
A(rect("amg-b", 548, 285, 596, 372))         # partie amovible, marches peu profondes, plancher de part et d'autre
A(path("amg-l", (572, 285), (572, 372)))     # marche de la partie amovible

A('<!-- Cabinet de toilette (tribord) -->')
A(path("amg", (400, 598), (400, 390), (580, 390)))
A(path("amg", (580, 472), (580, 598)))
A(path("amg", (480, 500), (580, 500)))
A(path("amg", (480, 500), (480, 598)))
A(circle("amg-b", 445, 445, 26))               # WC (légende avec les noms de zones)
A(circle("amg-b", 455, 412, 8))                # pompe
A(ellipse("amg", 530, 545, 38, 26))          # lavabo
A(rect("amg-b", 405, 545, 475, 590))           # caillebotis
for x in range(412, 475, 9):
    A(path("amg-l", (x, 548), (x, 587)))
A(porte((580, 390), (580, 472), (509, 431)))   # s'ouvre vers le cabinet

A('<!-- Cuisine (tribord) -->')
A(rect("amg-b", 585, 485, 665, 548))           # réchaud deux feux
A(rect("amg", 595, 495, 622, 538))
A(rect("amg", 628, 495, 655, 538))
A(rect("amg-b", 675, 505, 752, 582))           # glacière
A(rect("amg-b", 690, 345, 760, 475))           # bloc évier, contre la cloison du carré
A(rect("amg", 698, 352, 748, 405, rx=6))
A(rect("amg", 698, 415, 748, 468, rx=6))
A(rect("amg-b", 665, 318, 775, 338))           # plan de travail
A(path("amg", (760, 340), (760, 598)))

A('<!-- Carré : banquettes (le trait côté bord est le dossier), table repliée, pied de mât -->')
A(path("mat", *db, (1090, YA), (760, 226), close=True))
A(path("mat", *[(x, M(y)) for x, y in db], (1090, M(YA)), (760, M(226)), close=True))
for XC in (870, 980):                        # coffres sous les banquettes : trois parties
    yd = next(y for x, y in db if x >= XC)
    for f in (lambda y: y, M):
        A(path("amg-d", (XC, f(yd)), (XC, f(y_assise(XC)))))
A(rect("amg-f", 825, CY-25, 985, CY+25))     # table repliée, sur l'axe
A(circle("amg", 965, CY, 11))                # pied de mât, dans la table, à son bout avant

A('<!-- Cloison avant du carré, penderie bâbord, porte de la cabine de proue -->')
A(path("amg", (1090, 40), (1090, 282)))
A(path("amg", (1090, 357), (1090, 604)))
A(path("amg", (1150, 40), (1150, 250), (1090, 250)))
A(porte((1090, 357), (1090, 282), (1143, 304)))   # gonds côté tribord

A('<!-- Cabine de proue : couchette en V entre les dossiers, qui se rejoignent derrière le puits à chaîne ; '
  'à tribord, elle se prolonge jusqu’au carré -->')
dp = dossier(1150, 1700)
dpt = dossier(1090, 1700)
A(path("mat", (1150, dp[0][1]), *dp, *[(x, M(y)) for x, y in reversed(dpt[:-1])],
       (1090, M(dpt[0][1])), (1090, M(YA)), (1150, M(YT)), close=True))   # côté tribord du trapèze prolongé jusqu'au carré
A(path("amg", (1150, YT), (1210, 302), (1210, 342), (1150, M(YT)), close=True))  # trapèze, sur le bord de la couchette
A(path("axe", (1150, CY), (XT, CY)))            # l'axe traverse le trapèze, par-dessus le matelas


def y_dossier(x):
    """Ordonnée du dossier bâbord à l'abscisse x (interpolée)."""
    q = dossier(760, 1700)
    return next(ya + (yb-ya) * (x-xa) / (xb-xa) for (xa, ya), (xb, yb) in zip(q, q[1:]) if xa <= x <= xb)


# coffres sous la couchette : base du trapèze prolongée jusqu'au dossier tribord, sommet jusqu'aux
# deux dossiers ; le coffre triangulaire à l'avant est séparé en deux le long de l'axe
A(path("amg-d", (1150, M(YT)), (1150, M(y_dossier(1150)))))
A(path("amg-d", (XT, y_dossier(XT)), (XT, 302)))
A(path("amg-d", (XT, 342), (XT, M(y_dossier(XT)))))
A(path("amg-d", (XT, CY), (XV, CY)))
A(path("amg", (1535, 150), (1535, 494)))     # cloison du puits à chaîne

A('</g>')
# repères d'orientation et zones (provisoires)
LBL = [
    ("Cockpit", 300, 350),
    ("Cabine de poupe", 310, 220),
    ("Table à carte", 698, 170),
    ("Descente", 483, 328, -90),
    ("Toilette", 520, 480),
    ("Cuisine", 640, 478),
    ("Carré", 1040, 348),
    ("Cabine de proue", 1330, 300),
]
el.append('<!-- Noms de zones (provisoires) -->')
for s, x, y, *r in LBL:
    el.append(text("ts mid halo", x, y, s, *r))
el.append(text("ts mid", 445, 449, "WC"))
el.append(text("ts mid", 713.5, 547, "glacière"))
el.append(text("ts mid halo", 520, 87, "placard"))
el.append(text("ts mid halo", 520, 141, "lavabo"))
el.append(text("ts mid halo", (la[0]+lb[0]+lc[0]+ld[0])/4, (la[1]+lb[1]+lc[1]+ld[1])/4 + 3, "batterie"))
el.append(text("ts mid halo", 658, 84, "tableau de servitude"))
el.append(text("ts mid halo", 264, 430, "coffre"))
el.append(text("ts mid halo", 589, 328, "amovible", -90))
el.append(text("ts mid", 1125, 185, "placard", -90))
el.append(text("ts mid halo", 890, 328, "table repliée"))
el.append(text("ts mid halo", 965, 292, "pied de mât"))
el.append(text("ts mid halo", 1580, 410, "puits à chaîne"))
el.append(path("leader", (1580, 395), (1580, 340)))

# --- Objets du bord (phase 2) : pastilles numérotées et légendes ---
DONNEES = yaml.safe_load((ICI / "objets.yaml").read_text(encoding="utf-8"))
OBJ, BATEAU = DONNEES["objets"], DONNEES["bateau"]
CAT = [("securite", "sécurité"), ("gaz", "gaz"), ("fluides", "gazole et eau"), ("moteur", "moteur"),
       ("electricite", "électricité"), ("rangement", "rangement")]


def pastille(o, X, Y):
    conf = '<circle class="conf" r="10"/>' if o.get("a_confirmer") else ""
    return (f'<g class="obj {o["categorie"]}" transform="translate({X:.1f} {Y:.1f})">{conf}'
            f'<circle r="7.5"/><text y="3">{o["n"]}</text></g>')


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def trappe(o, X, Y):
    return (f'<g class="obj {o["categorie"]}" transform="translate({X:.1f} {Y:.1f})">'
            f'<rect class="tr" x="-7.5" y="-6.5" width="15" height="13" rx="2"/><text y="3">{o["n"]}</text></g>')


def icone_moteur(X, Y):
    """Pictogramme du moteur : bloc, bouchon de remplissage, courroie sur trois poulies, arbre et volant."""
    import math
    r = lambda x0, y0, w, h, rx=0, c="": (f'<rect{c} x="{X + x0:.1f}" y="{Y + y0:.1f}" width="{w}" height="{h}"'
                                          + (f' rx="{rx}"' if rx else "") + "/>")
    c = lambda x, y, rr: f'<circle cx="{X + x:.1f}" cy="{Y + y:.1f}" r="{rr}"/>'
    l = lambda x0, y0, x1, y1: f'<path d="M{X + x0:.1f} {Y + y0:.1f} L{X + x1:.1f} {Y + y1:.1f}"/>'
    poulies, R = [(-4.5, -2.5), (3.5, -1.5), (-0.5, 5.5)], 3.3
    d = ""                                  # courroie : enveloppe des poulies (côtés décalés, arcs autour)
    for i, (ax, ay) in enumerate(poulies):
        bx, by = poulies[(i + 1) % 3]
        n = math.hypot(bx - ax, by - ay)
        nx, ny = (by - ay) / n, -(bx - ax) / n          # normale extérieure (sommets dans le sens horaire)
        p0, p1 = (ax + R * nx, ay + R * ny), (bx + R * nx, by + R * ny)
        d += (f"M{X + p0[0]:.2f} {Y + p0[1]:.2f}" if not d else f" A{R} {R} 0 0 1 {X + p0[0]:.2f} {Y + p0[1]:.2f}")
        d += f" L{X + p1[0]:.2f} {Y + p1[1]:.2f}"
    d += f" A{R} {R} 0 0 1 {d[1:].split()[0]} {d.split()[1]} Z"
    return ('<g class="ico-mot">'
            + r(-6, -13.5, 11, 3.5, 1.5, ' class="f"') + l(-0.5, -10, -0.5, -7.5)        # bouchon et sa tige
            + r(-10, -7.5, 18, 18, 2.5, ' class="f"')                                     # bloc
            + l(-14, 0, -10, 0) + l(-14, -3.5, -14, 3.5)                                  # arbre côté gauche
            + l(8, 4, 11, 4) + r(11, 0, 3, 8, 1.2, ' class="f"')                          # volant côté droit
            + f'<path d="{d}"/>' + "".join(c(x, y, 1.9) for x, y in poulies)
            + l(-8, 7, -6, 9) + '</g>')


el.append('<!-- Objets du bord : pastilles (tirets : à confirmer), trappes d’accès, icône du moteur -->')
el.append(icone_moteur(OX + K * 445, OY + K * 312))   # au niveau des WC, près de l'axe, entre la cloison du cockpit et les repères
for o in OBJ:
    for x, y in o["positions"]:
        el.append(pastille(o, OX + K * x, OY + K * y))
    for x, y in o.get("trappes", []):
        el.append(trappe(o, OX + K * x, OY + K * y))
leg = []
for cote, y0, ymax, objs in (("bâbord", 50, 160, [o for o in OBJ if o["positions"][0][1] < CY]),
                             ("tribord", 730, 880, [o for o in OBJ if o["positions"][0][1] >= CY])):
    rangs = (len(objs) + 1) // 2
    pas = min(13.5, (ymax - y0) / max(rangs - 1, 1))   # interligne resserré si le cadre est plein
    for i, o in enumerate(objs):
        X, Y = (40 if i < rangs else 710), y0 + pas * (i % rangs)
        txt = f'<tspan font-weight="600">{esc(o["nom"])}</tspan> : {esc(o["emplacement"])}'
        if o.get("question"):
            txt += f' <tspan class="tu">({o["question"]})</tspan>'
        leg.append(pastille(o, X, Y - 4) + f'<text class="t leg" x="{X + 14}" y="{Y}">{txt}</text>')
x = 40
leg.append('<text class="ts" x="1376" y="896" text-anchor="end">pastille cerclée de tirets : à confirmer · (PBn) : question</text>')
for c, nom in CAT:
    leg.append(pastille({"categorie": c, "n": ""}, x, 892) + f'<text class="ts" x="{x + 12}" y="896">{nom}</text>')
    x += 28 + 5.6 * len(nom)
leg.append(trappe({"categorie": "moteur", "n": ""}, x, 892) + f'<text class="ts" x="{x + 12}" y="896">trappe d’accès</text>')

# nom du bateau en Arial, aussi en attribut pour les visionneuses qui ignorent le bloc <style>
SANS = 'font-family="Arial, Helvetica, sans-serif"'


def m(v, u="m"):
    return f"{v:.2f}".replace(".", ",") + f" {u}"
B = BATEAU
lignes = [("Longueur hors tout", m(B["longueur_hors_tout_m"])), ("Longueur à la flottaison", m(B["longueur_flottaison_m"])),
          ("Largeur", m(B["largeur_m"])), ("Tirant d’eau (dérive basse)", m(B["tirant_eau_m"])),
          ("Déplacement (lège)", f"≈ {B['deplacement_kg']:,} kg".replace(",", " ")),
          ("Tirant d’air (girouette)", m(B["tirant_air_m"]) + (" ?" if B.get("tirant_air_a_confirmer") else "")
           if B.get("tirant_air_m") else None)]
cx, cy = 1135, 520
cart = [f'<rect class="callout" x="{cx}" y="{cy}" width="240" height="{34 + 17 * len(lignes) + 16}" rx="2"/>',
        f'<text class="tb" x="{cx + 12}" y="{cy + 20}"><tspan {SANS}>{B["nom"].upper()}</tspan> · {B["modele"]} de {B["annee"]}</text>']
for i, (lib, val) in enumerate(lignes):
    y = cy + 40 + 17 * i
    cart.append(f'<text class="t" x="{cx + 12}" y="{y}">{lib}</text>')
    cart.append(f'<text class="t end{" tu" if val.endswith("?") else ""}" x="{cx + 228}" y="{y}">{val}</text>' if val else
                f'<text class="t tu end" x="{cx + 228}" y="{y}">? ({B["question_tirant_air"]})</text>')
if B.get("statut") == "estime":
    cart.append(f'<text class="ts" x="{cx + 12}" y="{cy + 40 + 17 * len(lignes) + 2}">d’après des fiches en ligne, à vérifier</text>')

# Profil tribord miniature (avant à droite), redessiné d'après le plan de voilure du constructeur
# (profil-constructeur.jpeg, points relevés en pixels de l'image) : mis à l'échelle sur la longueur hors tout
# (horizontalement) et sur le tirant d'air (verticalement) ; sans tirant d'air, haut du mât en tirets (PB12).
L, T, TA = B["longueur_hors_tout_m"], B["tirant_eau_m"], B.get("tirant_air_m")
IX0, IX1, IWL, ITOP = 80, 430, 533.3, 38     # image : arrière, étrave, flottaison, tête de mât (girouette)
KP, PX, PW = 12, 1185, 332                         # px par mètre, x de l'arrière, y de la flottaison
SX, SZ = L / (IX1 - IX0), (TA or 12.5) / (IWL - ITOP)
def pi(X, Y):                                      # point de l'image → point du folio
    return f"{PX + KP * SX * (X - IX0):.1f} {PW - KP * SZ * (IWL - Y):.1f}"
def ipath(cls, *pts, close=True):
    return f'<path class="{cls}" d="M' + " L".join(pi(*q) for q in pts) + (' Z"' if close else '"') + "/>"
COQUE = [(89.3, 499.3), (430, 493.7), (400, 530), (390, 540), (350, 547.5), (310, 551.3), (300, 552.5),
         (198.6, 551.4), (150, 547), (118.6, 543),                         # œuvres vives, jusqu'au skeg
         (113, 545), (110, 550), (107, 568.6), (105.7, 571.4), (100, 571.5),  # skeg devant le safran
         (100, 530), (80, 527.1)]                                          # tableau arrière incliné
BORDE = [(95.7, 508), (250, 506), (380, 503), (424.8, 500), (400, 530), (250, 531), (120, 530),
         (82.9, 528.6), (91.4, 520)]                                       # bordé foncé, entre le liston et la flottaison
ROOF = [(177, 496), (179, 481.5), (287, 481), (296, 493)]                 # rouf, son avant en pente
HUBLOTS = [(185, 212), (227, 280)]                                        # vitrages du rouf
LEST = [(207.5, 551.3), (207.5, 575.5), (270, 573.7), (305, 552.5)]        # aileron de quille
DERIVE = [(220, 575.5), (241.7, 606.7), (270, 573.7)]                     # dérive basse
SAFRAN = [(80, 527.1), (100, 530), (100, 571.5), (82, 569)]
GV = [(276.7, 44.7), (283.3, 440), (154.7, 444.7)]                        # grand-voile : tête, point d'amure, point d'écoute
GENOIS = [(288, 86.7), (427, 491), (208, 478)]                            # génois : point d'écoute en arrière du mât


def coutures(depart, fin, bords, pas, debut=None):
    """Coutures perpendiculaires au bord `depart` → `fin`, tous les `pas` à partir de `debut` (défaut : un pas),
    tracées vers l'intérieur de la voile jusqu'au premier des segments `bords` rencontré."""
    (hx, hy), (ex, ey) = depart, fin
    lx, ly = ex - hx, ey - hy
    n = (lx * lx + ly * ly) ** .5
    ux, uy = lx / n, ly / n
    px, py = -uy, ux
    cx = sum(q[0] for b in bords for q in b) / (2 * len(bords))
    cy = sum(q[1] for b in bords for q in b) / (2 * len(bords))
    if px * (cx - hx) + py * (cy - hy) < 0:            # vers l'intérieur de la voile
        px, py = -px, -py
    traits, d = [], debut or pas
    while d < n - 1:
        ax, ay = hx + ux * d, hy + uy * d
        best = None
        for (bx, by), (b2x, b2y) in bords:             # a + s·p = b + r·(b2 - b), 0 ≤ r ≤ 1, s > 0
            gx, gy = b2x - bx, b2y - by
            det = px * -gy + gx * py
            if abs(det) < 1e-9:
                continue
            s_ = ((bx - ax) * -gy + gx * (by - ay)) / det
            r = (px * (by - ay) - py * (bx - ax)) / det
            if s_ > 1e-6 and -1e-6 <= r <= 1 + 1e-6 and (best is None or s_ < best):
                best = s_
        if best:
            traits.append(f'M{pi(ax, ay)} L{pi(ax + px * best, ay + py * best)}')
        d += pas
    return f'<path class="amg-l" style="stroke-width:.45" d="{" ".join(traits)}"/>'


# génois coupé à onglet, comme sur le plan de voilure : couture d'onglet du guindant au point d'écoute ;
# au-dessus, laizes perpendiculaires à la chute ; au-dessous, perpendiculaires à la bordure
(GT, GA, GE), ONGLET = GENOIS, (378.5, 350)
COUT_GENOIS = (coutures(GT, GE, [(GT, ONGLET), (ONGLET, GE)], 30)
               + coutures(GA, GE, [(ONGLET, GE), (GA, ONGLET)], 29, debut=22)
               + f'<path class="amg-l" style="stroke-width:.45" d="M{pi(*ONGLET)} L{pi(*GE)}"/>')


xd = PX + KP * SX * (241.7 - IX0)
prof = ['<g class="profil">',
        ipath("amg-f", *GENOIS), COUT_GENOIS,   # le génois passe derrière la grand-voile
        ipath("amg-f", *GV), coutures(GV[0], GV[2], [(GV[0], GV[1]), (GV[1], GV[2])], 30),
        f'<path class="amg-l" d="M{pi(276.7, 38)} L{pi(89.3, 499.3)}"/>',      # pataras
        ipath("amg-b", *COQUE), ipath("amg-f", *BORDE), ipath("amg-b", *ROOF),
        *[f'<path class="amg-l" d="M{pi(a, 490)} L{pi(b, 490)}"/>' for a, b in HUBLOTS],
        f'<text class="tb" {SANS} style="font-family:Arial,Helvetica,sans-serif;font-size:6.5px;font-weight:700" x="{pi(112, 525).split()[0]}" y="{pi(112, 525).split()[1]}">{B["nom"].upper()}</text>',
        ipath("dn", *LEST), ipath("amg-b", *DERIVE), ipath("dn", *SAFRAN),
        f'<path class="n w2" d="M{pi(285.3, 490)} L{pi(276.7, 38)}"/>',       # mât
        f'<path class="flot" d="M{PX - 12} {PW} H{PX + KP * L + 14}"/>',       # flottaison, trait mixte fort
        f'<text class="ts end" x="{PX - 16}" y="{PW + 3}">flottaison</text>',
        f'<text class="ts" x="{xd + 12:.0f}" y="{PW + KP * SZ * (606.7 - IWL):.0f}">{m(T)}</text>',
        f'<text class="ts mid" x="{PX + KP * L / 2:.0f}" y="{PW + KP * SZ * (606.7 - IWL) + 16:.0f}">profil tribord · {m(L)}</text>']
HM = SZ * (IWL - ITOP)
if TA:   # cote du tirant d'air, à droite de l'étrave
    xc, conf = PX + KP * (L + 0.9), B.get("tirant_air_a_confirmer")
    prof += [f'<path class="amg-l" d="M{pi(281, 38)} H{xc + 4}"/>',
             f'<path class="arr" d="M{xc} {PW} V{PW - KP * HM:.1f} M{xc - 3} {PW - KP * HM + 6:.1f} L{xc} {PW - KP * HM:.1f} L{xc + 3} {PW - KP * HM + 6:.1f}'
             f' M{xc - 3} {PW - 6} L{xc} {PW} L{xc + 3} {PW - 6}"/>',
             f'<text class="ts{" tu" if conf else ""}" x="{xc + 5:.0f}" y="{PW - KP * HM / 2:.0f}">{m(TA)}{" ?" if conf else ""}</text>',
             f'<text class="ts" x="{xc + 5:.0f}" y="{PW - KP * HM / 2 + 13:.0f}">tirant</text>',
             f'<text class="ts" x="{xc + 5:.0f}" y="{PW - KP * HM / 2 + 26:.0f}">d’air</text>']
else:
    prof += [f'<text class="ts tu" x="{PX + KP * 6.5:.0f}" y="{PW - KP * HM:.0f}">tirant d’air ? ({B["question_tirant_air"]})</text>']
prof.append('</g>')

# Cote de la largeur, hors du navire derrière le tableau arrière ; lignes de rappel
# tangentes à la coque au maître-bau du dessin (bord le plus écarté de l'axe)
xb, yb = min(bord_babord(), key=lambda q: q[1])
Xb, Xm, Yh, Yt = OX + K * -55, OX + K * xb, OY + K * yb, OY + K * M(yb)
prof += [f'<path class="amg-l" d="M{Xm:.1f} {Yh:.1f} H{Xb - 4:.1f} M{Xm:.1f} {Yt:.1f} H{Xb - 4:.1f}"/>',
         f'<path class="arr" d="M{Xb:.1f} {Yh:.1f} V{Yt:.1f} M{Xb - 3:.1f} {Yh + 6:.1f} L{Xb:.1f} {Yh:.1f} L{Xb + 3:.1f} {Yh + 6:.1f}'
         f' M{Xb - 3:.1f} {Yt - 6:.1f} L{Xb:.1f} {Yt:.1f} L{Xb + 3:.1f} {Yt - 6:.1f}"/>',
         f'<text class="ts mid halo" x="{Xb - 5:.1f}" y="{OY + K * (CY + 95):.1f}" transform="rotate(-90 {Xb - 5:.1f} {OY + K * (CY + 95):.1f})">largeur {m(B["largeur_m"])}</text>']

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 910" role="img" aria-label="Plan de bord vu de dessus : aménagement intérieur, pont et objets du bord du Gib'Sea 31.">
  <title>Folio 6 · Plan de bord</title>
  <desc>Vue de dessus, avant à droite, bâbord en haut, redessinée d'après le plan d'emménagement du constructeur. Objets du bord (sécurité, gaz, fluides, moteur, électricité) repérés par des pastilles numérotées, légendées par bord ; premier essai d'après la feuille « Emplacement trucs bateau ».</desc>
{STYLE}{DEFS}  <rect class="bg" x="0" y="0" width="100%" height="100%"/>
  ''' + "\n  ".join(el) + f'''
  <text class="ts mid" x="{OX+K*700:.0f}" y="{OY+K*20:.0f}">BÂBORD</text>
  <text class="ts mid" x="{OX+K*700:.0f}" y="{OY+K*635:.0f}">TRIBORD</text>
  <text class="tb" x="{OX+K*1665:.0f}" y="{OY+K*CY+5:.0f}">AV</text>
  <text class="tb end" x="{OX-8:.0f}" y="{OY+K*CY+5:.0f}">AR</text>
  <!-- Légendes des objets -->
  <rect class="bound" x="20" y="20" width="1360" height="150"/>
  <text class="ts" x="28" y="34">objets du bord · bâbord</text>
  <rect class="bound" x="20" y="700" width="1360" height="204"/>
  <text class="ts" x="28" y="714">objets du bord · tribord</text>
  ''' + "\n  ".join(leg) + '''
  <!-- Caractéristiques du bateau -->
  ''' + "\n  ".join(cart) + '''
  <!-- Profil tribord miniature -->
  ''' + "\n  ".join(prof) + '''
</svg>
'''
(ICI / "folio-6-plan-de-bord.svg").write_text(svg, encoding="utf-8")


def pour_inkscape(svg):
    """Copie à styles explicites : couleurs du thème clair écrites en dur (sans var()), fond verrouillé,
    pastilles et trappes du plan dans un calque à part, identifiées pN-i / tN-i (objet N, emplacement i)."""
    sans_media = re.sub(r"@media[^{]*\{svg\{[^}]*\}\}", "", svg)
    V = dict(kv for bloc in re.findall(r"svg\{(--[^}]*)\}", sans_media)
             for kv in re.findall(r"(--[\w-]+):([^;}]+)", bloc))
    svg = re.sub(r"\n\s*@media[^{]*\{svg\{[^}]*\}\}", "", svg)
    svg = re.sub(r"\n\s*svg\{--[^}]*\}", "", svg)
    svg = re.sub(r"var\((--[\w-]+)\)", lambda m: V[m.group(1)].strip(), svg)
    ids = []
    for o in OBJ:
        ids += [f"p{o['n']}-{i}" for i in range(len(o["positions"]))]
        ids += [f"t{o['n']}-{i}" for i in range(len(o.get("trappes", [])))]
    lg = svg.split("\n")
    i0 = next(i for i, l in enumerate(lg) if l.lstrip().startswith('<g class="obj'))
    plan = [l.replace('<g class="obj', f'<g id="{k}" class="obj', 1) for k, l in zip(ids, lg[i0:i0 + len(ids)])]
    reste = lg[:i0] + lg[i0 + len(ids):]
    deb = next(i for i, l in enumerate(reste) if "</style>" in l) + 1
    fin = max(i for i, l in enumerate(reste) if l.strip() == "</svg>")
    svg = "\n".join(reste[:deb]
        + ['  <g id="fond" inkscape:groupmode="layer" inkscape:label="Fond (verrouillé)" sodipodi:insensitive="true">']
        + reste[deb:fin]
        + ['  </g>', '  <g id="pastilles" inkscape:groupmode="layer" inkscape:label="Pastilles à placer">']
        + plan + ['  </g>'] + reste[fin:])
    return svg.replace('<svg xmlns="http://www.w3.org/2000/svg"',
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
        ' xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"', 1)


(ICI / "folio-6-plan-de-bord-inkscape.svg").write_text(pour_inkscape(svg), encoding="utf-8")
print("ok")
