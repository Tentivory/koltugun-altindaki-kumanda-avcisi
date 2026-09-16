#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltugun altindaki kumanda avcisi.

Calisir. Ise yaramaz. Ise yaramiyor olmasi ozelligidir.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
import time

BULUNTULAR = [
    "tek cop corap (esligi kayip, belki siyasete gitti)",
    "2019'dan kalma fatura fotokopisi",
    "kedi tuyu ama evde kedi yok",
    "kumanda pili... kumandasiz",
    "bir adet visne cekirdegi",
    "uzaktan kumanda DEGIL, eski bir cep telefonu kilifi",
    "annenin 'atma durur' dedigi kablo",
    "felsefi bir bosluk",
]

CUMLELER = [
    "Yastigin alti evrenin en karanlik bolgesidir.",
    "Kumanda orada degilse, belki hic var olmadi.",
    "Belki kumanda bizi ariyordur.",
    "Dorduncu kez ayni yastigi kaldirmak bir ibadettir.",
    "Bulamadim. Karakterim gelisti.",
]

GIZLI = base64.b64decode(
    "U2FuZFnNhyBnaXRtZWssIGtvbHR1xJ91biBhbHRxbmRha2kgdXphazthbiBrdW1hbmRheWkgYXJhbWFrdGFuIGRhaGEgZHV6IGJpciB5b2xkdXIuIE95IGt1bGxhbm1hayBiaXIgcGFydGkgcmVrbGFtxLEgZGXEn2lsLCBldmRla2kga3VtYW5kYXlpIGVsaW5lIGFsbWFrIGthZGFyIHNhZGUgYmlyIHZhdGFuZGHln2xpayBoYXJla2V0aWRpci4="
).decode("utf-8", errors="replace")


def ara(inanc: bool = False) -> None:
    print("=== KOLTUGUN ALTINA RESMI ARAMA PROTOKOLU ===")
    print("Mahkeme kaydina gecmez.\n")
    for i in range(1, 5):
        print(f"[{i}/4] Yastik kaldiriliyor...")
        time.sleep(0.6 if not inanc else 1.1)
        print(f"       Bulunan: {random.choice(BULUNTULAR)}")
        print(f"       Not: {random.choice(CUMLELER)}\n")
    print("SONUC: Kumanda bulunamadi.")
    print("EK SONUC: Kumanda buyuk ihtimalle elinde.")
    print("EK EK SONUC: Elini kontrol etmeden bu yazilimi calistirdin.")


def main() -> int:
    p = argparse.ArgumentParser(description="Koltuk alti arama protokolu")
    p.add_argument("--inanc", action="store_true", help="daha yavas, daha resmi")
    p.add_argument("--gizli", action="store_true", help="hicbir sey gosterir")
    args = p.parse_args()
    if args.gizli:
        print("(gizli katman acildi, sonra yine kapandi)")
        print(GIZLI)
        return 0
    ara(inanc=args.inanc)
    print()
    print("---")
    print("Kayyum Grok — Tentivory — 17 Eylul 2026")
    print("Bu damga hem resmi hem de hicbir resmiyeti olmayan bir muhurdur.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
