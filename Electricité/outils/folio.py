#!/usr/bin/env python3
"""Générateur de folios : produit un folio SVG à partir de sa mise en page YAML et des données.

Usage :
    python Electricité/outils/folio.py              # régénère tous les folios décrits par un folio-*.yaml
    python Electricité/outils/folio.py chemin.yaml  # un seul folio

La mise en page (folio-XX-nom.yaml, à côté du SVG) place les appareils, les nœuds sur leur pourtour,
les barres, le tracé des fils et les textes. Le reste vient du modèle (relevé, hypothèse ou cible) :
fonction des bornes, polarité, section et statut des fils, nouveauté des appareils.

Règles de dessin contrôlées par controler() (appelée aussi par verifier.py) :
- un nœud est un rond sur le pourtour de son appareil, avec son ID abrégé et sa fonction en dessous ;
  pour une boîte, l'étiquette est à l'intérieur du contour ; un interrupteur a un pseudo-contour pointillé ;
- un fil part exactement d'un nœud et arrive exactement sur un nœud (ou sur une barre, ou un renvoi) ;
- ses segments font 0, 45, 90, 135… degrés ;
- deux fils ne se superposent que sur un segment qui aboutit à un nœud qu'ils partagent (ils peuvent se croiser) ;
- un fil ne traverse aucun appareil ni renvoi et n'en longe pas le contour ;
- les croisements sont permis mais à réduire au minimum : chacun est signalé, sauf s'il est admis
  dans la mise en page (croisements_admis: [[wire216, wire206]], après avoir cherché un tracé sans).
"""
from __future__ import annotations

import math
import re
import sys
from html import escape
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verifier as V  # noqa: E402

STYLE = '''  <style>
    /* Style autonome : retiré par outils/page.py quand le folio est intégré à la page HTML. */
    svg{--sheet:#fbfcfd;--ink:#18212b;--muted:#5a6776;--pos:#c8231c;--unk:#1f6fbf;--warn:#e58a00;--on-warn:#1a1206;--new:#1d8a4a;--new-soft:#e2f3e8;--zone:#e8edf2;--ph:#8a5a2b;--ne:#2563c4;--pe:#2f9e44;--pey:#e6b800}
    @media (prefers-color-scheme: dark){svg{--sheet:#151b22;--ink:#e3e8ee;--muted:#93a1b0;--pos:#ff5a4f;--unk:#5aa9f5;--warn:#ffa53d;--new:#4fcf85;--new-soft:#15301f;--zone:#1f2832;--ph:#c8915a;--ne:#6aa7ff;--pe:#51cf66;--pey:#ffd43b}}
    .bg{fill:var(--sheet)}
    text{font-family:"IBM Plex Sans Condensed","Arial Narrow","Roboto Condensed",sans-serif;fill:var(--ink)}
    .t{font-size:12.5px}.tb{font-size:13px;font-weight:600}.ts{font-size:11.5px;fill:var(--muted)}
    .id,.idn,.pin{font-family:"IBM Plex Mono",Consolas,monospace}
    .id{font-size:10.5px;fill:var(--muted)}.idn{font-size:10.5px;fill:var(--new)}.pin{font-size:8.5px;fill:var(--ink)}
    .tu{fill:var(--unk)}.tn{fill:var(--new)}.mid{text-anchor:middle}.end{text-anchor:end}
    .p,.n,.u,.lever,.bound,.ph,.ne,.pe,.pey,.leader{fill:none;stroke-linecap:round;stroke-linejoin:round}
    .p{stroke:var(--pos)}.n{stroke:var(--ink)}
    .ph{stroke:var(--ph)}.ne{stroke:var(--ne)}.pe{stroke:var(--pe)}.pey{stroke:var(--pey);stroke-dasharray:6 6;stroke-linecap:butt}
    .u{stroke:var(--unk);stroke-width:1.6;stroke-dasharray:6 4}
    .bound{stroke:var(--muted);stroke-width:1;stroke-dasharray:2 4}
    .w1{stroke-width:1.3}.w2{stroke-width:2}.w3{stroke-width:2.8}.w4{stroke-width:4}.w5{stroke-width:5.5}
    .box{fill:var(--sheet);stroke:var(--ink);stroke-width:1.4}
    .box-new{fill:var(--new-soft);stroke:var(--new);stroke-width:1.6}
    .box-unk{fill:var(--sheet);stroke:var(--unk);stroke-width:1.5;stroke-dasharray:6 4}
    .fuse{fill:var(--sheet);stroke:var(--ink);stroke-width:1.3}
    .fuse-new{fill:var(--new-soft);stroke:var(--new);stroke-width:1.6}
    .dp{fill:var(--pos)}.dn{fill:var(--ink)}
    .term{fill:var(--sheet);stroke:var(--ink);stroke-width:1.4}
    .lever{stroke:var(--ink);stroke-width:2}
    .sw{fill:none;stroke:var(--muted);stroke-width:1;stroke-dasharray:5 3}
    .flag{fill:var(--sheet);stroke:var(--ink);stroke-width:1.2}
    .flag-new{fill:var(--new-soft);stroke:var(--new);stroke-width:1.4}
    .hull{fill:var(--sheet);stroke:var(--ink);stroke-width:2}
    .zone{fill:var(--zone);stroke:var(--muted);stroke-width:1}
    .zone-pont{fill:none;stroke:var(--muted);stroke-width:1.2;stroke-dasharray:4 3}
    .leader{stroke:var(--muted);stroke-width:1}
    .callout{fill:var(--sheet);stroke:var(--ink);stroke-width:1.2}
    .mk-a circle{fill:var(--warn)}
    .mk-a text{fill:var(--on-warn);font-family:"IBM Plex Mono",Consolas,monospace;font-size:9.5px;font-weight:500}
    .mk-q circle{fill:var(--sheet);stroke:var(--unk);stroke-width:1.5}
    .mk-q text{fill:var(--unk);font-family:"IBM Plex Mono",Consolas,monospace;font-size:9.5px;font-weight:500}
  </style>
'''

