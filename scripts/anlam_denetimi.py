#!/usr/bin/env python3
"""Anlam denetimi: kaynak metinle yeniden yazılmış metni karşılaştırır.

Kullanım: python3 -I anlam_denetimi.py KAYNAK.txt YENI.txt [--koru "Başlık parçası;Başka parça"] [--terimler "terim;başka terim" | DOSYA] [--fark]

Model çalıştırmaz, internete çıkmaz, dosya yazmaz. İki metni okur ve korunması
gereken öğelerdeki farkları listeler:
- KESİN: sayının değeri, işleci, işareti, ölçü birimi ya da niteleyicisi (yaklaşık, en az,
  en fazla, en geç...); tablo satırı, kod, bağlantı ve DOI, alıntı, blok alıntı ve kaynak
  gösterimi; cümle içindeki özel adlar ve kısaltmalar; kaynakta hiç yokken giren birinci kişi;
  dipnot işareti ve metni; hukuki atıf (m. 99/5, § 218a, Art. 8, 5237 sayılı Kanun, RG, E./K.,
  birinci cümle...); korunan bölüm (başlığı Kaynakça, Kaynaklar, References, Bibliography olan
  ya da --koru parçalarından birini taşıyan bölüm birebir kalır); --terimler ile verilen
  terimlerden yeni metinde eksilen; kaynakta olmayan görünmez karakter ya da sohbet arayüzünden
  kalan kaynak işareti.
- KONTROL (numaralı): yalnızca yazılışı ya da sırası değişen sayılar; cümle
  eşlemesiyle bulunan, anlam sözlerindeki farklar (olumsuzluk, temkin, kapsam, kip,
  zaman, koşul, karşıolgusal koşul, neden-sonuç, görüşün sahibi, karar türü,
  tarama sınırı...); kayan odak sözü; ters dönen olay sırası (-dıktan sonra,
  -madan önce, -ınca, önce / sonra / ardından); adlar arasında yer değiştiren
  hâl ekleri; düşmüş görünen cümleler; yeni metinde daha sık geçen korunan terim;
  kaynaktan yeni metne geçen görünmez karakter ya da sohbet işareti.
- HEDEFLİ SORULAR (S): betiğin kesin yakalayamadığı kaymalar (sıra, rol, sayıdan uzaklaşan
  niteleyici, "en az bir" gibi sınır) için eşlenen ve değişen cümle çiftine sorulacak soru.
  Hüküm değildir, çıkış kodunu etkilemez.
--fark, raporun sonuna eşlenen ve değişen cümlelerin Markdown tablosunu ekler.
--terimler korunacak terimleri alır: ";" ile ayrılmış liste ya da her satırında bir terim
bulunan dosya (# ile başlayan satırlar yorumdur). Ekli biçimler de sayılır ("spirometriyle"),
büyük/küçük harf ayrılmaz. Görünmez karakterler (sıfır genişlikli boşluk, yumuşak tire...)
ve sohbet işaretleri ("【4†source】") karşılaştırmadan önce atılır; yalnızca bildirilir.

Sözcük sayımı kaba bir süzgeçtir: Kaymayı kanıtlamaz, nereye bakılacağını
gösterir. Çıkış kodu: 0 = kesin sorun yok, 1 = kesin sorun var, 2 = kullanım hatası.
"""
import difflib
import re
import sys
import unicodedata
from collections import Counter, namedtuple
from decimal import Decimal
from functools import lru_cache

HARF = "A-Za-zÇĞİÖŞÜÂÎÛçğıöşüâîû"

# Sayıdan sonra gelince ölçü birimi sayılan sözler. Sözcük birimleri ek alabilir.
SEMBOL_BIRIM = {
    "%", "‰", "mg", "g", "kg", "µg", "μg", "mcg", "ng", "pg", "ml", "l", "cl", "dl",
    "cm", "mm", "m", "km", "µm", "μm", "nm", "°c", "°", "db", "dba", "hz", "khz",
    "ppm", "mmhg", "iu", "u", "mmol", "meq", "tl", "usd", "eur", "kcal", "kj", "w",
    "kw", "v", "msv", "gy", "bq", "lux", "lx", "x",
}
SOZCUK_BIRIM = sorted([
    "saat", "gün", "hafta", "ay", "yıl", "dakika", "saniye", "kez", "kat",
    "kişi", "işçi", "çalışan", "katılımcı", "hasta", "birey", "olgu", "vaka",
    "adet", "istasyon", "lira", "dolar", "avro", "euro", "doz", "tablet",
    "ampul", "puan", "gece", "vardiya", "metre", "litre", "gram", "derece",
    "yaş", "personel", "işyeri", "kaza", "örnek", "madde", "fıkra", "sayılı",
    "sınıf", "okul", "şube", "ilçe", "il",
], key=len, reverse=True)
# Aynı birimin başka yazılışları ("5 dk" = "5 dakika", "₺" = "TL").
BIRIM_ES = {"dk": "dakika", "dak": "dakika", "sa": "saat", "sn": "saniye", "₺": "tl",
            "lira": "tl", "try": "tl", "$": "usd", "dolar": "usd", "€": "eur",
            "avro": "eur", "euro": "eur", "yüzde": "%"}
# Değişmesi değeri değiştiren birimler (sözcük birimlerinden yalnızca ölçü olanlar).
OLCU = SEMBOL_BIRIM | {"dakika", "saniye", "saat", "gün", "hafta", "ay", "yıl", "metre",
                       "litre", "gram", "derece", "kez", "kat", "doz", "tablet", "ampul"}

# Yazıyla sayılar. BELIRSIZ olanlar ("bir", "on", "yüz") tek başına ve eksiz yazılınca
# yalnızca rakamla yazılmış aynı değeri karşılamak için kullanılır, kendi başına uyarı vermez.
SOZ_DEGER = {
    "bir": 1, "iki": 2, "üç": 3, "dört": 4, "dörd": 4, "beş": 5, "altı": 6, "yedi": 7,
    "sekiz": 8, "dokuz": 9, "on": 10, "yirmi": 20, "otuz": 30, "kırk": 40, "elli": 50,
    "altmış": 60, "yetmiş": 70, "seksen": 80, "doksan": 90, "yüz": 100, "bin": 1000,
    "milyon": 10 ** 6, "milyar": 10 ** 9, "buçuk": Decimal("0.5"),
}
BELIRSIZ = {"bir", "on", "altı", "yüz", "bin", "milyon", "milyar", "buçuk"}
SAYI_DEGIL = ("üçgen", "dörtgen", "beşgen", "beşik", "sekizgen", "ikiz", "ikindi", "yedir")
SOZ_KOKLERI = sorted(SOZ_DEGER, key=len, reverse=True)

AY_GUN = [
    "ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos",
    "eylül", "ekim", "kasım", "aralık", "pazartesi", "salı", "çarşamba",
    "perşembe", "cuma", "cumartesi", "pazar",
]

# -dık / -dım (biz / ben geçmiş): ünlüden sonra hep "d" gelir, böylece "kritik, pratik" elenir.
DIK = (r"(?!(?:artık|fındık|sandık|tanıdık|bildik|düdük|alışıldık|gıdık|optik|taktik)(?![%s])"
       r"|\w*stik(?![%s]))\w*(?:[aeıioöuü]d|[çfhkpsşt]t|[bcdgğjlmnrvyz]d)[ıiuü]k" % (HARF, HARF))
DIM = (r"(?!(?:yardım|tadım|kadim|yudum)(?![%s]))"
       r"\w+(?:[aeıioöuü]d|[çfhkpsşt]t|[bcdgğjlmnrvyz]d)[ıiuü]m" % HARF)
FIIL_OLUMSUZ = (
    r"(?!(?:inanılmaz|ayrılmaz|vazgeçilmez|unutulmaz|yılmaz|namaz)(?![%s]))"
    r"\w+(?:m[ıiuü]yor|maz|mez|mazs|mezs|mazk|mezk|madı|medi|madığ|mediğ"
    r"|mamış|memiş|mayacak|meyecek|mamal|memel|mamak|memek|madan|meden"
    r"|mayan|meyen|mayıp|meyip|maksızın|meksizin|mayın|meyin)\w*" % HARF)

