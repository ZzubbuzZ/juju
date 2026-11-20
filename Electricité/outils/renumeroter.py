"""Renumérotation du 20/11 : sections de 100 numéros, par décalage.

Usage (depuis n'importe où) :
    python Electricité/outils/renumeroter.py            # aperçu : fichiers et nombre de remplacements
    python Electricité/outils/renumeroter.py --ecrire   # applique

Ancienne section → nouvelle (décalage) :
    001-049 batteries, coupe-circuits, shunt   → 001-049 (inchangé, section 001-099)
    050-099 charge                             → 100-149 (+50,  section 100-199)
    100-149 moteur et guindeau                 → 200-249 (+100, section 200-299)
    150-199 distribution 12 V                  → 300-349 (+150, section 300-399)
    200-249 tableau de servitude               → 400-449 (+200, section 400-499)
    300-399 réseau 230 V                       → 500-599 (+200, section 500-599)

Formes traitées : node159, wire158, n159, w158, plages (w038-40, n203-5, node325-327, tiret ou
tiret long). Le décalage étant constant dans une section, les plages restent des plages.
S'applique aux fichiers texte versionnés d'Electricité/ (sauf outils/), et à rien d'autre.
Ancienne numérotation : tag avant-renumerotation-2. Script à ne lancer qu'une fois.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent  # Electricité/
DECALAGES = ((1, 49, 0), (50, 99, 50), (100, 149, 100), (150, 199, 150), (200, 249, 200), (300, 399, 200))
BINAIRES = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".xlsx", ".docx", ".odt", ".zip"}

MOTIF = re.compile(
    r"\b(?P<p>node|wire|n|w)(?P<a>\d{3})"
    r"(?:(?P<t>[-–])(?P<p2>node|wire|n|w)?(?P<b>\d{1,3}))?\b")


class HorsSection(Exception):
    pass


def nouveau(n: int) -> int:
    for a, b, d in DECALAGES:
        if a <= n <= b:
            return n + d
    raise HorsSection(n)


def suffixe(debut: int, fin: int) -> str:
    """Le moins de chiffres possible après le tiret (w038-40, n203-5)."""
    s, e = f"{debut:03d}", f"{fin:03d}"
    for k in (1, 2, 3):
        if s[:3 - k] == e[:3 - k]:
            return e[3 - k:]
    return e


def remplacer(m: re.Match) -> str:
    p, a = m["p"], int(m["a"])
    na = nouveau(a)
    if m["b"] is None:
        return f"{p}{na:03d}"
    b = m["b"]
    fin = int(b) if len(b) == 3 else int(m["a"][:3 - len(b)] + b)
    if fin < a or nouveau(fin) - fin != na - a:   # pas une plage d'identifiants : chaque bout à part
        return f"{p}{na:03d}{m['t']}{m['p2'] or ''}{b}"
    nf = nouveau(fin)
    if m["p2"] or len(b) == 3:
        return f"{p}{na:03d}{m['t']}{m['p2'] or ''}{nf:03d}"
    return f"{p}{na:03d}{m['t']}{suffixe(na, nf)}"


def fichiers() -> list[Path]:
    sortie = subprocess.run(["git", "ls-files", "-z", "."], cwd=RACINE, capture_output=True, check=True).stdout
    liste = []
    for nom in sortie.decode("utf-8").split("\0"):
        if not nom or nom.startswith("outils/"):
            continue
        chemin = RACINE / nom
        if chemin.suffix.lower() in BINAIRES or not chemin.is_file():
            continue
        liste.append(chemin)
    return liste


def main() -> int:
    ecrire = "--ecrire" in sys.argv
    if re.search(r"node5\d\d", (RACINE / "releve" / "netlist.yaml").read_text(encoding="utf-8")):
        sys.exit("Déjà appliquée (le 230 V est en 500-599) : une seconde passe décalerait encore les numéros.")
    total, erreurs = 0, []
    for chemin in fichiers():
        try:
            texte = chemin.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            continue
        nb = 0

        def compte(m: re.Match) -> str:
            nonlocal nb
            try:
                r = remplacer(m)
            except HorsSection as e:
                erreurs.append(f"{chemin.relative_to(RACINE)} : {m[0]} (numéro {e.args[0]} hors des anciennes sections)")
                return m[0]
            nb += r != m[0]
            return r

        neuf = MOTIF.sub(compte, texte)
        if nb:
            total += nb
            print(f"{nb:5d}  {chemin.relative_to(RACINE)}")
            if ecrire:
                chemin.write_bytes(neuf.encode("utf-8"))
    for e in erreurs:
        print("ERREUR", e)
    print(f"{total} remplacement(s){'' if ecrire else ' (aperçu, rien écrit)'}")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