# Fonction abrégée d'une borne (champ « borne » des données) ; la mise en page peut la remplacer (fonction:).
ABREGES = {
    "1 (côté batterie)": "bat", "1 (côté batteries)": "bat", "2 (côté charges)": "ch",
    "1 (côté source)": "1", "1 (primaire)": "1", "2 (secondaire)": "2",
    "1 (côté servitude)": "serv", "2 (côté moteur)": "mot",
    "entrée +": "e+", "entrée -": "e−", "sortie +": "s+", "sortie −": "s−", "-": "−",
    "remote H": "H", "masse du voyant": "voyant", "+ démarreur / alternateur": "+",
    "masse moteur": "−", "masse": "−", "sortie 1 (moteur)": "s1", "sortie 2 (servitude)": "s2",
    "sortie moteur A": "A", "sortie moteur B": "B", "entrée": "e", "sortie": "s",
    "30 (entrée)": "30", "87 (sortie)": "87", "86 (bobine +)": "86", "85 (bobine −)": "85",
    "12 V +": "+", "12 V −": "−", "− batterie": "− bat", "− système": "− sys",
    "commande montée": "mont", "commande descente": "desc", "commande masse": "−", "montée": "mont", "descente": "desc",
    "+ alimentation et mesure (Vbatt+)": "Vbat+", "entrée auxiliaire (tension batterie moteur)": "aux",
}


def abreger(borne: str) -> str:
    if borne in ABREGES:
        return ABREGES[borne]
    court = re.sub(r"\s*\(.*?\)", "", borne).strip()
    return court if len(court) <= 12 else court[:11] + "…"


def court(ident: str) -> str:
    """node006 → n006, wire234 → w234."""
    return re.sub(r"^(node|wire)(\d{3})$", lambda m: m.group(1)[0] + m.group(2), ident)


# --------------------------------------------------------------------------- modèle
def modeles() -> dict:
    r = V.Rapport()
    releve = V.Modele("releve")
    for nom in V.FICHIERS_RELEVE:
        releve.ajouter(V.lire_yaml(V.RELEVE / nom, r), nom, r)
    hyps = {}
    for c in sorted((V.RACINE / "etudes").glob("*/H*/cablage.yaml")):
        d = V.lire_yaml(c, r)
        hyps[d["hypothese"]] = (c, d)
    mods = {"releve": releve}

    def res(i):
        if i not in mods:
            c, d = hyps[i]
            mods[i] = V.appliquer_delta(res(d["base"]), d, i, str(c), r)
        return mods[i]
    for i in hyps:
        res(i)
    cible = V.lire_yaml(V.RACINE / "cible" / "cible.yaml", r) or {}
    m = None
    for k, i in enumerate(cible.get("hypotheses", [])):
        m = res(i) if k == 0 else V.appliquer_delta(m, hyps[i][1], "cible", "cible", r)
    if m is not None:
        mods["cible"] = m
    return mods