# Her sınıf bir desen listesidir ve karşılaştırma desen başına yapılır: Aynı desene uyan
# biçimler birbirinin yerine geçebilir ("olabilir" / "olası"), ayrı desenler geçemez
# ("tüm" / "bazı", "önce" / "sonra"). Desenler küçük harfe çevrilmiş metne uygulanır.
IMLER = [
    ("Olumsuzluk", ["|".join([
        r"değil\w*", r"yok\w*", r"hiç", r"hiçbir\w*", r"asla", r"kimse\w*",
        r"ne\s[^.!?;\n]{1,80}?\sne", FIIL_OLUMSUZ,
        r"\w+m[ae]s[ıi]n(?:l[ae]r)?", r"\w+m[ae](?=\s*!)",
    ])]),
    ("Temkin / olasılık", [
        r"(?!kabil|mobil|otomobil)\w+[ae]bil\w*|muhtemel\w*|olası\w*|belki\w*|galiba"
        r"|herhalde|sanırım|tahmin\w*|şüphel\w*|kuşkul\w*",
        r"yaklaşık|civar\w*",
        r"kısmen|görece\w*|nispeten",
        r"düşündür\w*|işaret\w*|öngör\w*",
    ]),
    ("Kesinlik / derece", [
        r"kesin\w*|mutlaka|kuşkusuz|şüphesiz|açıkça|kanıtla\w*|ispat\w*",
        r"tamamen|tümüyle|büsbütün",
        r"büyük ölçüde|önemli ölçüde|belirgin\w*|anlamlı\w*|ciddi\w*|son derece|oldukça|çok|pek",
        r"hafif\w*|biraz",
    ]),
    ("Sıklık", [
        r"daima|her zaman|sürekli|hep", r"hiçbir zaman",
        r"genellikle|genelde|sıklıkla|çoğu zaman|çoğunlukla",
        r"bazen|ara sıra|zaman zaman", r"nadiren",
    ]),
    ("Kapsam / niceleyici", [
        r"tüm\w*|bütün\w*|her(?! zaman)|hepsi\w*|herkes\w*",
        r"bazı\w*|birçok\w*|çoğu(?! zaman)\w*|birkaç\w*|az sayıda|çok sayıda",
        r"yalnızca|sadece|yalnız", r"bile|dahi",
        r"en az|en çok|en fazla", r"neredeyse|hemen hemen",
    ]),
    ("Zorunluluk / öneri", [
        r"zorunlu\w*|gerek(?!çe)\w*|şart\w*|mecbur\w*|yükümlü\w*|zorunda\w*"
        r"|(?!elmalı)\w+m[ae]l[ıi](?:y[ıi]m|s[ıi]n|y[ıi]z|s[ıi]n[ıi]z|l[ae]r|d[ıi]r|d[ıi]|yd[ıi])?",
        r"yasak\w*", r"öner\w*|tavsiye\w*", r"izin\w*",
    ]),
    ("Koşul / istisna", [
        r"(?!neredeyse)\w+(?:[aeıioöuü]r|m[ae]z|y)s[ae](?:m|n|k|n[ıi]z|l[ae]r)?|\w+s[ae]yd[ıi]\w*|takdirde"
        r"|sürece|hâlinde|halinde|kaydıyla|şartıyla|eğer|şayet|\w+m[ae]d[ıi]kç[ae]",
        r"hariç\w*|dışında\w*|istisna\w*|muaf\w*", r"aksi\w*", r"ancak|fakat|lakin",
    ]),
    # Gerçekleşmemiş koşul ve sonucu: "ayrılsaydı … alınabilirdi" → "ayrılırsa … alınabilir".
    ("Karşıolgusal koşul (-saydı)", [r"\w+s[ae]yd[ıi](?:m|n|k|n[ıi]z|l[ae]r)?"]),
    ("Karşıolgusal sonuç (-ardı, -abilirdi)", [  # geçmiş zamanlı "gösterdi", "önerdi", "standardı" sayılmaz
        r"(?!(?:göster|öner|standar)d)\w{2,}(?:[ae]|(?<![dt])[ıiuü])r(?:l[ae]r)?d[ıiuü]"
        r"(?:m|k|n[ıiuü]z|l[ae]r)?"]),
    ("Bağlaç (veya / ya da)", [r"(?<!/)veya|ya da|yahut", r"ve/veya"]),
    # İki parçalı bağlaçlar: "hem … hem" ikisi, "ya … ya" biri, "ne … ne" hiçbiri (Olumsuzluk da sayar).
    ("Bağlaç çifti (hem … hem, ya … ya, ister … ister, ne … ne)", [
        r"hem\s[^.!?;\n]{1,80}?\shem", r"ya\s(?!da\s)[^.!?;\n]{1,80}?\sya",
        r"ister\s[^.!?;\n]{1,80}?\sister", r"ne\s[^.!?;\n]{1,80}?\sne"]),
    ("Soru", [r"\?|m[ıiuü](?:s[ıiuü]n(?:[ıiuü]z)?|y[ıiuü][mz]|d[ıiuü]r|yd[ıiuü])?"]),
    ("Neden-sonuç", ["|".join([
        r"çünkü", r"zira", r"nedeniyle", r"sebebiyle", r"yüzünden", r"dolayı\w*",
        r"bu yüzden", r"bu nedenle", r"sonucunda", r"sayesinde",
        r"\w+[dt][ıiuü]ğ[ıiuü](?:m[ıiuü]z|n[ıiuü]z|m|n)? için",
        r"\w+[dt][ıiuü]ğ[ıiuü](?:m[ıiuü]z|n[ıiuü]z|m|n)d[ae]n",
        r"yol aç\w*", r"neden ol\w*", r"sebep ol\w*", r"etki(?:le|liyo)\w*", r"katkı\w*",
    ])]),
    ("İlişki (nedensellik değil)", [
        r"ilişki(?!n(?![%s]))\w*|bağlantılı\w*|korelasyon\w*|birliktelik\w*" % HARF,
    ]),
    ("Zaman / sıra", [
        r"henüz", r"hâlâ|hala", r"artık", r"önce(?!l)\w*", r"sonra\w*|ardından", r"kadar",
        r"itibaren", r"boyunca", r"en geç", r"en erken", r"derhâl|derhal",
        r"\w+(?:[ae]r|[ıiuü]r|m[ae]z|m[ıiuü]ş|yor|y)ken", r"\w+[dt][ıiuü]kt[ae]n",
        r"\w+m[ae]d[ae]n", r"\w+[dt][ıiuü]kç[ae]",
        r"\w+[dt][ıiuü]ğ[ıiuü](?:m[ıiuü]z|n[ıiuü]z|m|n)d[ae]",
        r"\w+[ae]c[ae](?:k|ğ[ıi][mz]|ks[ıi]n(?:[ıi]z)?|kl[ae]r|kt[ıi]r?)",
        r"\w+m[ıiuü]şt[ıiuü](?!r)\w*", r"\w+m[ıiuü]ş[ıiuü][mz]",  # -mıştır aşağıda toplu sayılır
    ]),
    ("Aktarım / kaynak", [
        r"göre|iddia\w*|aktar\w*|bildiril\w*|söylen\w*|belirtil\w*|rivayet\w*",
    ]),
    ("Duyulan geçmiş (-mış)", [r"\w+m[ıiuü]ş(?:lar|ler|sa|se|ken)?(?!\s+(?:ol|gibi)|,)"]),
    ("Benzetme (sanki / gibi)", [r"sanki|gibi"]),
    ("Kişi (biz / ben)", [
        "|".join([r"bizim\w*", r"biz(?:e|i|ce|den|le)", r"\w+yoruz",
                  r"\w+(?:mekteyiz|maktayız)", r"\w+(?:acağız|eceğiz)", DIK]),
        "|".join([r"benim\w*", r"ben(?:i|ce|den)", r"bana", r"\w+yorum",
                  r"\w+(?:mekteyim|maktayım)", r"\w+(?:acağım|eceğim)", DIM]),
    ]),
    ("Alan terimleri", [
        r"işçi(?!lik|liğ)\w*", r"çalışan\w*", r"iş kazas\w*", r"meslek hastalı[kğ]\w*",
        r"insidans\w*", r"prevalans\w*", r"yaygınlı\w*", r"sıklı\w*", r"risk\w*",
        r"olasılı\w*", r"ortalama\w*", r"ortanca\w*", r"medyan\w*",
        r"tanı\w*", r"tedavi\w*", r"doz\w*", r"semptom\w*", r"belirti\w*",
    ]),
    ("Karşılaştırma / yön", [
        r"yüksek\w*|fazla\w*|artt\w*|artış\w*|artır\w*|artar\w*|artma\w*|yüksel\w*",
        r"düşük\w*|az|azal\w*|düştü\w*|düşüş\w*|düşer\w*|geriledi\w*",
        r"oranla|kıyasla",
    ]),
    # Hukuk metni: görüşü kime bağladığı, kararın türü ve taramanın sınırı.
    ("Görüşün sahibi", [
        r"kanaatimizce|kanımızca|bize göre", r"öğreti(?!m|ci)\w*", r"ağırlıklı görüş\w*",
        r"genel kabul\w*", r"karşı görüş\w*", r"savunul\w*", r"yargıtay\w*", r"daire\w*",
        r"başsavcılı\w*", r"aym|anayasa mahkemes\w*", r"aihm|avrupa insan hakları mahkemes\w*",
        r"ceza genel kurul\w*|cgk", r"kabul e[dt]\w*",
    ]),
    ("Karar türü", [
        r"kanun yararına boz\w*", r"bozma\w*|bozmuş\w*|bozdu\w*|bozan\w*",
        r"onama\w*|onamış\w*|onan\w*|onadı\w*", r"esas hük(?:üm|m)\w*", r"istem\w*",
        r"diren(?:me|il|di|miş)\w*",
    ]),
    ("Tarama sınırı", [
        r"rastlan\w*|bulunama\w*", r"incelenen\s[^.!?;\n]{0,80}?arasında", r"bu tarama\w*",
        r"ilk kez|ilk defa",
    ]),
]
IMLER_RE = [(ad, [re.compile(r"(?<![%s])(?:%s)(?![%s])" % (HARF, d, HARF)) for d in desenler])
            for ad, desenler in IMLER]
MUTLAK = ["her zaman", "sürekli", "daima", "asla", "hiçbir zaman", "tamamen"]
# Yapay zekâ metninde sık görülen, silinmesi beklenen cümle başı dolguları (ad değildir).
DOLGU = {"Günümüzde", "Sonuç", "Özetle", "Kısacası", "Ayrıca", "Dolayısıyla", "Böylece",
         "Elbette", "Harika", "Umarım", "Öncelikle", "Nitekim", "Peki"}
ODAK_SONRA, ODAK_ONCE = ("sadece", "yalnızca", "yalnız"), ("bile", "dahi")

BAGLANTI = r"https?://[^\s)>\]]+|www\.[^\s)>\]]+|[\w.+-]+@[\w-]+\.[\w.]+|(?<![\w/.])10\.\d{4,9}/[^\s\"<>]+"
# Görünmez karakterler: Unicode biçim karakterleri (sıfır genişlikli boşluk ve birleştiriciler, yumuşak
# tire, BOM, yön işaretleri, etiket karakterleri) ve özel kullanım alanı. Sohbet arayüzünden kopyalanan
# metinde kalır; sayıyı ya da sözcüğü bölerek denetimi yanıltabilir.
GORUNMEZ_AD = {"\u200b": "sıfır genişlikli boşluk", "\u200c": "sıfır genişlikli ayırıcı",
               "\u200d": "sıfır genişlikli birleştirici", "\u2060": "sözcük birleştirici",
               "\ufeff": "BOM", "\u00ad": "yumuşak tire"}
SOHBET_IZI = (r"【[^】\n]{0,80}】|\b(?:cite|filecite|navlist)?turn\d+(?:search|news|view|file|fetch|image)\d+\b"
              r"|:?contentReference\[oaicite:\d+\](?:\{index=\d+\})?")
