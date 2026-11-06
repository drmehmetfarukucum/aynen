#!/usr/bin/env python3
"""anlam_denetimi.py için regresyon testi.

Kullanım: python3 -I tests/regresyon.py [BETIK.py] [-v]

vakalar.json'daki her kaynak/yeni çiftini betiğin denetle() işlevinden geçirir ve
çıkan düzeyi (KESİN > KONTROL > TEMİZ) beklenenle karşılaştırır: Düzey en az
"beklenen" olmalı, "en_cok" verilmişse onu aşmamalı. Yalnızca standart kitaplığı kullanır,
dosya yazmaz. Başka bir betik yolu verilirse onu sınar (eski sürümle karşılaştırmak
için). -v her vakanın uyarılarını da yazar. Çıkış kodu: geçme oranı %90 ve üstüyse 0.
Vakada "koru" varsa denetle()'ye --koru parçaları olarak, "terimler" varsa korunan terimler
olarak verilir. "fark_icerir" fark tablosunda, "plan_icerir" bolumle.py planında aranacak
metinlerdir (plan vakasında düzey denetlenmez). "tarama" vakasında tarama.py'nin kaynakta
bulması gereken kalıp kimlikleri verilir (tam olarak bunlar; boş liste hiç iz beklemez).
Ayrıca tarama.py'deki her kalıp kimliğinin references/kaliplar.md'de bulunduğu denetlenir.
"soru", hedefli sorularda geçmesi gereken türlerdir; boş liste hiç soru çıkmamasını bekler.
"""
import importlib.util
import json
import os
import sys

DUZEY = {"TEMİZ": 0, "KONTROL": 1, "KESİN": 2}
AD = {v: k for k, v in DUZEY.items()}
BURASI = os.path.dirname(os.path.abspath(__file__))


def yukle(yol):
    sys.dont_write_bytecode = True  # scripts/ altına __pycache__ yazılmasın
    spec = importlib.util.spec_from_file_location("anlam_denetimi", yol)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def main():
    ayrinti = "-v" in sys.argv
    yollar = [a for a in sys.argv[1:] if a != "-v"]
    betik = yollar[0] if yollar else os.path.join(BURASI, "..", "scripts", "anlam_denetimi.py")
    denetim = yukle(betik)
    with open(os.path.join(BURASI, "vakalar.json"), encoding="utf-8") as f:
        vakalar = json.load(f)

    bolumle_yolu = os.path.join(os.path.dirname(betik), "bolumle.py")
    bolumle = yukle(bolumle_yolu) if os.path.exists(bolumle_yolu) else None
    tarama_yolu = os.path.join(os.path.dirname(betik), "tarama.py")
    tarama = yukle(tarama_yolu) if os.path.exists(tarama_yolu) else None
    gecen = 0
    if tarama:
        with open(os.path.join(os.path.dirname(betik), "..", "references", "kaliplar.md"), encoding="utf-8") as f:
            kaliplar = f.read()
        eksik = sorted({k for k, _, _, _ in tarama.KALIPLAR if "### %s " % k not in kaliplar})
        vakalar.append({"id": "TARAMA-KIMLIK", "kimlik_eksik": eksik})
    for v in vakalar:
        if "kimlik_eksik" in v:
            gecen += not v["kimlik_eksik"]
            if v["kimlik_eksik"] or ayrinti:
                print("%s %-12s kaliplar.md'de olmayan kimlik: %s" % (
                    "✗ " if v["kimlik_eksik"] else "  ", v["id"], ", ".join(v["kimlik_eksik"]) or "yok"))
            continue
        if "tarama" in v:
            bulunan = sorted({i.kimlik for i in tarama.tara(v["kaynak"])[2]}) if tarama else None
            tamam = bulunan == sorted(set(v["tarama"]))
            gecen += tamam
            if not tamam or ayrinti:
                print("%s %-12s çıkan %s beklenen %s %s" % ("  " if tamam else "✗ ", v["id"], bulunan,
                                                          sorted(set(v["tarama"])), v.get("not", "")))
            continue
        koru = v["koru"].split(";") if "koru" in v else ()
        if "plan_icerir" in v:
            plan = bolumle.plan(v["kaynak"], koru, v.get("sinir", 1500)) if bolumle else "(bolumle.py yok)"
            tamam = all(p in plan for p in v["plan_icerir"])
            gecen += tamam
            if not tamam or ayrinti:
                print("%s %-12s %s\n%s" % ("  " if tamam else "✗ ", v["id"], v.get("not", ""), plan))
            continue
        try:
            terim = {"terimler": v["terimler"].split(";")} if "terimler" in v else {}
            kesin, kontrol, _ = denetim.denetle(v["kaynak"], v["yeni"], *([koru] if koru else []), **terim)
            fark = denetim.fark_tablosu(v["kaynak"], v["yeni"]) if "fark_icerir" in v else ""
            sorular = denetim.hedefli_sorular(v["kaynak"], v["yeni"]) if "soru" in v else []
        except (TypeError, AttributeError) as h:  # eski sürümde --koru, --terimler, --fark ya da soru yok: vaka geçmez
            kesin, kontrol, fark, sorular = [], ["(eski sürüm: %s)" % h], None, []
        duzey = 2 if kesin else 1 if kontrol else 0
        en_az, en_cok = DUZEY[v["beklenen"]], DUZEY[v.get("en_cok", "KESİN")]
        etiketler = " ".join(s.split("]")[0] for s in sorular)  # "[SIRA+ROL"
        tamam = fark is not None and en_az <= duzey <= en_cok and all(
            p in fark for p in v.get("fark_icerir", [])) and (
            "soru" not in v or (all(t in etiketler for t in v["soru"]) if v["soru"] else not sorular))
        gecen += tamam
        if not tamam or ayrinti:
            beklenen = v["beklenen"] + ("" if en_cok == 2 else " … " + v["en_cok"])
            print("%s %-12s çıkan %-7s beklenen %-16s %s" % (
                "  " if tamam else "✗ ", v["id"], AD[duzey], beklenen, v.get("not", "")))
            for s in kesin:
                print("      KESİN   " + s)
            for s in kontrol:
                print("      KONTROL " + s)
            for s in sorular:
                print("      SORU    " + s)
    oran = gecen / len(vakalar)
    print("\nGeçen: %d / %d (%%%d)" % (gecen, len(vakalar), round(100 * oran)))
    return 0 if oran >= 0.9 else 1


if __name__ == "__main__":
    sys.exit(main())
