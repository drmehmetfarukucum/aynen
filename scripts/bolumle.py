#!/usr/bin/env python3
"""Bölüm planı: Markdown belgesinin başlıklarını ve önerilen çalışma parçalarını yazdırır.

Kullanım: python3 -I bolumle.py BELGE.md [--koru "Başlık parçası;Başka parça"]

Belgeye dokunmaz. Her başlık için kendi satır aralığını (alt başlığa kadar), ana metindeki
sözcük sayısını, dipnot işareti sayısını ve korunup korunmadığını yazar; dipnot tanımları
([^id]: ...) ana metin sayılmaz. Korunan bölümler anlam_denetimi.py ile aynı kuralla
seçilir (Kaynakça, Kaynaklar, References, Bibliography ya da --koru parçası; alt
başlıklarıyla birlikte). Çalışma parçaları korunmayan başlıklardan, başlık sınırında
bölünerek, en çok 1.500 sözcük olacak biçimde toplanır. Çıkış kodu: 0, kullanım hatasında 2.
"""
import importlib.util
import os
import re
import sys

sys.dont_write_bytecode = True  # scripts/ altına __pycache__ yazılmasın
_spec = importlib.util.spec_from_file_location(  # -I betiğin klasörünü sys.path'e koymaz
    "anlam_denetimi", os.path.join(os.path.dirname(os.path.abspath(__file__)), "anlam_denetimi.py"))
ad = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ad)

SINIR = 1500
TANIM = re.compile(r"^\[\^[^\]\s]+\]:")  # shortcut: girintili devam satırı olan çok paragraflı dipnot tanımı ana metin sayılır


def bloklar(metin, koru):
    """Her başlığın kendi bloğu: (ilk satır, son satır, başlık satırı, sözcük, dipnot, korunan)."""
    satirlar = metin.splitlines()
    bas = [i for i, s in enumerate(satirlar) if ad.BASLIK.match(s)]
    if not bas or (bas[0] > 0 and any(s.strip() for s in satirlar[:bas[0]])):
        bas.insert(0, 0)  # ilk başlıktan önceki metin
    ust, sonuc = [], []  # ust: açık üst başlıkların (düzey, korunan) yığını
    for n, i in enumerate(bas):
        son = bas[n + 1] if n + 1 < len(bas) else len(satirlar)
        m = ad.BASLIK.match(satirlar[i])
        duzey = len(m.group(1)) if m else 7
        while ust and ust[-1][0] >= duzey:
            ust.pop()
        korunan = bool(m and ad.korunan_mu(m.group(2), koru)) or any(k for _, k in ust)
        ust.append((duzey, korunan))
        govde = "\n".join(s for s in satirlar[i:son] if not TANIM.match(s))
        sonuc.append((i + 1, son, satirlar[i].strip() if m else "(başlıksız giriş)",  # "##", "-" sözcük değil
                      len(re.findall(r"\S*\w\S*", re.sub(ad.DIPNOT, " ", govde))), len(re.findall(ad.DIPNOT, govde)),
                      korunan))
    return sonuc


def parcalar(bl, sinir):
    """Korunmayan ardışık blokları sınırı aşmadan toplar; korunan blok parçayı keser."""
    sonuc, cari = [], []
    for b in bl:
        if cari and (b[5] or sum(x[3] for x in cari) + b[3] > sinir):
            sonuc.append(cari)
            cari = []
        if not b[5]:
            cari.append(b)
    return sonuc + ([cari] if cari else [])


def plan(metin, koru=(), sinir=SINIR):
    bl = bloklar(metin, koru)
    satirlar = metin.splitlines()
    tanim = [i + 1 for i, s in enumerate(satirlar) if TANIM.match(s)]
    cikti = ["BÖLÜM PLANI",
             "Ana metin %d sözcük, %d dipnot işareti; %d dipnot tanımı%s (ana metin sayılmadı)" % (
                 sum(b[3] for b in bl), sum(b[4] for b in bl), len(tanim),
                 " satır %d–%d" % (tanim[0], tanim[-1]) if tanim else ""),
             "", "| Satırlar | Başlık | Sözcük | Dipnot | Korunan |", "|---|---|---|---|---|"]
    cikti += ["| %d–%d | %s | %d | %d | %s |" % (a, s, b.replace("|", "\\|"), w, d, "evet" if k else "")
              for a, s, b, w, d, k in bl]
    cikti += ["", "ÖNERİLEN ÇALIŞMA PARÇALARI (en çok %d sözcük, başlık sınırından)" % sinir]
    for n, p in enumerate(parcalar(bl, sinir), 1):
        w = sum(b[3] for b in p)
        cikti.append("P%d. satır %d–%d: %d sözcük, %d dipnot; %s%s" % (
            n, p[0][0], p[-1][1], w, sum(b[4] for b in p), p[0][2] + (" … " + p[-1][2] if len(p) > 1 else ""),
            " (SINIRI AŞIYOR: tek başlık, başlık içinde bölünmedi)" if w > sinir else ""))
    korunan = [b for b in bl if b[5]]
    cikti += ["", "KORUNAN (dokunmayın): " + ("; ".join("satır %d–%d %s" % (b[0], b[1], b[2]) for b in korunan)
                                               if korunan else "yok")]
    return "\n".join(cikti)


def main():
    secim = ad.secenekler(sys.argv[1:])
    if not secim or len(secim[0]) != 1 or secim[2]:
        print(__doc__.strip().splitlines()[2])
        return 2
    print(plan(ad.oku(secim[0][0]), secim[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