KOD_BLOGU = r"(?ms)^[ \t]*```.*?^[ \t]*```"
# tur: 0 rakam, 1 sayı sözü, 2 belirsiz söz. bicim: boşluksuz yazılış, sözcük birimi yalın hâliyle.
# nitel: sayıya bağlı niteleyicinin grubu (NITELEYICI), yoksa boş.
Sayi = namedtuple("Sayi", "yer deger islec birim yazi bicim tur nitel", defaults=("",))
# Sayının hemen önündeki ya da ardındaki niteleyici (ardında araya en çok bir sözcük girebilir):
# (grup, önde, arkada). Aynı gruptakiler birbirinin yerine geçer ("yaklaşık 100" = "100 civarında").
# "üzerinde / altında" ilgi ekiyle sınırdır ("10 hasta üzerinde" sınır değil).
# shortcut: "1 yıla kadar" da yaklaşık sayılır, çünkü "-e kadar" ile yalın "hafta kadar" ek
# çözümlemesi yapılmadan ayrılamaz; üst sınır gerekirse birim gövdesiyle ayırın.
NITELEYICI = [
    ("yaklaşık", r"yaklaşık|aşağı yukarı|[~≈]", r"civarında|kadar|(?<=[ae]\s)yakın"),
    ("alt sınır", r"en az|asgari", r"(?<=[dt][ae]n\s)fazla|(?<=n\s)üzerinde|(?<=[ıiuü]\s)(?:aşkın|geçkin)"),
    ("üst sınır", r"en fazla|en çok|azami", r"(?<=[dt][ae]n\s)az|(?<=n\s)altında"),
    ("süre sınırı", r"en geç|en erken", None),
]