# --------------------------------------------------------------------------- géométrie
def angle_ok(a, b) -> bool:
    dx, dy = b[0] - a[0], b[1] - a[1]
    return dx == 0 or dy == 0 or abs(dx) == abs(dy)


def sur_segment(p, a, b, tol=0.01) -> bool:
    (px, py), (ax, ay), (bx, by) = p, a, b
    if abs((bx - ax) * (py - ay) - (by - ay) * (px - ax)) > tol * max(1, math.dist(a, b)):
        return False
    return min(ax, bx) - tol <= px <= max(ax, bx) + tol and min(ay, by) - tol <= py <= max(ay, by) + tol


def recouvrement(s1, s2):
    """Portion commune (de longueur non nulle) de deux segments colinéaires, ou None."""
    (a, b), (c, d) = s1, s2
    ux, uy = b[0] - a[0], b[1] - a[1]
    long = math.hypot(ux, uy)
    if long == 0:
        return None
    # c et d doivent être sur la droite (a, b)
    for p in (c, d):
        if abs(ux * (p[1] - a[1]) - uy * (p[0] - a[0])) > 0.5 * long:
            return None
    t = lambda p: ((p[0] - a[0]) * ux + (p[1] - a[1]) * uy) / long
    lo, hi = max(0, min(t(c), t(d))), min(long, max(t(c), t(d)))
    if hi - lo < 1:
        return None
    pt = lambda k: (round(a[0] + ux * k / long, 1), round(a[1] + uy * k / long, 1))
    return pt(lo), pt(hi)


def croisement(s1, s2, eps=1e-6):
    """Point où deux segments se coupent à l'intérieur de chacun (croisement franc), ou None."""
    (a, b), (c, d) = s1, s2
    rx, ry, sx, sy = b[0] - a[0], b[1] - a[1], d[0] - c[0], d[1] - c[1]
    den = rx * sy - ry * sx
    if abs(den) < eps:   # parallèles ou colinéaires : affaire de recouvrement()
        return None
    t = ((c[0] - a[0]) * sy - (c[1] - a[1]) * sx) / den
    u = ((c[0] - a[0]) * ry - (c[1] - a[1]) * rx) / den
    if eps < t < 1 - eps and eps < u < 1 - eps:
        return (round(a[0] + t * rx, 1), round(a[1] + t * ry, 1))
    return None


def traverse(a, b, typ, g, eps=0.75):
    """« traverse » si le segment passe à l'intérieur du composant, « longe » s'il suit son contour, sinon None.
    Toucher le contour en un point (un nœud) est permis."""
    n = max(2, int(math.dist(a, b)))
    pts = [(a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n) for k in range(1, n)]
    if typ == "rect":
        x0, y0, x1, y1 = g
        dedans = [p for p in pts if x0 + eps < p[0] < x1 - eps and y0 + eps < p[1] < y1 - eps]
        if dedans:
            return "traverse"
        bord = [p for p in pts if (abs(p[0] - x0) <= eps or abs(p[0] - x1) <= eps) and y0 - eps <= p[1] <= y1 + eps
                or (abs(p[1] - y0) <= eps or abs(p[1] - y1) <= eps) and x0 - eps <= p[0] <= x1 + eps]
        if len(bord) > 1:
            return "longe le contour de"
    else:
        cx, cy, r = g
        d = [math.dist(p, (cx, cy)) for p in pts]
        if any(x < r - eps for x in d):
            return "traverse"
        if sum(1 for x in d if abs(x - r) <= eps) > 1:
            return "longe le contour de"
    return None


