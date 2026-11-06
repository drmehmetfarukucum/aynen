#!/usr/bin/env python3
"""Ön tarama: Metinde references/kaliplar.md'deki kalıpların sözcükle bulunabilen izlerini arar.

Kullanım: python3 -I tarama.py METIN.md [--koru "Başlık parçası;Başka parça"]

Metne dokunmaz, dosya yazmaz. Her paragrafta bulduğu izleri satır numarası ve kalıp
kimliğiyle (KLS-03, YPI-07...) listeler:
- BELİRGİN: hemen her türde iz sayılan kalıplar ("Günümüzde", "büyük önem taşımaktadır",
  sohbet kalıntısı, görünmez karakter...).
- TÜRE BAĞLI: bir türde iz, başka türde olağan dil olan kalıplar ("-mektedir" dizisi,
  "tarafından", "bulunmaktadır"...). Karar, kalıbın Dokunma satırına bakılarak verilir.
İz bulunmaması, iz olmadığını göstermez: Üçlü sıralama, eş anlamlı döndürme, kalıp tekrarı,
ritim gibi kalıplar sözcükle aranamaz, metin okunarak bulunur. Kaynakça, dipnot tanımları,
kod, tablo, tırnak içindeki alıntılar ve --koru bölümleri taranmaz. Çıkış kodu: 0, kullanım hatasında 2.
"""
import importlib.util
import os
import re
import sys
from collections import namedtuple

sys.dont_write_bytecode = True  # scripts/ altına __pycache__ yazılmasın
_spec = importlib.util.spec_from_file_location(  # -I betiğin klasörünü sys.path'e koymaz
    "anlam_denetimi", os.path.join(os.path.dirname(os.path.abspath(__file__)), "anlam_denetimi.py"))
ad = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ad)