def kucuk(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def oku(yol):
    with open(yol, encoding="utf-8") as f:
        return unicodedata.normalize("NFC", f.read())


def sade(s):
    return re.sub(r"\s+", " ", s).strip()


def alintisiz(metin):
    """Blok alıntının ">" önekini atar."""
    return re.sub(r"(?m)^[ \t]*>[ \t]?", "", metin)


def baglanti(b):
    """Bağlantının sonundaki noktalamayı ve eşi olmayan kapanış ayracını atar: "(doi:10.1/x)." → "10.1/x"."""
    b = b.rstrip(".,;:!?")
    while b[-1:] in (")", "]") and b.count("(" if b[-1] == ")" else "[") < b.count(b[-1]):
        b = b[:-1].rstrip(".,;:!?")
    return b


def baglantilar(metin):
    return {baglanti(b) for b in re.findall(BAGLANTI, metin)}


def gorunmez_mu(metin, i):
    c = metin[i]
    if unicodedata.category(c) not in ("Cf", "Co") or (c == "\ufeff" and i == 0):
        return False
    return not (c == "\u200d" and i > 0 and not metin[i - 1].isalpha())  # emoji dizisindeki birleştirici iş görür


def gorunmezler(metin):
    """Görünmez karakterlerin ve sohbet işaretlerinin sayımı: {"sıfır genişlikli boşluk (U+200B)": 3}."""
    sayim = Counter("%s (U+%04X)" % (GORUNMEZ_AD.get(metin[i], "görünmez karakter"), ord(metin[i]))
                    for i in range(len(metin)) if gorunmez_mu(metin, i))
    sayim.update("sohbet işareti %s" % m for m in re.findall(SOHBET_IZI, gorunmezsiz(metin, False)))
    return sayim


def gorunmezsiz(metin, sohbet=True):
    metin = "".join(c for i, c in enumerate(metin) if not gorunmez_mu(metin, i))
    return re.sub(SOHBET_IZI, "", metin) if sohbet else metin


def analiz_metni(metin):
    """Birebir denetlenen parçaları (kod, tablo, bağlantı) ve görünmez karakterleri çıkarır, alıntı
    önekini atar. Bağlantıdan sonraki noktalama cümle sonu olarak kalır."""
    metin = re.sub(KOD_BLOGU, " ", gorunmezsiz(metin))
    metin = re.sub(r"`[^`\n]+`", " ", metin)
    metin = re.sub(r"(?m)^[ \t]*\|.*$", " ", metin)
    return alintisiz(re.sub(BAGLANTI, lambda m: " " + m.group()[len(baglanti(m.group())):], metin))


def cumleler(metin, sinir=".!?…"):
    """Cümlelere böler. "A.Ş.", "Dr.", hukuk metnindeki "m.", "s.", "dn.", "Art." gibi kısaltma
    noktası, tek küçük harfli kısaltma ("c.", "f.") ve sıra sayısı ("14. CD") cümleyi bitirmez."""
    metin = re.sub(r"([.!?…])((?:\[\^[^\]\s]+\])+)", r"\2\1", metin)  # "belirler.[^1] Sonra" iki cümledir
    metin = re.sub(r"(?m)^([ \t]*#.*)$", r"\1\n", metin)  # başlık kendi cümlesidir
    metin = re.sub(r"(?m)^([ \t]*(?:#+[ \t]*)?)\d+[.)][ \t]+", r"\1- ", metin)  # "1." cümle sonu değil
    parcalar = re.split(r"(?<=[%s])\s+|\n\s*\n|\n(?=[ \t]*[#>|*-])" % re.escape(sinir), metin)
    sonuc = []
    for p in parcalar:
        p = re.sub(r"^[#>*\-\s]+", "", sade(p))
        if not p:
            continue
        if sonuc and re.search(r"(?:^|[\s(])(?:[A-ZÇĞİÖŞÜ]\.)+$|\b(?:Dr|Prof|Doç|Uzm|Av|vb|vs|örn|bkz|No|Sn"
                               r"|md|ss|dn|vd|no|art|Art|Abs|Rn|Nr|Bkz|krş|karş|Karş|çev|haz)\.$"
                               r"|(?:^|[\s(])(?:[a-np-zçğıöşü]|\d{1,2})\.$", sonuc[-1]):  # "14. CD", "2. Yasama"
            sonuc[-1] += " " + p
        else:
            sonuc.append(p)
    return sonuc


# --- Sayılar ------------------------------------------------------------------

def birim(tok):
    t = kucuk(tok).split("'")[0].split("’")[0].strip(".,;:!?()[]\"“”«»")
    if t in BIRIM_ES:
        return BIRIM_ES[t]
    if re.split(r"[/(]", t)[0] in SEMBOL_BIRIM:
        return t
    for u in SOZCUK_BIRIM:
        if t.startswith(u) and (len(u) >= 3 or re.fullmatch(u + r"(?:d[ae]n?|[ıi]n|l[ıi]k\w*|[ıi]|y[ae])?", t)):
            return BIRIM_ES.get(u, u)
    return None


def olcu_mu(b, kume=OLCU):
    return b is not None and re.split(r"[/(]", b)[0] in kume


def degerler(ham):
    """Yazılışın olası değerleri. Türkçede virgül ondalık, nokta binlik ayırıcıdır; İngilizce
    okunuş da denenir. "1,186" iki türlü okunur (belirsiz); "14.30" saat de olabilir.
    Değeri okunamayan yazılışlar (tarih ya da oran gibi) için boş küme döner."""
    if "/" in ham or ":" in ham:
        m = re.fullmatch(r"([01]?\d|2[0-3]):([0-5]\d)", ham)
        return {"saat %d:%s" % (int(m.group(1)), m.group(2))} if m else set()
    okunus = {}
    for binlik, ondalik in ((".", ","), (",", ".")):
        tam, _, ond = ham.partition(ondalik)
        parca = tam.split(binlik)
        if (ond and not ond.isdigit()) or (len(parca) > 1 and (
                not re.fullmatch(r"[1-9]\d{0,2}", parca[0]) or any(len(p) != 3 for p in parca[1:]))):
            continue
        okunus[ondalik] = (Decimal("".join(parca) + ("." + ond if ond else "")), ond)
    sonuc = {d for d, _ in okunus.values()}
    if len(sonuc) == 2:  # "42.000" 42 diye yazılmaz: sıfırla biten ondalık okunuşu at
        sonuc = {d for d, ond in okunus.values() if not ond.endswith("0")} or sonuc
    m = re.fullmatch(r"([01]?\d|2[0-3])\.([0-5]\d)", ham)
    if m:
        sonuc.add("saat %d:%s" % (int(m.group(1)), m.group(2)))
    return sonuc


def oge(metin, bas, son, deger, tur):
    """Sayının önündeki işleç ve birim, arkasındaki çarpan ve birim."""
    gorunen = bas
    on = re.search(r"(?:([%%‰₺$€])\s?|(?<![%s])([Yy]üzde)\s+)$" % HARF, metin[max(0, bas - 8):bas])  # "% 60" = "%60"
    b = None
    if on:
        gorunen -= len(on.group(0))
        b = "%" if on.group(2) else BIRIM_ES.get(on.group(1), on.group(1))
    once = metin[max(0, gorunen - 4):gorunen]
    m = re.search(r"([<>]=?|[≤≥±=])\s*$|(?:^|[^\w)])([-−+])$", once)
    islec = ""
    if m:
        isaret = m.group(1) or m.group(2)
        islec = {"=": "", "<=": "≤", ">=": "≥", "−": "-"}.get(isaret, isaret)
        gorunen -= len(once) - once.rfind(isaret)
    carpan = 1
    m = re.match(r"\s+(bin(?!a)|milyon|milyar)[%s]*" % HARF, kucuk(metin[son:son + 30]))  # "75 Milyon TL"
    if m:
        carpan, son = SOZ_DEGER[m.group(1)], son + m.end()
    sayi_son, birim_yazi = son, ""
    if b is None:
        m = re.match(r"\s*(%%|‰|°\s?[CcFf]?|[₺$€]|[%sµμ][%s0-9µμ]*(?:/[%sµμ][%s0-9µμ]*)*(?:\([A-Za-z]\))?)"
                     % ((HARF,) * 4), metin[son:])
        if m and birim(m.group(1)):
            b, son, t = birim(m.group(1)), son + m.end(), kucuk(m.group(1))
            birim_yazi = t if t in BIRIM_ES or olcu_mu(t, SEMBOL_BIRIM) else b  # "dk" kalır, "yıllık" "yıl" olur
    deger = frozenset(d * carpan if isinstance(d, Decimal) else d for d in deger)
    return Sayi(bas, deger, islec, b, sade(metin[gorunen:son]),
                re.sub(r"\s", "", metin[gorunen:sayi_son]) + birim_yazi, tur, niteleyici(metin, gorunen, son))


def niteleyici(metin, bas, son):
    """metin[bas:son] sayısına bağlı niteleyicinin grubu ("yaklaşık 5", "5'ten fazla"); yoksa boş."""
    once = kucuk(metin[max(0, bas - 20):bas])
    b = max(0, son - 4)  # arkadakinin baktığı hâl eki son'dan önce olabilir ("100 kişiden fazla")
    sonra = kucuk(metin[b:son + 40])
    # Arkada: kesmeli ek, araya en çok bir sözcük, niteleyici ve ek eylem ("100 kişi civarındaydı").
    arka = r"(?:['’][{h}]*)?(?:\s+[{h}]+(?:['’][{h}]*)?)?\s+(?:{ard})(?:y?d[ıiuü]r?)?(?![{h}])"
    for grup, on, ard in NITELEYICI:
        if re.search(r"(?<![%s])(?:%s)(?:\s+olarak)?\s*$" % (HARF, on), once) or (
                ard and re.compile(arka.format(h=HARF, ard=ard)).match(sonra, son - b)):
            return grup
    return ""


def soz_koku(w):
    for k in SOZ_KOKLERI:
        if w == k:
            return k, False
        if w.startswith(k):
            ek = w[len(k):]
            if re.fullmatch(r"[ıiuü]?nc[ıiuü]\w*", ek) or (k not in BELIRSIZ and not w.startswith(SAYI_DEGIL)):
                return k, True
    return None, False


def soz_sayilari(metin):
    """Yazıyla sayılar: "on iki" = 12, "iki buçuk" = 2,5. Çekimli biçimler ("ikisi", "dördü")
    sayı sayılır, "üçgen" gibi türevler sayılmaz."""
    ogeler, dizi = [], []

    def bitir():
        if not dizi:
            return
        toplam = grup = Decimal(0)
        for _, _, k, _ in dizi:
            v = SOZ_DEGER[k]
            if k == "yüz":
                grup = (grup or 1) * 100
            elif v >= 1000:
                toplam, grup = toplam + (grup or 1) * v, Decimal(0)
            else:
                grup += v
        guclu = len(dizi) > 1 or dizi[0][2] not in BELIRSIZ or dizi[0][3]
        ogeler.append(oge(metin, dizi[0][0], dizi[-1][1], {toplam + grup}, 1 if guclu else 2))
        dizi.clear()

    for m in re.finditer(r"[%s]+" % HARF, metin):
        k, ekli = soz_koku(kucuk(m.group(0)))
        if not (k and dizi and not dizi[-1][3] and metin[dizi[-1][1]:m.start()].isspace()):
            bitir()
        if k:
            dizi.append((m.start(), m.end(), k, ekli))
    bitir()
    return ogeler


def sayilar(metin):
    """Rakamla ve yazıyla sayılar, metindeki sırasıyla. Satır başı liste imleri ("1.", "2)") sayılmaz."""
    metin = re.sub(r"(?m)^([ \t]*(?:#+[ \t]*)?)\d+[.)](?=[ \t])", r"\1  ", metin)
    ogeler = []
    for m in re.finditer(r"(?<![\w.,:/])\d+(?:[.,:/]\d+)*", metin):
        d = degerler(m.group(0))
        if d:
            ogeler.append(oge(metin, m.start(), m.end(), d, 0))
        else:  # tarih ya da oran: her parça ayrı sayıdır, "03/04" → "04/03" sıra denetiminde yakalanır
            for p in re.finditer(r"\d+", m.group(0)):  # niteleyici ("en geç 31.12.2025") ilk parçaya bağlanır
                ogeler.append(Sayi(m.start() + p.start(), frozenset({Decimal(p.group(0))}), "", None,
                                   p.group(0), p.group(0), 0, "" if p.start() else niteleyici(metin, *m.span())))
    # "3 Nisan 2025": ay adı da bir sayıdır, "03/04/2025" ile eşleşsin.
    for m in re.finditer(r"(?<=\d)\s+(%s)(?![%s])" % ("|".join(AY_GUN[:12]), HARF), kucuk(metin)):
        ogeler.append(Sayi(m.start(1), frozenset({Decimal(AY_GUN.index(m.group(1)) + 1)}), "", None,
                           m.group(1), m.group(1), 1))
    return sorted(ogeler + soz_sayilari(metin), key=lambda o: o.yer)


def sayi_farklari(kaynak, yeni, kesin, kontrol):
    K, Y = sayilar(kaynak), sayilar(yeni)
    es, kullanilan = {}, set()
    for kosul in (lambda a, b: a.bicim == b.bicim and a.tur == b.tur and a.nitel == b.nitel,
                  lambda a, b: a.bicim == b.bicim and a.tur == b.tur,
                  lambda a, b: a.tur < 2 and b.tur < 2 and a.deger & b.deger,
                  lambda a, b: a.deger & b.deger):  # "1 hekim" → "Bir hekim"
        for i, a in enumerate(K):
            if i not in es:
                j = next((j for j, b in enumerate(Y) if j not in kullanilan and kosul(a, b)), None)
                if j is not None:
                    es[i] = j
                    kullanilan.add(j)

    yazilis = []
    for i, j in sorted(es.items()):
        a, b = K[i], Y[j]
        if a.nitel != b.nitel and 2 not in (a.tur, b.tur):  # "yaklaşık 5" → "5" bir sayı iddiasıdır
            kesin.append("Sayıya bağlı niteleyici değişti: %s (%s → %s)" % (
                a.yazi, a.nitel or "yok", b.nitel or "yok"))
        if (a.tur and b.tur) or 2 in (a.tur, b.tur):  # iki söz ("dördü" / "dört kişi") ya da belirsiz söz
            continue
        if a.islec != b.islec:
            kesin.append("Sayının işleci ya da işareti değişti: %s → %s" % (a.yazi, b.yazi))
        elif a.birim != b.birim:
            agir = olcu_mu(a.birim, SEMBOL_BIRIM) or olcu_mu(b.birim, SEMBOL_BIRIM) or (
                olcu_mu(a.birim) and olcu_mu(b.birim))
            (kesin if agir else kontrol).append("Sayının birimi ya da yanındaki söz değişti: %s → %s" % (
                a.yazi, b.yazi))
        elif a.bicim != b.bicim and min(a.tur, b.tur) == 0:
            belirsiz = any(sum(isinstance(d, Decimal) for d in o.deger) > 1 for o in (a, b))
            yazilis.append("%s → %s%s" % (a.yazi, b.yazi, " (ayırıcı belirsiz)" if belirsiz else ""))
    if yazilis:
        kontrol.append("Yalnızca yazılışı değişen sayılar (değeri doğrulayın): " + "; ".join(yazilis))

    for ogeler, eslenen, mesaj in ((K, set(es), "Sayı yeni metinde yok ya da değeri değişti: %s"),
                                   (Y, kullanilan, "Kaynakta olmayan sayı: %s")):
        for yazi, n in Counter(o.yazi for i, o in enumerate(ogeler) if i not in eslenen and o.tur == 0).items():
            kesin.append(mesaj % yazi + (" (×%d)" % n if n > 1 else ""))
    ks = [o.yazi for i, o in enumerate(K) if i not in es and o.tur == 1]
    ys = [o.yazi for j, o in enumerate(Y) if j not in kullanilan and o.tur == 1]
    if ks or ys:
        kontrol.append("Yazıyla sayı farkı (çekimli biçim ya da başka bir söz olabilir): kaynakta %s; yenide %s"
                       % (", ".join(ks) or "-", ", ".join(ys) or "-"))

    # Aynı sayılar başka sırada: "sabah 5 mg, akşam 10 mg" → "sabah 10 mg, akşam 5 mg".
    enb = None
    for i, j in sorted((i, j) for i, j in es.items() if K[i].tur == 0 and Y[j].tur == 0):
        if enb and j < enb[1]:
            kontrol.append("Sayıların sırası değişti (etiketle eşleşmesi değişmiş olabilir): "
                           "kaynakta %s … %s, yenide %s … %s" % (K[enb[0]].yazi, K[i].yazi, Y[j].yazi, Y[enb[1]].yazi))
            break
        if not enb or j > enb[1]:
            enb = (i, j)


# --- Korunan parçalar ------------------------------------------------------------

def alintilar(metin):
    """Tırnak içi alıntılar. Tırnak satır atlayabilir, boş satır atlayamaz."""
    ic = r"(?:[^%s\n]|\n(?![ \t]*\n))"
    desen = "|".join([r'"(%s{2,600}?)"' % (ic % '"'), r"“(%s{2,600}?)”" % (ic % "”"),
                      r"«(%s{2,600}?)»" % (ic % "»"),
                      r"‘((?:[^’\n]|’(?=\w)){2,300}?)’(?!\w)",
                      r"(?<![\w'’])'((?:[^'\n]|'(?=\w)){2,300}?)'(?!\w)"])
    return [sade(next(g for g in m.groups() if g)) for m in re.finditer(desen, alintisiz(metin))]


def blok_alintilar(metin):
    return [sade(alintisiz(m.group(0))) for m in re.finditer(r"(?m)(?:^[ \t]*>.*(?:\n|$))+", metin)]


def atiflar(metin):
    return [sade(m.group(0)) for m in re.finditer(r"\([^()]*?\b(?:1[6-9]|20)\d{2}[a-zğ]?\b[^()]*\)", metin)]


# Hukuki atıflar: madde, paragraf, fıkra / cümle / bent, kanun ve Resmî Gazete, karar künyesi.
# Her biri yeni metinde birebir (boşluk ve büyük/küçük harf dışında) aynı kalmalı. Atıftaki listenin
# ikinci ve sonraki öğeleri ("m. 13, 17 ve 41") sayı denetimine kalır.
HUKUKI_ATIF = re.compile("|".join([
    r"(?:(?<![\w.,/])\d{3,4}\s+|(?<!\w)[A-ZÇĞİÖŞÜ]\w*[A-ZÇĞİÖŞÜ]\s+)?(?<!\w)md?\.\s*\d+[a-z]?"
    r"(?:/\d+|/[a-zçğıöşü](?!\w))*(?:\s*[–-]\s*\d+(?:/\d+)*)?",
    r"§§?\s*\d+[a-z]?(?:\(\d+[a-z]?\))*(?:\s*[–-]\s*\d+[a-z]?(?:\(\d+[a-z]?\))*)?",
    r"(?<!\w)(?:Abs|Art)\.\s*\d+[a-z]?",
    r"(?<![\w.,/])\d+\s+sayılı(?:\s+Kanun)?",
    r"(?<!\w)RG\s+\d{1,2}[./]\d{1,2}[./]\d{4}(?:,\s*S\.\s*\d+)?",
    r"(?<!\w)(?:\w+?nc[ıiuü]|\(?[a-zçğıöşü]\))(?:\s+(?:ve|veya|ile|\w+?nc[ıiuü]))*\s+(?:cümle|fıkra|bent|bend)",
    r"(?<!\w)[EK]\.\s*\d{4}/\d+", r"(?<![\w/])\d{4}/\d+\s*[EK]\.",
    r"(?<![\w/])\d{3,6}/\d{2}(?![\w/])",  # AİHM başvuru numarası
]))


def hukuki_atif_farklari(kaynak, yeni, kesin):
    anahtar = lambda m: kucuk(re.sub(r"\s+", "", m.group(0)))
    yc, kc, yazi = Counter(anahtar(m) for m in HUKUKI_ATIF.finditer(yeni)), Counter(), {}
    for m in HUKUKI_ATIF.finditer(kaynak):
        kc[anahtar(m)] += 1
        yazi.setdefault(anahtar(m), sade(m.group(0)))
    for a in yazi:
        if kc[a] > yc[a]:
            kesin.append("Hukuki atıf yeni metinde birebir yok: %s" % yazi[a] + (
                " (kaynakta %d, yenide %d kez)" % (kc[a], yc[a]) if yc[a] else ""))


def atif_ogeleri_var_mi(atif, metin):
    """"(Yılmaz, 2020)" → "Yılmaz'ın (2020)" biçim değişikliğidir: ad ve yıl öbür metinde duruyor mu?"""
    return all(p in metin for p in re.findall(r"[%s]{2,}|\d{4}" % HARF, atif) if p not in ("ve", "vd", "and"))


def tirnak(s):
    return re.sub(r"[\"“”«»‘’']", '"', s)


def korunanlar(kaynak, yeni, kesin, kontrol):
    yeni_sade = sade(alintisiz(yeni))
    yeni_satir = {s.strip() for s in yeni.splitlines()}
    for blok in re.findall(KOD_BLOGU, kaynak):
        if blok.strip() not in yeni:
            kesin.append("Kod bloğu yeni metinde birebir yok: %s" % sade(blok)[:80])
    for kod in re.findall(r"`[^`\n]+`", re.sub(KOD_BLOGU, " ", kaynak)):
        if kod not in yeni:
            kesin.append("Satır içi kod yeni metinde birebir yok: %s" % kod)
    for satir in kaynak.splitlines():
        if satir.strip().startswith("|") and satir.strip() not in yeni_satir:
            kesin.append("Tablo satırı değişti (tablolara dokunulmaz): %s" % satir.strip())
    for b in sorted(baglantilar(kaynak) - baglantilar(yeni)):
        kesin.append("Bağlantı ya da DOI yeni metinde birebir yok: %s" % b)
    for b in sorted(baglantilar(yeni) - baglantilar(kaynak)):
        kesin.append("Kaynakta olmayan bağlantı ya da DOI: %s" % b)
    for etiket, liste in (("Blok alıntı", blok_alintilar(kaynak)), ("Alıntı", alintilar(kaynak))):
        for parca in liste:
            if parca in yeni_sade:
                continue
            if tirnak(parca) in tirnak(yeni_sade):  # ‘A “b” c’ → “A ‘b’ c”: yalnızca tırnak türü değişti
                kontrol.append("%s içindeki tırnak işaretleri değişti: %s" % (etiket, parca))
            else:
                kesin.append("%s yeni metinde birebir yok: %s" % (etiket, parca))
    for parca in atiflar(kaynak):
        if parca not in yeni_sade:
            (kontrol if atif_ogeleri_var_mi(parca, yeni) else kesin).append(
                "Kaynak gösterimi yeni metinde birebir yok: %s" % parca)
    for parca in atiflar(yeni):
        if parca not in sade(kaynak):
            (kontrol if atif_ogeleri_var_mi(parca, kaynak) else kesin).append(
                "Kaynakta olmayan kaynak gösterimi: %s" % parca)
    ka, ya = alintilar(kaynak), alintilar(yeni)
    ortak = set(ka) & set(ya)
    if [a for a in ka if a in ortak] != [a for a in ya if a in ortak]:
        kontrol.append("Alıntıların sırası değişti (kime ait olduğu değişmiş olabilir): %s → %s" % (
            " / ".join(a for a in ka if a in ortak), " / ".join(a for a in ya if a in ortak)))


# --- Adlar ----------------------------------------------------------------------

def baslik_mi(sozler):
    """Başlık Düzeninde Yazılmış bir satır ya da etiket ("Mevcut Durum")."""
    harfli = [s for s in sozler if s[0].isalpha() and s not in ("ve", "ile", "için", "veya")]
    return len(harfli) >= 2 and sum(s[0].isupper() for s in harfli) >= 0.7 * len(harfli)


def kisaltma_mi(s):
    return sum(c.isupper() for c in s) >= 2 or any(c.isdigit() for c in s)


def buyuk_harfliler(cumle):
    """Cümledeki büyük harfli sözcükler; kesme işaretinden sonrası ek sayılır."""
    sonuc = []
    for s in re.findall(r"[%s0-9][%s0-9.\-/'’]*" % (HARF, HARF), cumle):
        s = re.split(r"['’]", s)[0].rstrip(".-/")
        sonuc.append(s if s and s[0].isupper() and not any(kucuk(s).startswith(a) for a in AY_GUN) else None)
    return sonuc


def adlar(metin):
    """(cümle içindeki adlar ve kısaltmalar, yalnızca cümle başında görülen büyük harfli sözcükler).
    Başlık düzenindeki satırlar ad sayılmaz."""
    ic, bas = set(), set()
    metin = re.sub(r"(?m)^\s*(?:#+|[-*]|\d+[.)])\s+", "", metin).replace("**", "\n")
    for cumle in cumleler(metin, ".!?…:"):
        sozler = buyuk_harfliler(cumle)
        baslik = baslik_mi(re.findall(r"[%s0-9][%s0-9.\-/'’]*" % (HARF, HARF), cumle)) and \
            not cumle.rstrip("*").endswith((".", "!", "?", "…"))
        for i, s in enumerate(sozler):
            if s and (kisaltma_mi(s) or not (i == 0 or baslik)):
                ic.add(s)
            elif s and i == 0 and not baslik:
                bas.add(s)
    return ic, bas - ic


def duz_sozler(metin):
    """(kesmesi ve noktası atılmış küçük harfli söz, adı ya da None): "Hastanesi'ne" → ("hastanesine",
    "Hastanesi"), "K.D.V." → ("kdv", "K.D.V")."""
    sozler = re.findall(r"[%s0-9][%s0-9.\-/'’]*" % (HARF, HARF), metin)
    return {(kucuk(re.sub(r"['’.]", "", s.rstrip(".-/"))), ad) for ad, s in zip(buyuk_harfliler(metin), sozler)}


def ad_farklari(kaynak, yeni, kesin, kontrol):
    k_ic, k_bas = adlar(kaynak)
    y_ic, y_bas = adlar(yeni)
    yeni_tum, yeni_soz = y_ic | y_bas, re.findall(r"[%s0-9]+" % HARF, kucuk(yeni))
    kaynak_kucuk = kucuk(kaynak)
    # shortcut: "Ali'ye" → "Aliye" (başka ad) de yalnızca KONTROL olur; gerekirse ad listesiyle ayırın.
    kd, yd = duz_sozler(kaynak), duz_sozler(yeni)
    yf, kf = {f for f, _ in yd}, {f for f, a in kd if a}
    for ad in sorted(k_ic - yeni_tum):
        if kucuk(ad) in yeni_soz or any(a == ad and f in yf for f, a in kd):
            kontrol.append("Özel adın yazımı değişti (büyük/küçük harf, kesme ya da kısaltma noktası): %s" % ad)
        else:
            kesin.append("Özel ad ya da kısaltma yeni metinde yok: %s" % ad)
    # Cümle başındaki büyük harfli söz ad da olabilir, sıradan söz de; kalkmışsa yalnızca kontrol.
    kayip = [ad for ad in sorted(k_bas - yeni_tum)
             if len(ad) > 2 and ad not in DOLGU and not any(w.startswith(kucuk(ad)) for w in yeni_soz)
             and not re.search(r"(?<=[\s(])%s(?![%s])" % (re.escape(kucuk(ad)), HARF), kaynak_kucuk)
             and not any(r.fullmatch(kucuk(ad)) for _, rs in IMLER_RE for r in rs)]
    if kayip:
        kontrol.append("Cümle başındaki büyük harfli söz yeni metinde yok (ad olabilir): %s" % ", ".join(kayip))
    yeni_ad = sorted(ad for ad in y_ic - k_ic - k_bas if not any(a == ad and f in kf for f, a in yd))
    if yeni_ad:
        kontrol.append("Kaynakta olmayan özel ad ya da kısaltma: %s" % ", ".join(yeni_ad))


def ay_gun(metin, gevsek):
    """Ay ve gün adları. Sıkı sayımda yalnızca büyük harfli ya da sayıdan sonra gelenler
    sayılır ("güven aralığı", "pazarlama" gibi sözler karışmasın)."""
    c = Counter()
    for m in re.finditer(r"[%s]+" % HARF, metin):
        k = kucuk(m.group(0))
        tarih = m.group(0)[0].isupper() or re.search(r"\d\s?$", metin[max(0, m.start() - 3):m.start()])
        for ad in sorted(AY_GUN, key=len, reverse=True):
            if k.startswith(ad) and len(k) - len(ad) <= 3:
                if gevsek or tarih:
                    c[ad] += 1
                break
    return c


# --- Anlam sözleri ve cümle eşleme ----------------------------------------------

def imler(metin):
    """Her sınıf için desen başına eşleşen biçimlerin listesi."""
    k = kucuk(metin)
    return {ad: [[m.group(0) for m in r.finditer(k)] for r in rs] for ad, rs in IMLER_RE}


def odaklar(metin):
    """Odak sözü ve kapsadığı söz: "sadece gece…", "planı… bile"."""
    s = re.findall(r"[%s]+" % HARF, kucuk(metin))
    c = Counter()
    for i, w in enumerate(s):
        if w in ODAK_SONRA and i + 1 < len(s):
            c["sadece %s…" % s[i + 1][:5]] += 1
        elif w in ODAK_ONCE and i:
            c["%s… %s" % (s[i - 1][:5], w)] += 1
    return c


def olumsuz_baglam(metin):
    """Olumsuz sözün önündeki söz ("kayıtlar artmadı" / "şikâyetler artmadı"). Kısa ekler (de, ki) atlanır."""
    k = kucuk(metin)
    c = Counter()
    for m in IMLER_RE[0][1][0].finditer(k):  # Olumsuzluk sınıfının tek deseni
        once = [w for w in re.findall(r"[%s]+" % HARF, k[:m.start()]) if len(w) > 2]
        c["%s… (olumsuz)" % (once[-1][:5] if once else "")] += 1
    return c


@lru_cache(maxsize=None)
def isaret_mi(w):
    return any(r.fullmatch(w) for _, rs in IMLER_RE for r in rs)


def kokler(s):
    """İçerik sözcüklerinin ilk beş harfi (kaba gövde). İşlev sözcükleri ve anlam sözleri sayılmaz:
    cümleler içerikle eşlenir, anlam sözleri eşlenen cümleler arasında karşılaştırılır."""
    return [w[:5] for w in re.findall(r"[%s]+" % HARF, kucuk(s))
            if len(w) >= 4 and w[:5] not in ("daha", "için", "olara", "gibi", "kadar", "şekil", "olan")
            and not isaret_mi(w)]


def obekler(kc, yc):
    """Cümle eşleme. difflib değişmeyen cümleleri sabitler. Aradaki değişen bölgede her cümle
    öbür metinde en çok benzediği cümleye bağlanır; birbirine bağlanan cümleler bir öbek olur,
    böylece bölünen ve birleşen cümleler de eşleşir. Karşılığı olmayan cümle tek başına öbektir."""
    gruplar = []
    sm = difflib.SequenceMatcher(None, [kucuk(s) for s in kc], [kucuk(s) for s in yc], autojunk=False)
    for etiket, i1, i2, j1, j2 in sm.get_opcodes():
        if etiket == "equal":
            continue
        if i1 == i2 or j1 == j2:
            gruplar += [([i], []) for i in range(i1, i2)] + [([], [j]) for j in range(j1, j2)]
            continue
        K, Y = range(i1, i2), range(j1, j2)
        kk, yk = {i: kokler(kc[i]) for i in K}, {j: kokler(yc[j]) for j in Y}
        oran = {(i, j): difflib.SequenceMatcher(None, kk[i], yk[j], autojunk=False).ratio() for i in K for j in Y}
        ata = {x: x for x in [(0, i) for i in K] + [(1, j) for j in Y]}

        def kok(x):
            while ata[x] != x:
                x = ata[x]
            return x

        def puan(i, j):  # eşit benzerlikte bölgedeki yeri yakın olan seçilir
            return oran[i, j], -abs((i - i1) / len(K) - (j - j1) / len(Y))

        for i in K:  # hiçbir gövdesi ortak olmayan cümle bağlanmaz, tek başına kalır
            j = max(Y, key=lambda j: puan(i, j))
            if puan(i, j)[0]:
                ata[kok((0, i))] = kok((1, j))
        for j in Y:
            i = max(K, key=lambda i: puan(i, j))
            if puan(i, j)[0]:
                ata[kok((1, j))] = kok((0, i))
        bolge = {}
        for taraf, x in sorted(ata):
            bolge.setdefault(kok((taraf, x)), ([], []))[taraf].append(x)
        gruplar += sorted(bolge.values())
    return gruplar


def kisa(s, n=70):
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"


MISTIR = re.compile(r"[%s]+m[ıiuü]şt[ıiuü]r[%s]*" % (HARF, HARF))
# Sıra bildiren ekler. Yardımcı eylemde ("test edildikten") kök önceki içerik sözcüğünden alınır.
SIRA_EKI = [(ad, re.compile(r"(?<![%s])([%s]{2,}?)%s(?![%s])" % (HARF, HARF, d, HARF))) for ad, d in (
    ("-dıktan sonra", r"[dt][ıiuü]kt[ae]n\s+sonra"), ("-madan önce", r"m[ae]d[ae]n\s+önce"),
    ("-ıncaya kadar", r"y?[ıiuü]nc[ae]y[ae]\s+kadar"), ("-ınca", r"y?[ıiuü]nc[ae]"))]
YARDIMCI = {"ed", "et", "edil", "ol", "olun", "yap", "yapıl", "kıl", "kılın"}
EK_UYUM = str.maketrans("eiuüt", "aıııd")


def sira_kokleri(metin):
    """Her sıra eki için bağlı olduğu eylemlerin kökleri (kokler gibi ilk beş harf)."""
    k, sonuc = kucuk(metin), {}
    for ad, r in SIRA_EKI:
        for m in r.finditer(k):
            kok = (kokler(k[:m.start()]) or [""])[-1] if m.group(1) in YARDIMCI else m.group(1)[:5]
            if len(kok) >= 3:
                sonuc.setdefault(ad, set()).add(kok)
    return sonuc


def sira_isaretleri(metin):
    """"A … sonra B": önce / sonra / ardından işaretinden önceki ve sonraki ilk içerik kökü."""
    k = kucuk(metin)
    isaret = r"(?<![%s])(?:önce|sonra|ardından)(?![%s])" % (HARF, HARF)
    return {(o[0], m.group(0), s[0]) for m in re.finditer(isaret, k)
            for o, s in [(kokler(k[:m.start()]), kokler(k[m.end():]))] if o and s}


def ad_ekleri(metin):
    """(ad, kesme işaretinden sonraki ek): "Ali'yi" ve "Ahmet'i" aynı eki taşır (uyum ve kaynaştırma atılır)."""
    sozler = re.findall(r"[%s0-9][%s0-9.\-/'’]*" % (HARF, HARF), metin)
    return {(ad, re.sub(r"^[yn](?=[aeıiuü])", "", kucuk((re.split(r"['’]", s) + [""])[1])).translate(EK_UYUM))
            for ad, s in zip(buyuk_harfliler(metin), sozler) if ad}


def obek_farklari(kt, yt, bildirilen):
    """İki cümle öbeği arasındaki anlam sözü, odak ve ad sırası farkları; ayrıca -mıştır farkı.
    -mıştır → -dı yeniden yazımda çok sık olduğu için ayrı döner (yalnız başına satır açmaz)."""
    a, b = imler(kt), imler(yt)
    farklar = []
    for ad, _ in IMLER:
        cikan, giren = Counter(), Counter()
        for x, y in zip(a[ad], b[ad]):
            y = [f for f in y if f not in bildirilen]  # metin genelinde zaten bildirilen mutlak söz
            if len(x) != len(y):
                cikan += Counter(x) - Counter(y)
                giren += Counter(y) - Counter(x)
        if cikan or giren:
            farklar.append("%s (çıkan: %s; giren: %s)" % (ad, ", ".join(cikan.elements()) or "-",
                                                         ", ".join(giren.elements()) or "-"))
            if ad.startswith("Karşıolgusal") and sum(cikan.values()) > sum(giren.values()):
                farklar[-1] += ": gerçekleşmemiş koşul açık koşula dönmüş olabilir"
    ko, yo = olumsuz_baglam(kt), olumsuz_baglam(yt)
    if not any(f.startswith("Olumsuzluk") for f in farklar) and ko != yo:
        farklar.append("Olumsuzluk başka öğeye geçmiş olabilir: %s → %s" % (", ".join(ko - yo), ", ".join(yo - ko)))
    ko, yo = odaklar(kt), odaklar(yt)
    if ko != yo:
        farklar.append("Odak sözü kaydı: %s → %s" % (", ".join(ko) or "-", ", ".join(yo) or "-"))
    ka, ya = [s for s in buyuk_harfliler(kt) if s], [s for s in buyuk_harfliler(yt) if s]
    ortak = set(ka) & set(ya)
    ka, ya = [s for s in dict.fromkeys(ka) if s in ortak], [s for s in dict.fromkeys(ya) if s in ortak]
    if len(ortak) > 1 and ka != ya:
        farklar.append("Adların sırası değişti (kim kime, rol değişmiş olabilir): %s → %s" % (
            ", ".join(ka), ", ".join(ya)))
    ke, ye = ad_ekleri(kt), ad_ekleri(yt)
    ortak = {a for a, _ in ke} & {a for a, _ in ye}
    ke, ye = {x for x in ke if x[0] in ortak}, {x for x in ye if x[0] in ortak}
    if ke != ye and Counter(e for _, e in ke) == Counter(e for _, e in ye):
        farklar.append("Hâl ekleri adlar arasında yer değiştirdi; roller değişmiş olabilir: %s"
                       % ", ".join(sorted({a for a, _ in ke ^ ye})))
    ks, ys = sira_kokleri(kt), sira_kokleri(yt)
    gecer = lambda kok, s: re.search(r"(?<![%s])%s" % (HARF, re.escape(kok)), kucuk(s))
    for ad in sorted(set(ks) & set(ys)):
        if any(gecer(a, yt) and gecer(b, kt) for a in ks[ad] - ys[ad] for b in ys[ad] - ks[ad]):
            farklar.append("Sıra bildiren ek (%s) başka bir eyleme geçmiş; olayların sırası ters dönmüş "
                           "olabilir: %s → %s" % (ad, ", ".join(sorted(ks[ad])), ", ".join(sorted(ys[ad]))))
    yi = sira_isaretleri(yt)
    ters = ["%s … %s … %s" % t for t in sorted(sira_isaretleri(kt)) if t[0] != t[2] and t[::-1] in yi]
    if ters:
        farklar.append("Sıra sözünün iki yanı yer değiştirdi; olayların sırası ters dönmüş olabilir: %s"
                       % ", ".join(ters))
    km, ym = Counter(MISTIR.findall(kucuk(kt))), Counter(MISTIR.findall(kucuk(yt)))
    mistir = "çıkan: %s; giren: %s" % (", ".join((km - ym).elements()) or "-",
                                      ", ".join((ym - km).elements()) or "-") if km != ym else ""
    return farklar, mistir


def cumle_farklari(kaynak, yeni, kontrol, bildirilen=()):
    kc, yc = cumleler(kaynak), cumleler(yeni)
    yeni_kok = set(kokler(yeni))
    dusen = {i for i, s in enumerate(kc) if len(kokler(s)) >= 3
             and sum(k in yeni_kok for k in kokler(s)) < len(kokler(s)) / 2}
    satirlar, notlar, eklenen, yalniz_mistir = [], {}, [], []
    for ki, yi in obekler(kc, yc):
        farklar, mistir = obek_farklari(" ".join(kc[i] for i in ki), " ".join(yc[j] for j in yi), bildirilen)
        if mistir and (farklar or set(ki) <= dusen):
            farklar.append("-mıştır (%s)" % mistir)
        elif mistir:
            yalniz_mistir.append("Cümle %s (%s)" % (",".join(str(i + 1) for i in ki), mistir))
        if not farklar:
            continue
        yenide = ",".join(str(j + 1) for j in yi) or "-"
        if not ki:  # kaynakta karşılığı olmayan yeni cümle
            eklenen.append("yeni %s “%s” [%s]" % (yenide, kisa(yc[yi[0]]), "; ".join(farklar)))
        elif set(ki) <= dusen:  # düşmüş görünen cümlenin farkları kendi satırına yazılır
            notlar[ki[0]] = " [→ yeni %s: %s]" % (yenide, "; ".join(farklar))
        else:
            satirlar.append("Cümle %s → yeni %s: %s. Kaynak: “%s”" % (
                ",".join(str(i + 1) for i in ki), yenide, "; ".join(farklar),
                kisa(max((kc[i] for i in ki), key=len))))
    if dusen or eklenen:
        kontrol.append("Karşılığı zayıf ya da olmayan cümle (düşmüş ya da eklenmiş olabilir): " + "; ".join(
            ["Cümle %d “%s”%s" % (i + 1, kisa(kc[i]), notlar.get(i, "")) for i in sorted(dusen)] + eklenen))
    if yalniz_mistir:
        kontrol.append("Yalnızca -mıştır değişen cümleler (kesinlik ya da çıkarım değişmiş olabilir): "
                       + "; ".join(yalniz_mistir))
    kontrol.extend(satirlar)


def ek_ciftleri(kaynak, yeni, kontrol):
    """Biçimbilimsel çözümleme yapmadan iki karşıtlık: -lı/-sız (kayıtlı → kayıtsız) ve ettirgen
    (yaptırdı → yaptı). Yalnızca aynı gövdenin karşıt biçimi öbür metinde geçiyorsa uyarır."""
    ks, ys = (set(re.findall(r"[%s]+" % HARF, kucuk(t))) for t in (kaynak, yeni))
    for a, b in ((ks, ys), (ys, ks)):
        for w in sorted(a - b):
            m = re.fullmatch(r"(\w{3,})(s[ıiuü]z|l[ıiuü])\w*", w)
            if m and a is ks:  # iki yön için de kaynaktaki biçimden bakmak yeter
                karsit = re.compile(m.group(1) + ("l[ıiuü]" if m.group(2)[0] == "s" else "s[ıiuü]z"))
                if any(karsit.match(x) for x in b - a) and not any(karsit.match(x) for x in a):
                    kontrol.append("-lı / -sız karşıtlığı: %s ↔ %s" % (w, next(x for x in b - a if karsit.match(x))))
            for m in re.finditer(r"[dt][ıiuü]r", w):
                s = m.start()
                if s < 2 or w[s + 3:s + 4] in ("", "l"):  # "-dır", "-dırlar" ek eylemdir
                    continue
                yalin = w[:s] + w[s + 3:]
                if w[s + 3:s + 4] == "d" and w[s - 1] in "çfhkpsşt":
                    yalin = w[:s] + "t" + w[s + 4:]
                if yalin in b - a:
                    kontrol.append("Ettirgen çatı değişti (yaptırdı / yaptı): %s ↔ %s" % (w, yalin))


def genel_farklar(kaynak, yeni, kesin, kontrol):
    """Metin geneli: giren birinci kişi ve giren mutlak söz. Eklenen mutlak sözleri döndürür."""
    ki, yi = imler(kaynak)["Kişi (biz / ben)"], imler(yeni)["Kişi (biz / ben)"]
    # "biz", "ben" ve "şirketimiz" gibi iyelik de kaynakta birinci kişi sayılır (cümle karşılaştırmasında gürültülü).
    if not any(ki) and any(yi) and not re.search(
            r"(?<![%s])(?:biz|ben)(?![%s])|[%s]+[ıiuü]m[ıiuü]z" % (HARF, HARF, HARF), kucuk(kaynak)):
        kesin.append("Kaynakta birinci kişi yokken yeni metinde var: %s" % ", ".join(sum(yi, [])))
    kk, yk = kucuk(kaynak), kucuk(yeni)
    eklenen = [s for s in MUTLAK if not re.search(r"(?<![%s])%s(?![%s])" % (HARF, s, HARF), kk)
               and re.search(r"(?<![%s])%s(?![%s])" % (HARF, s, HARF), yk)]
    if eklenen:
        kontrol.append("Kaynakta olmayan sıklık ya da mutlaklık sözü eklendi: %s" % ", ".join(eklenen))
    return eklenen


DIPNOT = r"\[\^([^\]\s]+)\](?!:)"


def dipnotlar(metin):
    """Her dipnot işaretinin her geçişi için işaretten önce, aynı cümlede söylenenin kökleri."""
    sonuc = {}
    for c in cumleler(metin):
        for m in re.finditer(DIPNOT, c):
            sonuc.setdefault(m.group(1), []).append((set(kokler(re.sub(DIPNOT, " ", c[:m.start()]))), c))
    return sonuc


def dipnot_farklari(kaynak, yeni, kesin):
    tanim = lambda t: dict(re.findall(r"(?m)^\[\^([^\]\s]+)\]:(.*)$", t))
    kt, yt = tanim(kaynak), tanim(yeni)
    for d in kt:
        if kt[d] != yt.get(d):
            kesin.append("Dipnot metni değişti ya da silindi: [^%s]" % d)
    kd, yd = dipnotlar(kaynak), dipnotlar(yeni)
    for d in kd:
        if d not in yd:
            kesin.append("Dipnot işareti yeni metinde yok: [^%s]" % d)
            continue
        if len(yd[d]) < len(kd[d]):  # aynı dipnot birden çok yerde: her geçiş sayılır
            kesin.append("Dipnot işareti eksik: [^%s] kaynakta %d, yenide %d kez" % (d, len(kd[d]), len(yd[d])))
        for (onceki, kc), (simdi, yc) in zip(kd[d], yd[d]):
            if onceki and len(onceki & simdi) < len(onceki) / 2:
                kesin.append("Dipnot [^%s] başka bir iddiaya taşınmış olabilir. Kaynakta: “%s” · Yenide: “%s”"
                             % (d, kisa(kc), kisa(yc)))
    for d in yd:
        if len(yd[d]) > len(kd.get(d, [])):
            kesin.append("Kaynakta olmayan dipnot işareti: [^%s]" % d)


BASLIK = re.compile(r"(?m)^(#{1,6})[ \t]+(.+?)[ \t#]*$")
# "Bölüm kaynakçası (2. Bölüm)" korunur; "Yeni kaynaklar ve erişim düzeyleri" gibi not başlıkları korunmaz.
KAYNAKCA = r"kaynakça|bibliography|^(?:[\divxlc]+[.)]\s+)?(?:kaynaklar|references)(?:\s*\(.*\))?$"


def korunan_mu(baslik, koru=()):
    """Kaynakça başlığı ya da --koru parçalarından birini (büyük/küçük harf ayrımsız) taşıyan başlık."""
    k = kucuk(baslik)
    return bool(re.search(KAYNAKCA, k)) or any(p.strip() and kucuk(p.strip()) in k for p in koru)


def bolumler(metin):
    """(başlık, metin): bölüm, aynı ya da daha üst düzeydeki bir sonraki başlığa kadar sürer."""
    bas = [(len(m.group(1)), m.group(2), m.start()) for m in BASLIK.finditer(metin)]
    return [(b, metin[s:next((s2 for d2, _, s2 in bas[i + 1:] if d2 <= d), len(metin))])
            for i, (d, b, s) in enumerate(bas)]


def korunan_bolum_farklari(kaynak, yeni, koru, kesin):
    duz = lambda t: [s.rstrip() for s in t.strip().splitlines()]
    yeniler = {}
    for b, t in bolumler(yeni):
        yeniler.setdefault(sade(b), []).append(duz(t))
    for b, t in bolumler(kaynak):
        eski, adaylar = duz(t), yeniler.get(sade(b), [])
        if not korunan_mu(b, koru) or eski in adaylar:
            continue
        if not adaylar:
            kesin.append("Korunan bölüm yeni metinde yok (başlığı değişmiş olabilir): %s" % b)
            continue
        y = adaylar[0]
        i = next((i for i, (a, c) in enumerate(zip(eski, y)) if a != c), min(len(eski), len(y)))
        kesin.append("Korunan bölüm değişti: %s (bölümün %d. satırı: “%s”)" % (
            b, i + 1, kisa(eski[i] if i < len(eski) else y[i], 120)))


def fark_tablosu(kaynak, yeni):
    """Cümle eşlemesindeki her değişen öbek için bir satır; karşılığı olmayan taraf "—" yazılır."""
    kc, yc = cumleler(analiz_metni(kaynak)), cumleler(analiz_metni(yeni))
    hucre = lambda s: s.replace("|", "\\|") or "—"
    satirlar = []
    for ki, yi in obekler(kc, yc):
        kt, yt = " ".join(kc[i] for i in ki), " ".join(yc[j] for j in yi)
        if kt != yt:
            satirlar.append("| %s → %s | %s | %s |" % (",".join(str(i + 1) for i in ki) or "-",
                                                     ",".join(str(j + 1) for j in yi) or "-", hucre(kt), hucre(yt)))
    return "\n".join(["| No | Önce | Sonra |", "|---|---|---|"] + satirlar) if satirlar else "Değişen cümle yok."


# --- Hedefli sorular: riskli cümleyi bulur, hüküm vermez ------------------------
# shortcut: "-sınca / -ğınca" atılır ("Dairesince", "Bakanlığınca" sıra değil),
# "basınca", "doğunca" da kaçar.
SIRA_SOZU = re.compile(r"(?<![%s])(?:önce(?!l)\w*|sonra\w*|ardından|kadar|itibaren|beri|\w+[dt][ıiuü]kt[ae]n"
                       r"|\w+m[ae]d[ae]n|(?!düşünce)\w+(?<![sğ])y?[ıiuü]nc[ae])(?![%s])" % (HARF, HARF))
# -dığı / -acağı. Ünsüz uyumu DIK'taki gibi: "etiği", "pratiği" (ünlü + t) ilgi yapısı değildir.
ILGI = re.compile(r"(?<![%s])(?!ol(?:du|aca|madı)ğ)[%s]*(?:(?:[aeıioöuü]d|[çfhkpsşt]t|[bcdgğjlmnrvyz]d)[ıiuü]"
                  r"|[ae]c[ae])ğ[ıiuü]" % (HARF, HARF))
# -(y)an / -(y)en ve ardından bir söz. Hâl eki (-dan, -ten), -ken ve -an / -en ile biten yaygın
# sözler atılır.
YAYGIN_AN = ("olan", "olmayan", "bulunan", "alan", "oran", "zaman", "insan", "uzman", "alman", "erken", "hemen",
             "tamamen", "kısmen", "nadiren", "esasen", "aslen", "itibaren", "beyan", "ilan", "imkan", "imkân", "plan")
SIFAT_FIIL = re.compile(r"(?<![%s])(?!(?:%s)\s)(?:eden|[%s]+(?:y[ae]n|[^\W\d_dt][ae]n))(?<!ken)\s+[%s]"
                        % (HARF, "|".join(YAYGIN_AN), HARF, HARF))
KISI_KURUM = [re.compile(r"(?<![%s])%s" % (HARF, p)) for p in (
    "hekim", "doktor", "çalışan", "işçi(?!lik|liğ)", "işveren", "kadın", "hasta(?!lı|ne)",
    r"eş(?:i|in|ine|ini|inin|iyle|e|ler\w*)?(?![%s])" % HARF, "veli", "h[âa]kim", "savcı", "sanı[kğ]",
    "mağdur", "fail", "daire", "başsavcılı", "yargıtay", "mahkeme", "kurul(?![adm])", "bakanlı")]
NITEL_SOZU = re.compile(r"(?<![%s])(?:%s)(?![%s])" % (
    HARF, "|".join(p for _, on, ard in NITELEYICI for p in (on, ard) if p), HARF))
SINIR_SOZU = re.compile(r"(?<![%s])(?:(?:en az|en fazla|yalnızca|sadece|tek)\s+bir|hiçbir\w*)(?![%s])" % (HARF, HARF))
SORU = {"SIRA": "Hangi olay önce oluyor?", "ROL": "Kim kime ne yaptı?",
        "NİTELEYİCİ": "Her niteleyici hangi sayıya bağlı?", "SINIR": "Bu sınır hangi öğeye bağlı?"}


def soru_turleri(cumle):
    k = kucuk(cumle)
    kisiler = sum(bool(r.search(k)) for r in KISI_KURUM) + len(  # yalnızca hâl eki alan adlar rol taşır
        {s for s in re.findall(r"(?<![%s])([A-ZÇĞİÖŞÜ][%s]*)['’][%s]+" % (HARF, HARF, HARF), cumle)
         if not any(r.match(kucuk(s)) for r in KISI_KURUM)})
    return {t for t, var in (
        ("SIRA", SIRA_SOZU.search(k)),
        ("ROL", ILGI.search(k) or SIFAT_FIIL.search(k) or kisiler >= 2),
        ("NİTELEYİCİ", NITEL_SOZU.search(k) and sum(o.tur < 2 for o in sayilar(cumle)) >= 2),
        ("SINIR", SINIR_SOZU.search(k))) if var}


def aralik(xs):
    return "%d-%d" % (xs[0] + 1, xs[-1] + 1) if len(xs) > 1 and xs[-1] - xs[0] == len(xs) - 1 \
        else ",".join(str(x + 1) for x in xs)


def hedefli_sorular(kaynak, yeni):
    """Eşlenen ve değişen her cümle çifti için en çok bir soru satırı (türler "[SIRA+ROL]" diye birleşir)."""
    kc, yc = cumleler(analiz_metni(kaynak)), cumleler(analiz_metni(yeni))
    sorular = []
    for ki, yi in obekler(kc, yc):
        kt, yt = " ".join(kc[i] for i in ki), " ".join(yc[j] for j in yi)
        if not ki or not yi or kt == yt:
            continue
        turler = set().union(*(soru_turleri(c) for c in [kc[i] for i in ki] + [yc[j] for j in yi]))
        if turler:
            sira = [t for t in SORU if t in turler]
            sorular.append("[%s] Cümle %s → yeni %s: %s Kaynakta ve yenide aynı mı? Kaynak: “%s” · Yeni: “%s”" % (
                "+".join(sira), aralik(ki), aralik(yi), " ".join(SORU[t] for t in sira), kisa(kt, 160), kisa(yt, 160)))
    return sorular


def gorunmez_farklari(kaynak, yeni, kesin, kontrol):
    ks, ys = gorunmezler(kaynak), gorunmezler(yeni)
    if ys - ks:
        kesin.append("Kaynakta olmayan görünmez karakter ya da sohbet işareti: %s" % ", ".join(
            "%s ×%d" % x for x in sorted((ys - ks).items())))
    if ys & ks:
        kontrol.append("Kaynaktaki görünmez karakter ya da sohbet işareti yeni metinde duruyor (silinebilir; "
                       "denetim bunları yok sayar): %s" % ", ".join("%s ×%d" % x for x in sorted((ys & ks).items())))


def terimleri_oku(deger):
    """--terimler değeri: dosya yolu ya da ";" ile ayrılmış liste."""
    try:
        with open(deger, encoding="utf-8") as f:
            satirlar = f.read().splitlines()
    except OSError:
        satirlar = deger.split(";")
    return [sade(t) for t in satirlar if sade(t) and not t.strip().startswith("#")]


def terim_farklari(kaynak, yeni, terimler, kesin, kontrol):
    """Kullanıcının verdiği terimler: ekli biçimler de sayılır, büyük/küçük harf ayrılmaz."""
    kk, yk = kucuk(kaynak), kucuk(yeni)
    for t in terimler:
        desen = r"(?<![%s0-9])%s" % (HARF, r"\s+".join(map(re.escape, kucuk(t).split())))
        a, b = len(re.findall(desen, kk)), len(re.findall(desen, yk))
        if a > b:
            kesin.append("Korunan terim yeni metinde eksik: %s (kaynakta %d, yenide %d kez)" % (t, a, b))
        elif b > a:
            kontrol.append("Korunan terim yeni metinde daha sık: %s (kaynakta %d, yenide %d kez)" % (t, a, b))


def denetle(kaynak, yeni, koru=(), terimler=()):
    kesin, kontrol = [], []
    gorunmez_farklari(kaynak, yeni, kesin, kontrol)
    kaynak, yeni = gorunmezsiz(kaynak), gorunmezsiz(yeni)
    korunanlar(kaynak, yeni, kesin, kontrol)
    korunan_bolum_farklari(kaynak, yeni, koru, kesin)
    dipnot_farklari(kaynak, yeni, kesin)
    kaynak_a, yeni_a = analiz_metni(kaynak), analiz_metni(yeni)
    hukuki_atif_farklari(kaynak_a, yeni_a, kesin)
    sayi_farklari(kaynak_a, yeni_a, kesin, kontrol)
    terim_farklari(kaynak_a, yeni_a, terimler, kesin, kontrol)

    ks_gun, yg_gun = ay_gun(kaynak_a, False), ay_gun(yeni_a, True)
    ys_gun, kg_gun = ay_gun(yeni_a, False), ay_gun(kaynak_a, True)
    for ad in sorted(set(ks_gun) | set(ys_gun)):
        if ks_gun[ad] > yg_gun[ad]:
            kesin.append("Ay ya da gün adı: %s kaynakta %d, yeni metinde %d kez geçiyor." % (ad, ks_gun[ad], yg_gun[ad]))
        if ys_gun[ad] > kg_gun[ad]:
            kontrol.append("Kaynakta olmayan ay ya da gün adı: %s" % ad)

    ad_farklari(kaynak_a, yeni_a, kesin, kontrol)
    eklenen = genel_farklar(kaynak_a, yeni_a, kesin, kontrol)
    cumle_farklari(kaynak_a, yeni_a, kontrol, eklenen)
    ek_ciftleri(kaynak_a, yeni_a, kontrol)

    ka, ya = re.findall(r"\w+", kucuk(kaynak)), re.findall(r"\w+", kucuk(yeni))
    oran = 1 - difflib.SequenceMatcher(None, ka, ya, autojunk=False).ratio()
    return kesin, kontrol, oran


def secenekler(argv):
    """(dosyalar, --koru parçaları, --terimler, --fark var mı); bir seçeneğin değeri eksikse None döner."""
    args, koru, terimler = [a for a in argv if a != "--fark"], [], []
    for ad in ("--koru", "--terimler"):
        while ad in args:
            i = args.index(ad)
            if i + 1 >= len(args):
                return None
            if ad == "--koru":
                koru += args[i + 1].split(";")
            else:
                terimler += terimleri_oku(args[i + 1])
            del args[i:i + 2]
    return args, koru, terimler, "--fark" in argv


def main():
    secim = secenekler(sys.argv[1:])
    if not secim or len(secim[0]) != 2:
        print(__doc__.strip().splitlines()[2])
        return 2
    (kaynak, yeni), koru, terimler, fark = [oku(y) for y in secim[0]], secim[1], secim[2], secim[3]
    kesin, kontrol, oran = denetle(kaynak, yeni, koru, terimler)
    kn, yn = len(kaynak.split()), len(yeni.split())
    print("ANLAM DENETİMİ")
    print("Sözcük sayısı: kaynak %d, yeni %d (%%%d)" % (kn, yn, round(100 * yn / max(kn, 1))))
    print("Değişen sözcük oranı: %%%d" % round(oran * 100))
    if kesin:
        print("\nKESİN SORUNLAR (düzeltin; kaynakta öyle değilse gerekçesini yazın)")
        for s in kesin:
            print("- " + s)
    if kontrol:
        print("\nKONTROL EDİN (anlam değişmiş olabilir; her birini kaynakla karşılaştırın)")
        for n, s in enumerate(kontrol, 1):
            print("K%d. %s" % (n, s))
    if not kesin and not kontrol:
        print("\nSorun bulunmadı.")
    sorular = hedefli_sorular(kaynak, yeni)
    if sorular:
        print("\nHEDEFLİ SORULAR (betik hüküm vermez; her soruyu kaynakla karşılaştırarak yanıtlayın)")
        for n, s in enumerate(sorular, 1):
            print("S%d. %s" % (n, s))
    if fark:
        print("\nFARK TABLOSU (eşlenen ve değişen cümleler; numaralar yukarıdaki cümle numaralarıdır)\n")
        print(fark_tablosu(kaynak, yeni))
    return 1 if kesin else 0


if __name__ == "__main__":
    sys.exit(main())