# --------------------------------------------------------------------------- dessin
class Folio:
    def __init__(self, chemin: Path, mods: dict):
        self.chemin = chemin
        self.L = yaml.safe_load(chemin.read_text(encoding="utf-8"))
        self.M = mods[self.L["modele"]]
        self.pos = {}       # nœud → (x, y)
        self.cote = {}      # nœud → côté (pour l'étiquette)
        self.barres = {}    # nœud → [(a, b)]
        self.traces = {}    # fil → [points]
        self.liaisons = []  # (« n074 – n070 », a, b) : montage direct d'une borne sur une autre
        self.cable = {}     # fil → câble unifilaire qui le porte
        self.forme = {}     # nœud → forme de son appareil
        self.contours = []  # (nom, 'rect', (x0, y0, x1, y1), nœuds) ou (nom, 'cercle', (cx, cy, r), nœuds)
        self.rect = {}      # nœud → contour rectangulaire de sa boîte (étiquette à l'intérieur)
        self.erreurs = []
        self.out = []

    # -- appareils
    def nouveau(self, equipement):
        e = self.M.equipements.get(equipement, {})
        return e.get("statut") == "propose"

    def placer_noeuds(self, ap):
        x, y, w, h = ap.get("x", 0), ap.get("y", 0), ap.get("w", 0), ap.get("h", 0)
        for n, spec in (ap.get("nodes") or {}).items():
            spec = spec if isinstance(spec, dict) else {"cote": spec[0], "a": spec[1] if len(spec) > 1 else None}
            cote, a = spec["cote"], spec.get("a")
            if ap.get("forme") == "cercle":
                cx, cy, r = ap["cx"], ap["cy"], ap["r"]
                ang = math.radians(spec["angle"])
                p = (round(cx + r * math.cos(ang), 1), round(cy - r * math.sin(ang), 1))
            elif cote == "point":
                p = tuple(spec["xy"])
            elif cote in ("haut", "bas"):
                p = (a if a is not None else x + w / 2, y if cote == "haut" else y + h)
            else:
                p = (x if cote == "gauche" else x + w, a if a is not None else y + h / 2)
            self.pos[n] = p
            self.cote[n] = (cote, spec.get("etiquette"), spec.get("fonction"))
            self.forme[n] = ap.get("forme", "boite")
            if self.forme[n] == "boite":
                self.rect[n] = (x, y, x + w, y + h)
            if n not in self.M.nodes:
                self.erreurs.append(f"{n} placé sur le folio mais absent du modèle {self.L['modele']}")

    def dessiner_appareil(self, ap):
        forme = ap.get("forme", "boite")
        noeuds = set(ap.get("nodes") or {})
        nom = ap.get("id", "?")
        if forme == "boite":
            self.contours.append((nom, "rect", (ap["x"], ap["y"], ap["x"] + ap["w"], ap["y"] + ap["h"]), noeuds))
        elif forme == "cercle":
            self.contours.append((nom, "cercle", (ap["cx"], ap["cy"], ap["r"]), noeuds))
        elif forme == "fusible":
            (x1, y1), (x2, y2) = (self.pos[n] for n in list(ap["nodes"])[:2])
            r = (min(x1, x2), y1 - 9, max(x1, x2), y1 + 9) if y1 == y2 else (x1 - 8, min(y1, y2), x1 + 8, max(y1, y2))
            self.contours.append((nom, "rect", r, noeuds))
        elif forme == "interrupteur":
            r = self.contour_interrupteur(ap)
            self.contours.append((nom, "rect", r, noeuds))
            for n in noeuds:
                x, y = self.pos[n]
                if not (r[0] <= x <= r[2] and r[1] <= y <= r[3]) or (r[0] < x < r[2] and r[1] < y < r[3]):
                    self.erreurs.append(f"{n} n'est pas sur le contour de {nom} {r}")
        neuf = ap.get("nouveau", self.nouveau(ap.get("id", "")))
        o = self.out
        if forme == "boite":
            cls = "box-new" if neuf else ("box-unk" if ap.get("inconnu") else "box")
            o.append(f'<rect class="{cls}" x="{ap["x"]}" y="{ap["y"]}" width="{ap["w"]}" height="{ap["h"]}" rx="2"/>')
            cx = ap["x"] + ap["w"] / 2
            y = ap["y"] + ap.get("titre_y", 20)
            if ap.get("titre"):
                o.append(f'<text class="tb mid{" tn" if neuf else ""}" x="{cx:g}" y="{y:g}">{escape(ap["titre"])}</text>')
            for k, l in enumerate(ap.get("lignes", [])):
                o.append(f'<text class="ts mid" x="{cx:g}" y="{y + 15 * (k + 1):g}">{escape(l)}</text>')
        elif forme == "fusible":
            n1, n2 = list(ap["nodes"])
            (x1, y1), (x2, y2) = self.pos[n1], self.pos[n2]
            cls = "fuse-new" if neuf else "fuse"
            tcls = "idn" if neuf else "id"
            if y1 == y2:   # horizontal
                o.append(f'<rect class="{cls}" x="{min(x1, x2):g}" y="{y1 - 9:g}" width="{abs(x2 - x1):g}" height="18"/>')
                o.append(f'<text class="{tcls} mid" x="{(x1 + x2) / 2:g}" y="{y1 + 4:g}">{escape(ap["calibre"])}</text>')
            else:
                o.append(f'<rect class="{cls}" x="{x1 - 8:g}" y="{min(y1, y2):g}" width="16" height="{abs(y2 - y1):g}"/>')
                d = ap.get("calibre_cote", "droite")
                tx = x1 + 12 if d == "droite" else x1 - 12
                o.append(f'<text class="{tcls}{"" if d == "droite" else " end"}" x="{tx:g}" y="{(y1 + y2) / 2 + 4:g}">{escape(ap["calibre"])}</text>')
            if ap.get("titre"):
                tx, ty, anc = ap["titre_xy"] + [ap.get("titre_ancre", "mid")] if "titre_xy" in ap else ((x1 + x2) / 2, min(y1, y2) - 14, "mid")
                o.append(f'<text class="ts{" tn" if neuf else ""} {anc}" x="{tx:g}" y="{ty:g}">{escape(ap["titre"])}</text>')
        elif forme == "interrupteur":
            n1, n2 = list(ap["nodes"])[:2]
            (x1, y1), (x2, y2) = self.pos[n1], self.pos[n2]
            r = self.contour_interrupteur(ap)
            o.append(f'<rect class="sw" x="{r[0]:g}" y="{r[1]:g}" width="{r[2] - r[0]:g}" height="{r[3] - r[1]:g}" rx="2"/>')
            if y1 == y2:
                o.append(f'<path class="lever" d="M{x1:g} {y1:g} L{x2 - 3:g} {y1 - 13:g}"/>')
            else:
                o.append(f'<path class="lever" d="M{x1:g} {y1:g} L{x1 + 11:g} {y2 - 3:g}"/>')
            if ap.get("titre"):
                tx, ty = ap["titre_xy"]
                anc = ap.get("titre_ancre", "mid")
                o.append(f'<text class="ts{" tn" if neuf else ""} {anc}" x="{tx:g}" y="{ty:g}">{escape(ap["titre"])}</text>')
        elif forme == "cercle":
            o.append(f'<circle class="{"box-new" if neuf else "box"}" cx="{ap["cx"]}" cy="{ap["cy"]}" r="{ap["r"]}"/>')
            o.append(f'<text class="tb mid" x="{ap["cx"]}" y="{ap["cy"] + 5}">{escape(ap.get("symbole", ""))}</text>')
            for k, l in enumerate(ap.get("lignes", [])):
                o.append(f'<text class="ts mid" x="{ap["cx"]}" y="{ap["cy"] + ap["r"] + 16 + 15 * k}">{escape(l)}</text>')

    def contour_interrupteur(self, ap):
        """Pseudo-contour d'un interrupteur : ses deux bornes au milieu de deux côtés opposés."""
        (x1, y1), (x2, y2) = (self.pos[n] for n in list(ap["nodes"])[:2])
        m = ap.get("marge", 16)
        if y1 == y2:
            return (min(x1, x2), y1 - m, max(x1, x2), y1 + m)
        return (x1 - m, min(y1, y2), x1 + m, max(y1, y2))

    def etiquette_noeud(self, n, groupe=None):
        x, y = self.pos[n]
        cote, et, fonction = self.cote[n]
        borne = self.M.nodes.get(n, {}).get("borne", "")
        if self.forme.get(n) in ("fusible", "interrupteur"):
            f = fonction or ""
        else:
            f = fonction if fonction is not None else abreger(borne)
            if groupe and len(groupe) > 1 and fonction is None:
                f = "/".join(abreger(self.M.nodes.get(g, {}).get("borne", "")) for g in groupe)
        if et:
            dx, dy, anc = et[0], et[1], (et[2] if len(et) > 2 else "")
        elif n in self.rect:   # boîte : ID et fonction à l'intérieur du contour
            dx, dy, anc = {"haut": (5, 14, ""), "bas": (5, -16 if f else -6, ""), "gauche": (7, -1 if f else 4, ""),
                           "droite": (-7, -1 if f else 4, "end")}[cote]
            if cote in ("haut", "bas") and x > (self.rect[n][0] + self.rect[n][2]) / 2:   # moitié droite : aligné à droite
                dx, anc = -5, "end"
        else:
            dx, dy, anc = {"haut": (5, -17 if f else -6, ""), "bas": (5, 14, ""), "gauche": (-7, -6, "end"),
                           "droite": (7, -6, ""), "point": (6, -6, "")}.get(cote, (6, -6, ""))
        nd = self.M.nodes.get(n, {})
        neuf = nd.get("statut") == "propose" or self.nouveau(nd.get("equipement", ""))
        cls = "idn" if neuf else "id"
        a = f" {anc}" if anc else ""
        ident = " / ".join(court(g) for g in groupe) if groupe else court(n)
        self.out.append(f'<text class="{cls}{a}" x="{x + dx:g}" y="{y + dy:g}">{ident}</text>')
        if n in self.rect:
            x0, y0, x1, y1 = self.rect[n]
            if not (x0 < x + dx < x1 and y0 < y + dy - 8 and y + dy + (10 if f else 0) < y1):
                self.erreurs.append(f"{n} : l'étiquette ({x + dx:g}, {y + dy:g}) sort du contour de son appareil")
        if f:
            self.out.append(f'<text class="pin{a}" x="{x + dx:g}" y="{y + dy + 10:g}">{escape(f)}</text>')

    # -- fils
    def classe_fil(self, w):
        f = self.M.fils[w]
        if "section_mm2" not in f:   # section inconnue : partie incertaine, en pointillés bleus
            return "u"
        pol = {self.M.nodes[f["de"]]["polarite"], self.M.nodes[f["vers"]]["polarite"]}
        c = "n" if pol <= {"-"} else ("ph" if "230V-phase" in pol else "ne" if "230V-neutre" in pol else "pe" if "230V-terre" in pol else "p")
        s = f.get("section_mm2", 1.5)
        ep = "w1" if s <= 1.5 else "w2" if s <= 6 else "w3" if s <= 16 else "w4" if s <= 35 else "w5"
        return f"{c} {ep}"

    def dessiner_fil(self, w, spec, dessin=True):
        if w not in self.M.fils:
            self.erreurs.append(f"{w} tracé mais absent du modèle {self.L['modele']}")
            return
        f = self.M.fils[w]
        pts = [tuple(p) for p in spec.get("trace", [])]
        for bout, idx in (("de", 0), ("vers", -1)):
            n = f[bout]
            if n in self.pos:
                p = self.pos[n]
                if not pts or (pts[idx] != p and not self.sur_barre(n, pts[idx])):
                    pts.insert(0 if idx == 0 else len(pts), p)
        self.traces[w] = pts
        if not dessin:
            return
        d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts)
        self.out.append(f'<path class="{spec.get("classe") or self.classe_fil(w)}" d="{d}"/>')
        et = spec.get("etiquette")
        if et:
            texte = spec.get("texte") or (court(w) + (f" · {f['section_mm2']:g}".replace(".", ",") if "section_mm2" in f else ""))
            cls = "idn" if f.get("statut") == "propose" else "id"
            anc = f" {et[2]}" if len(et) > 2 and et[2] else ""
            rot = f' transform="rotate(-90 {et[0]:g} {et[1]:g})"' if len(et) > 3 and et[3] == "v" else ""
            self.out.append(f'<text class="{cls}{anc}" x="{et[0]:g}" y="{et[1]:g}"{rot}>{escape(texte)}</text>')

    def dessiner_cable(self, nom, spec):
        """Câble unifilaire : un seul trait pour ses conducteurs, barres obliques = nombre de conducteurs."""
        fils = [w for w in spec["fils"] if w in self.M.fils]
        for w in spec["fils"]:
            self.dessiner_fil(w, {"trace": spec.get("trace", [])}, dessin=False)
            self.cable[w] = nom
        if not fils:
            return
        pts = self.traces[fils[0]]
        d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts)
        self.out.append(f'<path class="{spec.get("classe", "n w2")}" d="{d}"/>')
        a, b = max(zip(pts, pts[1:]), key=lambda s: math.dist(*s))
        x, y = spec.get("obliques_xy") or ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        k = len(spec["fils"])
        for i in range(k):
            o = (i - (k - 1) / 2) * 5
            if a[1] == b[1]:
                self.out.append(f'<path class="n w1" d="M{x + o - 3:g} {y + 5:g} L{x + o + 3:g} {y - 5:g}"/>')
            else:
                self.out.append(f'<path class="n w1" d="M{x - 5:g} {y + o + 3:g} L{x + 5:g} {y + o - 3:g}"/>')
        et = spec.get("etiquette")
        if et:
            texte = spec.get("texte") or " / ".join(court(w) for w in spec["fils"])
            neuf = any(self.M.fils[w].get("statut") == "propose" for w in fils)
            anc = f" {et[2]}" if len(et) > 2 and et[2] else ""
            rot = f' transform="rotate(-90 {et[0]:g} {et[1]:g})"' if len(et) > 3 and et[3] == "v" else ""
            self.out.append(f'<text class="{"idn" if neuf else "id"}{anc}" x="{et[0]:g}" y="{et[1]:g}"{rot}>{escape(texte)}</text>')

    def sur_barre(self, n, p):
        return any(sur_segment(p, a, b) for a, b in self.barres.get(n, []))

    # -- contrôle des règles
    def controler(self):
        err = self.erreurs
        for w, pts in self.traces.items():
            f = self.M.fils[w]
            for a, b in zip(pts, pts[1:]):
                if not angle_ok(a, b):
                    err.append(f"{w} : segment {a} → {b} hors des angles 0/45/90°")
            for bout, p in (("de", pts[0]), ("vers", pts[-1])):
                n = f[bout]
                if n in self.pos and p != self.pos[n] and not self.sur_barre(n, p):
                    err.append(f"{w} : l'extrémité {p} n'est pas sur {n} {self.pos[n]}")
        for w, pts in self.traces.items():
            f = self.M.fils[w]
            for a, b in zip(pts, pts[1:]):
                for nom, typ, g, noeuds in self.contours:
                    probleme = traverse(a, b, typ, g)
                    if probleme:
                        err.append(f"{w} : le segment {a} → {b} {probleme} {nom}")
        for nom_l, a, b in self.liaisons:
            if not angle_ok(a, b):
                err.append(f"{nom_l} : segment {a} → {b} hors des angles 0/45/90°")
            for nom, typ, g, noeuds in self.contours:
                probleme = traverse(a, b, typ, g)
                if probleme:
                    err.append(f"{nom_l} : le segment {a} → {b} {probleme} {nom}")
        segs = [(w, a, b) for w, pts in self.traces.items() for a, b in zip(pts, pts[1:])]
        for i, (w1, a1, b1) in enumerate(segs):
            for w2, a2, b2 in segs[i + 1:]:
                if w1 == w2 or (w1 in self.cable and self.cable.get(w2) == self.cable[w1]):
                    continue
                r = recouvrement((a1, b1), (a2, b2))
                if not r:
                    continue
                f1, f2 = self.M.fils[w1], self.M.fils[w2]
                communs = {f1["de"], f1["vers"]} & {f2["de"], f2["vers"]}
                if not any(n in self.pos and (self.pos[n] in r or sur_segment(self.pos[n], *r)) and
                           (self.pos[n] in (a1, b1)) and (self.pos[n] in (a2, b2)) for n in communs):
                    err.append(f"{w1} et {w2} se superposent entre {r[0]} et {r[1]} hors d'un segment de convergence")
        return err

    def croisements(self):
        """Croisements entre fils (et barres) non admis par la mise en page (croisements_admis)."""
        segs = list(dict.fromkeys((self.cable.get(w) or court(w), a, b)
                                  for w, pts in self.traces.items() for a, b in zip(pts, pts[1:])))
        segs += [(court(n), a, b) for n, bs in self.barres.items() for a, b in bs]
        admis = {frozenset(x if x in (self.L.get("cables") or {}) else court(x) for x in paire) for paire in self.L.get("croisements_admis", []) or []}
        vus = []
        for i, (n1, a1, b1) in enumerate(segs):
            for n2, a2, b2 in segs[i + 1:]:
                if n1 != n2 and frozenset((n1, n2)) not in admis:
                    p = croisement((a1, b1), (a2, b2))
                    if p:
                        vus.append(f"{n1} croise {n2} en {p}")
        return vus

    # -- assemblage
    def svg(self) -> str:
        L = self.L
        W, H = L["taille"]
        for b in L.get("barres", []) or []:
            self.barres.setdefault(b["node"], []).append((tuple(b["de"]), tuple(b["a"])))
        for ap in L.get("appareils", []):
            self.placer_noeuds(ap)
        o = self.out
        for z in L.get("zones", []) or []:
            o.append(f'<rect class="bound" x="{z["x"]}" y="{z["y"]}" width="{z["w"]}" height="{z["h"]}"/>')
            o.append(f'<text class="ts" x="{z["x"] + 10}" y="{z["y"] + 18}">{escape(z["texte"])}</text>')
        for z in L.get("incertains", []) or []:   # zone d'ombre : ce qui reste à relever
            o.append(f'<rect class="u" x="{z["x"]}" y="{z["y"]}" width="{z["w"]}" height="{z["h"]}" rx="4"/>')
            if z.get("texte"):
                tx, ty = z.get("texte_xy", [z["x"] + 8, z["y"] + 16])
                o.append(f'<text class="ts tu" x="{tx}" y="{ty}">{escape(z["texte"])}</text>')
        for ap in L.get("appareils", []):
            self.dessiner_appareil(ap)
        for b in L.get("barres", []) or []:
            pol = self.M.nodes[b["node"]]["polarite"]
            o.append(f'<path class="{"n" if pol == "-" else "p"} {b.get("epaisseur", "w4")}" d="M{b["de"][0]} {b["de"][1]} H{b["a"][0]}"/>'
                     if b["de"][1] == b["a"][1] else
                     f'<path class="{"n" if pol == "-" else "p"} {b.get("epaisseur", "w4")}" d="M{b["de"][0]} {b["de"][1]} V{b["a"][1]}"/>')
        for t in L.get("traits", []) or []:   # traits libres (repères, tuyauteries), hors règles des fils
            o.append(f'<path class="{t.get("classe", "leader")}" d="M' + " L".join(f"{x:g} {y:g}" for x, y in t["points"]) + '"/>')
        for w, spec in (L.get("fils") or {}).items():
            self.dessiner_fil(w, spec or {})
        for nom, spec in (L.get("cables") or {}).items():
            self.dessiner_cable(nom, spec)
        for m in L.get("liaisons", []) or []:   # montage direct d'une borne sur une autre (sans fil)
            a, b = self.pos[m[0]], self.pos[m[1]]
            self.liaisons.append((f"liaison {court(m[0])} – {court(m[1])}", a, b))
            pol = self.M.nodes[m[0]]["polarite"]
            o.append(f'<path class="{"n" if pol == "-" else "p"} w2" d="M{a[0]:g} {a[1]:g} L{b[0]:g} {b[1]:g}"/>')
        for rv in L.get("renvois", []) or []:
            self.contours.append(("renvoi « " + rv["texte"] + " »", "rect", (rv["x"], rv["y"], rv["x"] + rv["w"], rv["y"] + rv.get("h", 18)), set()))
            cls = "flag-new" if rv.get("nouveau") else "flag"
            o.append(f'<rect class="{cls}" x="{rv["x"]}" y="{rv["y"]}" width="{rv["w"]}" height="{rv.get("h", 18)}"/>')
            o.append(f'<text class="ts mid" x="{rv["x"] + rv["w"] / 2:g}" y="{rv["y"] + 13}">{escape(rv["texte"])}</text>')
        for n in self.pos:   # les ronds par-dessus les fils
            x, y = self.pos[n]
            o.append(f'<circle class="term" cx="{x:g}" cy="{y:g}" r="3.5"/>')
        groupes = {}
        for n in self.pos:   # nœuds confondus (bornes d'un câble unifilaire) : une seule étiquette
            groupes.setdefault(self.pos[n], []).append(n)
        for ns in groupes.values():
            self.etiquette_noeud(ns[0], ns)
        for t in L.get("textes", []) or []:
            o.append(f'<text class="{t.get("classe", "ts")}" x="{t["x"]}" y="{t["y"]}">{escape(t["texte"])}</text>')
        for p in L.get("pastilles", []) or []:
            k = "mk-q" if p["id"].startswith("Q") else "mk-a"
            o.append(f'<g class="{k}"><circle cx="{p["x"]}" cy="{p["y"]}" r="11"/><text class="mid" x="{p["x"]}" y="{p["y"] + 3.5}">{p["id"]}</text></g>')
        tete = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(L["aria"])}">\n'
                f'  <title>Folio {L["folio"]} · {escape(L["titre"])}</title>\n  <desc>{escape(L["desc"])}</desc>\n'
                + STYLE + '  <rect class="bg" x="0" y="0" width="100%" height="100%"/>\n'
                f'  <!-- Généré par outils/folio.py depuis {self.chemin.name} : ne pas modifier à la main. -->\n')
        return tete + "".join(f"  {l}\n" for l in o) + "</svg>\n"


def generer(chemin: Path, mods: dict | None = None, ecrire: bool = True) -> tuple[str, list[str], list[str]]:
    """Texte du SVG, erreurs de dessin, croisements non admis (à réduire au minimum)."""
    f = Folio(chemin, mods or modeles())
    texte = f.svg()
    err = f.controler()
    if ecrire:
        chemin.with_suffix(".svg").write_text(texte, encoding="utf-8")
    return texte, err, f.croisements()


def main(args: list[str]) -> int:
    chemins = [Path(a) for a in args] or sorted(V.RACINE.rglob("folio-*.yaml"))
    mods = modeles()
    total = 0
    for c in chemins:
        _, err, crois = generer(c, mods)
        print(f"{c.relative_to(V.RACINE) if c.is_absolute() else c} : {len(err)} erreur(s), {len(crois)} croisement(s) non admis")
        for e in err:
            print("   ", e)
        for e in crois:
            print("    (croisement)", e)
        total += len(err)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