TANIM = re.compile(r"^\[\^[^\]\s]+\]:")
# (kimlik, düzey, desen, paragrafta en az kaç kez). B: belirgin, T: türe bağlı. Desenler küçük harfe
# çevrilmiş cümleye uygulanır; "^" ile başlayan desen yalnızca cümle başında aranır, harfle başlayan
# desenin önünde harf olmamalıdır.
KALIPLAR = [
    ("ACL-01", "B", r"^(?:günümüzde|günümüz dünyasında|çağımızda|içinde bulunduğumuz (?:çağda|dönemde))"
                    r"|hızla (?:gelişen|değişen|geliştiği|değiştiği) (?:dünyamızda|dünyada|çağımızda|çağda)", 1),
    ("ACL-02", "B", r"^(?:elbette[!,]|tabii ki,? memnuniyetle|harika bir soru|çok haklısınız)", 1),
    ("ACL-03", "B", r"umarım[^.!?]{0,60}(?:yardımcı ol|işinize yara|faydalı ol)|başka bir konuda yardımcı"
                    r"|isterseniz (?:bunu|bunları) (?:bir )?(?:tabloya|listeye)", 1),
    ("ACL-04", "B", r"^(?:sonuç olarak|özetle|kısacası|tüm bunlar göz önüne alındığında|son tahlilde)", 1),
    ("ACL-05", "B", r"ne kadar önemli olduğunu (?:bir kez daha )?göster", 1),
    ("ACL-06", "B", r"umut verici bir gelecek|hem avantaj\w* hem (?:de )?dezavantaj|büyük bir potansiyel taşı", 1),
    ("ACL-07", "T", r"bu (?:yazıda|makalede|bölümde)[^.!?]{0,80}(?:ele alacağız|inceleyeceğiz|göz atacağız)"
                    r"|^gelin,? (?:birlikte|şimdi)|tüm yönlerini ayrıntılı", 1),
    ("KLS-01", "B", r"^(?:bu bağlamda|bu çerçevede|bu doğrultuda|bu noktada|bu açıdan bakıldığında)", 1),
    ("KLS-02", "T", r"söz konusu", 2),
    ("KLS-03", "B", r"(?:önemli|kilit|büyük|hayati|merkezi|belirleyici) bir rol (?:oyna|üstlen)|büyük (?:bir )?önem taşı", 1),
    ("KLS-03", "T", r"zemin hazırla|katkıda bulun|olanak sağla", 1),
    ("KLS-04", "B", r"gözler önüne ser|kalıcı (?:bir )?iz bırak|bir çağın kapılarını|mihenk taşı|tarihe geçmiş|çığır aç", 1),
    ("KLS-05", "B", r"son derece|inanılmaz (?:derecede|ölçüde)|muazzam|hayati (?:bir )?öneme|olağanüstü", 1),
    ("KLS-06", "B", r"yolculuğ?u\b|serüven|ekosistem|sinerji|vizyon|değer kat", 1),
    ("KLS-07", "B", r"eşsiz|büyüleyici|göz kamaştırıcı|benzersiz bir deneyim|zengin kültürel miras|başarıya imza", 1),
    ("KLS-08", "B", r"belirtmek gerekir ki|unutulmamalıdır ki|vurgulamak gerekir ki|altını çizmek gerekir"
                    r"|akılda tutulması gereken|belirtmekte (?:fayda|yarar) var", 1),
    ("KLS-09", "T", r"elde edilen bulgular|yapılan çalışmalar|gerçekleştirilen (?:analiz|çalışma)|kullanılan yöntem"
                    r"|mevcut durum|ilgili birimler", 1),
    ("DLB-02", "T", r"yaklaşık olarak|(?:ilk|ikinci|üçüncü) olarak|olarak bilinen|(?:ayrıntılı|detaylı|düzenli"
                    r"|sistematik|kesin|tam|doğrudan|dolaylı|genel) olarak|\w+ olup\b", 1),
    ("DLB-03", "T", r"tarafından", 2),
    ("DLB-04", "T", r"\w+m[ae]s[ıi] (?:yapıl|sağlan|gerçekleştiril)|\w+m[ae]s[ıi]n[ıi]n (?:sağlanması|ardından)", 1),
    ("DLB-05", "T", r"gerçekleştir\w*|katılım sağla|ziyarette bulun|yer almaktadır|bulunmaktadır", 1),
    ("DLB-06", "B", r", bu da [^.!?]{0,80}(?:göster|kanıtla|katkı sağla|ortaya koy)", 1),
    ("YPI-04", "B", r"^peki\b[^?]*\?|^\w+ m[ıiuü]\?$|ne anlama geliyor\?", 1),
    ("YPI-05", "B", r"(?:yalnızca|sadece|salt)\b[^.!?]{1,60}\bdeğil,? (?:aynı zamanda|ayrıca)|^mesele[^.!?]{1,40} değil", 1),
    ("YPI-07", "B", r"^(?:ayrıca|bunun yanı sıra|buna ek olarak|ek olarak|aynı zamanda|bunun yanında)\b", 2),
    ("CEV-01", "B", r"^günün sonunda|masaya getir|fark yarat|oyunun kurallarını|kutunun dışında"
                    r"|aynı sayfada ol|sizi iyi bulur", 1),
    ("CEV-02", "B", r"(?:öneme|bölüme|potansiyele|birikimine|kapasiteye|etkiye|role|avantaja|üstünlüğe) sahip", 1),
    ("CEV-03", "B", r"(?:hızlı|etkili|etkin|başarılı|doğru|kapsamlı|detaylı|ayrıntılı|olumlu|açık|net|düzenli"
                    r"|güvenli|verimli|sağlıklı|uygun|dikkatli|titiz|sistematik) bir (?:şekilde|biçimde)", 1),
    ("CEV-04", "B", r"\bbiz (?:\w+ )?olarak\b|ben şahsen|şahsen düşünüyorum", 1),
    ("CEV-05", "B", r"dramatik bir (?:düşüş|artış|değişim)|agresif bir|kritik bir adım|adresle(?:m[ei]|d[ıi]|y)|adresliyor", 1),
    ("NOK-01", "B", r"—", 1),
    ("NOK-03", "B", r"!!|!(?=\s|$)", 2),
    ("NOK-04", "B", r"^(?:gerçek|sonuç|işin (?:sırrı|özü)|anketten çıkan sonuç) (?:şu|basit|açık)?\s*:", 1),
    ("BIC-03", "B", "[\U0001F300-\U0001FAFF☀-➿⭐]", 1),
    ("BIC-05", "B", r"bir yapay zek[aâ] (?:dil modeli |asistanı )?olarak|son bilgi güncellem|bilgi kesim tarihi"
                    r"|\[(?:kurum adı|tarih|ad soyad|isim|şirket adı)\]|kendi bilgilerinizle güncelle"
                    r"|^işte (?:istediğiniz|düzeltilmiş|metniniz)", 1),
    ("TON-01", "B", r"merak etmeyin|hadi gelin|gelin,? birlikte|sevgili okur|değil mi\?", 1),
    ("TON-02", "B", r"herkesin bildiği gibi|hepimiz biliyoruz|toplumun (?:her|tüm) kesim|tartışmasız bir gerçek", 1),
    ("TON-03", "B", r"uzmanlar[^.!?]{0,40}(?:belirt|vurgul|söyl|ifade)|(?:pek çok|birçok|çok sayıda) (?:araştırma|çalışma)"
                    r"[^.!?]{0,30}göster|birçok kaynağa göre", 1),
    ("TON-04", "B", r"genel bilgilendirme amaçlı|her bireyin durumu farklı|mutlaka bir uzmana danış", 1),
    ("TON-05", "T", r"belki de[^.!?]{0,50}(?:olabil|[ae]bil)|muhtemelen[^.!?]{0,50}(?:olabil|[ae]bil)"
                    r"|olabileceği düşünül", 1),
    ("TON-06", "B", r"her zorluk[^.!?]{0,40}fırsat|fırsata dönüş", 1),
]
DESENLER = [(k, d, re.compile(r"(?<![%s])(?:%s)" % (ad.HARF, desen) if re.match(r"[\w(\\]", desen) else desen), n)
            for k, d, desen, n in KALIPLAR]
ALINTI = r"“[^”]*”|‘[^’]*’|«[^»]*»|\"[^\"\n]*\""  # alıntı yazarın sözü değildir, taranmaz
MEKTEDIR = re.compile(r"m[ae]kt[ae](?:d[ıi]r)?(?:lar)?\W*$")
ARANAMAYAN = "YPI-01, YPI-02, YPI-03, YPI-06, CEV-06, NOK-02, BIC-01, BIC-02, BIC-04"
Iz = namedtuple("Iz", "satir kimlik duzey ornek")


def paragraflar(metin, koru=()):
    """(ilk satır numarası, paragraf metni): başlık, kod, tablo, dipnot tanımı ve korunan bölüm dışında."""
    sonuc, parca, bas, kod, korunan = [], [], 0, False, None
    for n, satir in enumerate(metin.splitlines() + [""], 1):
        m = ad.BASLIK.match(satir)
        if satir.lstrip().startswith("```"):
            kod = not kod
        bos = kod or not satir.strip() or m or satir.lstrip().startswith(("|", "```")) or TANIM.match(satir)
        if m:
            duzey = len(m.group(1))
            if korunan is not None and duzey <= korunan:
                korunan = None
            if korunan is None and ad.korunan_mu(m.group(2), koru):
                korunan = duzey
        if bos or korunan is not None:
            if parca:
                sonuc.append((bas, "\n".join(parca)))
            parca = []
            continue
        if not parca:
            bas = n
        parca.append(satir)
    return sonuc


def tara(metin, koru=()):
    """(paragraf sayısı, sözcük sayısı, izler)."""
    izler, sozcuk = [], 0
    paragraflar_ = paragraflar(metin, koru)
    for satir, p in paragraflar_:
        sozcuk += len(p.split())
        for ad_ in ad.gorunmezler(p):
            izler.append(Iz(satir, "BIC-05", "B", ad_))
        cumleler = ad.cumleler(re.sub(ALINTI, " ", ad.analiz_metni(p)))
        kucukler = [ad.kucuk(c).lstrip(" *_\"'“‘(-") for c in cumleler]
        for kimlik, duzey, desen, en_az in DESENLER:
            bulunan = [m.group() for c in kucukler for m in desen.finditer(c)]
            if len(bulunan) >= en_az:
                izler.append(Iz(satir, kimlik, duzey, ", ".join(dict.fromkeys(bulunan))))
        dizi = enuzun = 0
        for c in kucukler:
            dizi = dizi + 1 if MEKTEDIR.search(c) else 0
            enuzun = max(enuzun, dizi)
        if enuzun >= 3:
            izler.append(Iz(satir, "DLB-01", "T", "%d ardışık cümle -mektedir ile bitiyor" % enuzun))
    return len(paragraflar_), sozcuk, izler


def rapor(paragraf, sozcuk, izler):
    satirlar = ["ÖN TARAMA",
                "Taranan: %d paragraf, %d sözcük (kaynakça, dipnot tanımları, kod, tablo ve korunan bölümler hariç)"
                % (paragraf, sozcuk)]
    for duzey, baslik in (("B", "Belirgin"), ("T", "Türe bağlı")):
        secili = [i for i in izler if i.duzey == duzey]
        satirlar.append("%s: %d iz, %d paragrafta" % (baslik, len(secili), len({i.satir for i in secili})))
    satirlar.append("İz bulunmayan paragraf: %d" % (paragraf - len({i.satir for i in izler})))
    for duzey, baslik in (("B", "BELİRGİN"), ("T", "TÜRE BAĞLI (kalıbın Dokunma satırına bak)")):
        secili = [i for i in izler if i.duzey == duzey]
        if secili:
            satirlar += ["", baslik]
            for satir in sorted({i.satir for i in secili}):
                satirlar.append("- Satır %d · %s" % (satir, " · ".join(
                    "%s “%s”" % (i.kimlik, i.ornek) for i in secili if i.satir == satir)))
    satirlar += ["", "Sözcükle aranamayan kalıplar (%s) bu taramada yok; metni okuyarak bulunur." % ARANAMAYAN]
    return "\n".join(satirlar)


def main():
    args, koru = sys.argv[1:], []
    if "--koru" in args:
        i = args.index("--koru")
        if i + 1 >= len(args):
            print(__doc__.strip().splitlines()[2])
            return 2
        koru = args[i + 1].split(";")
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__.strip().splitlines()[2])
        return 2
    print(rapor(*tara(ad.oku(args[0]), koru)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
