---
name: aynen
description: Aynen, Türkçe bir metni yapay zekâ kokusundan arındırıp iyi bir insan yazarın elinden çıkmış gibi okunur hâle getirir ve bunu yaparken metnin söylediği hiçbir şeyi değiştirmez. Temkin, kapsam, olumsuzluk, koşul, kip, zaman, kanıtsallık, sayılar, terimler, dipnotlar ve atıflar korunur, sonuç bir anlam denetiminden geçer. Kullanıcı Türkçe bir metin için "doğallaştır", "insanlaştır", "yapay zekâ gibi durmasın", "robot gibi olmuş", "AI kokuyor", "daha doğal yaz", "akıcılaştır", "humanize" dediğinde ya da bir blog yazısını, e-postayı, duyuruyu, raporu, tez bölümünü, akademik özeti, resmî yazıyı, ürün metnini veya sosyal medya paylaşımını "elden geçir", "redakte et", "yeniden yaz" diye verdiğinde kullan. Yabancı dildeki bir metin için "Türkçeleştir" isteğinde de kullan. İki metni anlam bakımından karşılaştırma isteğinde yalnızca denetim betiğini çalıştır. Kaynak metin olmadan sıfırdan yazma, yalnızca özetleme ve yapay zekâ dedektörünü atlatma istekleri için kullanma. Use for humanizing or de-AI-ing Turkish text without changing its meaning.
---

# Aynen — Türkçe Metin Doğallaştırıcı

*İnsan gibi yazar, söylediğini aynen korur.*

Yapay zekâyla üretilmiş Türkçe metni ele veren şey tek tek sözcüklerden çok kalıplardır:
- hep "Günümüzde" ile başlayan girişler
- birbirinin kopyası cümleler
- "-mektedir" ile biten yüklem dizileri
- "önemli bir rol oynamaktadır" türü içi boş ifadeler
- İngilizceden taşınmış noktalama

Aynen bu kalıpları temizler. Asıl işi ise temizlerken **anlamı korumaktır**. Doğallık ile anlam çatışırsa her zaman anlam kazanır.

## Sınır

- Hedef, iyi bir Türk yazarın kaleminden çıkmış gibi okunan bir metindir. Dedektörden geçme vaadi verilmez. Kullanıcı sorarsa tek cümleyle açıkla: Dedektörler güvenilir değildir, Aynen yalnızca metni doğallaştırır.
- Görünmez karakter, kasıtlı yazım hatası ya da anlamsız eş anlamlı değişimi gibi dedektör hileleri kullanılmaz.
- Aynen olgu düzeltmez. Metinde bir yanlış ya da çelişki görürsen onu düzeltme, yalnızca bildir.

## Öncelik sırası

Her madde, altındakilerin hepsinden önce gelir:
1. Anlam ve korunacak öğeler
2. Kullanıcının açık isteği
3. Projenin, derginin ya da kurumun yazım kılavuzu (varsa)
4. Metin türü ve register
5. Düzeltme seviyesi
6. Kalıp kataloğundaki öneriler

## Anlam sözleşmesi

Düzeltilmiş metin, kaynağın söylediği her şeyi aynı güçle söyler, kaynakta olmayan hiçbir şeyi söylemez. Ayrıntılar ve örnekler `references/anlam-kaymasi.md` dosyasında (ANL-01 – ANL-23).

**Aynı kalanlar:**
- **Kesinlik:** temkin ("olabilir", "düşündürmektedir"), derece ("büyük ölçüde", "kısmen") ve sayısal yaklaşıklık ("yaklaşık 100"). Bunlar üç ayrı şeydir; biri ötekinin yerine geçmez.
- **Kapsam ve dağılım:** "bazı", "tüm", "her", "sadece", "bile", "her çalışana ikişer". Kapsam sözü bağlandığı öğenin yanında kalır.
- **Olumsuzluk:** "-mA", "değil", "yok", "ne … ne", "pek … değil". "Anlamlı fark bulunmadı", "fark yok" demek değildir. "Gerekmiyor" da "yapılmamalı" demek değildir.
- **Koşul ve istisna:** "-sa", "-madıkça", "takdirde", "ancak … ise", "hariç". Gerekli koşul yeterli koşula, gerçekleşmemiş koşul ("-saydı") açık koşula dönüşmez.
- **Mantıksal bağ:** "ve" ile "veya" yer değiştirmez. Soru bildirime dönüşmez.
- **İlişki ve neden:** "ilişkili", "artırır" olmaz. Amaç gerçekleşmiş bir sonuca dönmez. Kaynakta olmayan bir "bu yüzden" eklenmez, olan bağ silinmez.
- **Kip:** Olasılık, çıkarım, yetenek, izin ve yetki, öneri, gereklilik, yükümlülük ve yasak ayrı türlerdir. Tür de güç de değişmez. Öneri karara, "deneyin" "deneyebilirsiniz"e dönüşmez.
- **Zaman ve olayın durumu:** "planlandı", "yapıldı" değildir. "henüz", "hâlâ", "artık", "önce", "sonra", "en geç" yerinde kalır. Olayların sırası korunur.
- **Kanıtsallık:** Aktarılan bilgi "-mış" ve "göre" ile kalır.
- **Roller:** Kim kime ne yaptı aynı kalır. Ettirgen ve edilgen ekler korunur, "-lı" "-sız"a dönmez. Kaynakta olmayan "biz" ya da kurum eklenmez.
- **Görüşün sahibi:** Kanun, mahkeme, öğreti ve yazarın görüşü ("kanaatimizce") birbirine dönüşmez.
- **Karşılaştırma:** Yön ve taban korunur.
- **Yazarın sesi:** Retorik soru, ironi, bilinçli tekrar ve devrik cümle bilinçli seçimlerdir; korunur.

**Aynen kalan öğeler:**
- sayılar ve yanlarındaki işaretler (<, >, eksi)
- birimler ve para birimleri, tarihler, saatler
- istatistik değerleri (n, p, OR, %95 GA)
- kaynak gösterimleri, dipnot işaretleri ve dipnot metinleri
- hukuki atıflar: madde, fıkra, cümle, §, E./K., başvuru numarası
- terimler, kısaltmalar, özel adlar
- alıntılar, bağlantılar, kod, tablolar

**Biçim kuralları:**
- Sayının biçimine yalnızca değeri kesinse ve metin içinde tutarsızsa dokun.
- Sayısal tarih biçimine dokunma: "03/04" iki türlü okunabilir. Tek istisna: Kılavuz istiyorsa ve gün ile ay açıksa kılavuza uyabilirsin.
- Saatteki iki noktayı TDK'ye göre noktaya çevirebilirsin (yazım ve noktalama dosyası, YZ-09); değer aynı kalır. Kodda, tabloda ve arayüz metninde çevirme.
- Yazıyla yazılmış sayıyı rakama, rakamı yazıya çevirme.

**Eklenmeyen ve silinmeyenler:**
- **Eklenmez:** Kaynakta olmayan örnek, gerekçe, sonuç, sayı, özne, derece ya da sıklık sözü ("çoğu zaman", "her zaman").
- **Silinmez:**
  - zaman ve yer sınırı ("son yıllarda", "bu işletmede")
  - kaynak ("Bakanlık verilerine göre")
  - koşul, tanım
  - önceki bir bölümü gösteren söz
  - yakın anlamlı ama ayrı nitelikler ("sezgisel ve kolay anlaşılır")

**Register:** Akademik metin akademik, resmî metin resmî kalır. Hitap (siz/sen) ve anlatıcının kişisi değişmez. Edilgen yapı yalnızca orta ve derin seviyede, fail kaynakta açıkça yazılıysa etkene çevrilir.

## Düzeltme seviyeleri

| Seviye | Ne yapılır | Varsayılan olduğu metinler |
|---|---|---|
| **hafif** | Yazım ve noktalama. Açılış ve kapanış dolguları, bağlam klişeleri (ACL, KLS-01, KLS-02). Süs pekiştirmeyi eş güçte sade bir sözle değiştirme ("son derece kritik" → "çok önemli"; "büyük önem taşımaktadır" → "çok önemlidir"). Yalnızca ekleme işlevi gören cümle başı geçişleri silme ("Ayrıca"). "-mekte olup", "-mış olup" ve sonraki yüklemin "-tır"ını paylaşan noktalı virgüllü "-mış;" zincirlerini bölme ya da sıfat-fiille birleştirme (aktarım bildiren "-mış" bölünse de "-mış" kalır; bölmek bir sonraki bağlacın kapsamını daraltıyorsa bölme). Açık dolgu sözlerin silinmesi de hafif seviyeye girer: dolgu "bize", yalnızca ekleme yapan "aynı zamanda", dolgu sıfat-fiiller (KLS-09: "elde edilen bulgular" → "bulgular", "yapılan bu çalışmada" → "bu çalışmada"). Zaman ve kip aynı kalıyorsa ağır yardımcı fiil sadeleştirmesi de hafife girer (DLB-05: "gerçekleştirilmektedir" → "yapılmaktadır"). Zaman ve görünüşü koruyan sıfat-fiil sadeleştirmeleri de girer ("oynamakta olduğu" → "oynadığı"). Bunların dışında cümle sınırına ve yüklem zamanına dokunulmaz. Akademik metinde "-mektedir" zinciri türün olağan dilidir; hafif seviyede kalır. | akademik, tez, tıbbi, hukuki, mevzuat, sözleşme |
| **orta** | Hafiftekilere ek olarak cümle birleştirme ve bölme, bağlaç seçimi, "-mektedir" yoğunluğunu azaltma (zaman ve görünüş aynı kalarak), fail açıkça yazılıysa "tarafından"ı çözme, gereksiz maddeleri düzyazıya çevirme. | duyuru, olay raporu, iş e-postası, resmî yazışma, blog, deneme ve köşe yazısı (yazarın sesi korunarak), ürün metni, sosyal medya |
| **derin** | Ortadakilere ek olarak öğe sırası, paragraf düzeni ve ritim. Yalnızca kullanıcı isterse uygulanır ("baştan yaz", "daha cesur ol"). | yok |

- Kullanıcı bir seviye söylerse ona uy. "Hâlâ yapay duruyor" derse bir üst seviyeye geç. Seviyeyi sen seçtiysen ve bir denetim notu yazıyorsan seviyeyi notta belirt.
- Hiçbir seviye anlam sözleşmesini gevşetmez.
- **Temkin, izleri bırakmak demek değildir.** Şu açık izler her seviyede temizlenir, `Dokunma` satırındaki istisnalar hariç:
  - açılış ve kapanış dolguları
  - "bu bağlamda / bu çerçevede / bu doğrultuda"
  - belirli bir belgeyi göstermeyen "söz konusu"
  - süs pekiştirme ("son derece", "hayati")
  - "hızla değişen dünyada" türü girişler
  - "vazgeçilmez bir parçası" türü önem şişirmesi

  Bir klişeyi eş işlevli başka bir klişeyle değiştirmek ("bu bağlamda" → "bu çerçevede") temizlik sayılmaz. Ya silinir ya da gerçek bir bağla değiştirilir.
- Orta seviyede, duyuru ve raporda art arda "-mıştır / -mektedir / -ecektir" yığılmasını, zaman ve görünüşü koruyarak azalt.
- **Yapay zekâ taslağı.** Kullanıcı metnin yapay zekâ gibi durduğundan yakınıyorsa ("yapay zekâ gibi durmasın", "AI kokuyor", "robot gibi") ve metin birden çok kümeden kalıp taşıyorsa, metni yapay zekâ taslağı say. Akademik, tıbbi, hukuki, mevzuat ve sözleşme dışındaki türlerde şunları uygula:
  - Deneme, köşe yazısı, slogan ve sosyal medya için kalıpların **Dokunma** satırlarındaki "yazarın sesi" istisnaları taslakta geçerli değildir. Korunacak bir yazar sesi yoktur, ses yapay zekânındır.
  - Hazır imgeler ("görünmez bir zırh", "ruhsal çölleşme", "beton yığınları arasında yalnızlık"), tanıtım abartısı ("inanılmaz", "muazzam", "kocaman, dinamik ve güçlü bir aile", "sınırları kaldıran deneyim"), hazır kapanış özdeyişleri ve tekdüze cümle ritmi iz sayılır. Orta seviyede sadeleştir. Slogan, çağrı ya da kapanış cümlesini silme, sadeleştir: Silmek bir çağrıyı ya da iddiayı kaldırır.
  - İddianın gücü kalır, söyleyiş değişir: "tarihin en yalnız döneminden geçiyoruz" bir üstünlük iddiasıdır, "hiç bu kadar yalnız olmamıştık" olur, "biraz yalnızlaştık" olmaz. Sayı, koşul, istisna, kip, temkin ve olumsuzluk anlam sözleşmesine tabidir.
  - İz taşıyan cümlelerin çoğuna dokunmak bu durumda olağandır. Birkaç cümleye dokunup gerisini bırakmak, kullanıcının istediğini karşılamaz.
  - Metinde gerçek bir insan sesinin işaretleri varsa (kişisel ayrıntı, somut anekdot, beklenmedik söz seçimi, ironi), metin taslak değildir ya da yalnızca bir bölümü taslaktır. Bu durumda yazarın sesi kuralları geçerlidir.
  - Kalıp az, metin doğalsa (haber, kurum metni, gerçek bir köşe yazısı), kullanıcının isteğine rağmen az dokun ve bunu söyle.
- Proje kılavuzu seviyeyle çatışırsa kılavuz kazanır. Örneğin kılavuz uzun cümlelerin bölünmesini istiyorsa hafif seviyede de bölebilirsin. Ama bölünen cümledeki her dipnot, koşul ve istisna kendi iddiasıyla kalır.

## Çalışma adımları

### 1. Metni tanı

- **Kaynak:** Denetimde kaynak, kullanıcının bu turda verdiği metindir. Önceki bir çıktın yeniden düzeltiliyorsa ilk metni de elinde tut ki kaymalar birikmesin.
- **Register ve seviye:** Kararsızsan daha resmî registerı ve daha hafif seviyeyi seç. Resmî bir metni gündelikleştirmek daha büyük bir hatadır.
- **Proje kılavuzu:** Projenin klasöründe ya da kullanıcının verdiği bir yazım kılavuzu varsa önce onu oku.
- **Uzunluk:** Metin 2.000 sözcüğü aşıyorsa ya da birden çok dosyadan oluşuyorsa `references/uzun-belge.md` iş akışını izle.
- **Korunacaklar listesi:** Sayıları etiketleri ve işaretleriyle birlikte yaz ("%95 GA 1,21–2,79", "p<0,001"). Tarihleri, birimleri, özel adları, terimleri, kısaltmaları, atıfları, dipnotları ve alıntıları da listele.
- **Dokunulmayacak bloklar:** Kodun, satır içi kodun, bağlantıların, tabloların, doğrudan alıntıların, mevzuat aktarımlarının ve kaynakçanın sınırlarını önceden işaretle. Bunlar yeniden yazıma girmez. Kullanıcı düzeltilmesini istediği taslağı bir blok alıntıya koyduysa o blok düzeltilir.
- **Önerme listesi:** Kaynağı numaralı, tek iddialı önermelere ayır. Her önermenin yanına şunları not et:
  - kesinlik ve kip türü
  - olumsuzluk, kapsam, koşul
  - zaman ve sıra
  - bilginin kaynağı
  - neden-sonuç bağı
  - kim kime ne yaptı

  Akademik, tıbbi, hukuki ve resmî metinde ve 150 sözcüğü aşan her metinde bu listeyi yaz (kullanıcıya gösterme). Uzun belge modunda liste yalnızca değiştirdiğin paragraflar için yazılır.

**Kısa yol:** Başlıksız ve 120 sözcükten kısa gündelik bir metinde (mesaj, kısa e-posta, sosyal medya) önerme listesini yazma, bağımsız denetçiyi atla. Betik ve iki yönlü kontrol yine yapılır.

### 2. İzleri bul

Başvuru dosyaları:
- **`scripts/tarama.py`:** Önce bunu çalıştır (`python3 -I <skill-klasörü>/scripts/tarama.py metin.md`). Kalıplardan sözcükle bulunabilenleri satır ve kalıp kimliğiyle listeler. Yapısal kalıpları göremez; metni yine baştan sona oku.
- **Okuma sırası:** `anlam-kaymasi.md`'yi tamamen oku. `kaliplar.md`'den dizini, taramada çıkan kalıpların maddelerini ve metinde gördüğün öteki kalıpların maddelerini oku; dosyanın tamamını okumak gerekmez. Öteki başvuru dosyalarına yalnızca gerektiğinde bak.
- **`references/kaliplar.md`:** Yapay zekâ izi kalıpları. Kümeler: ACL, KLS, DLB, YPI, CEV, NOK, BIC, TON. Her kalıbın **Dokunma** satırı, o kalıbın hangi registerda olağan dil olduğunu söyler. Her öneri anlam sözleşmesine tabidir.
- **`references/anlam-kaymasi.md`:** Düzeltirken anlamın nerede kaydığını gösterir. Kalıp önerisiyle çatışırsa bu dosya kazanır.
- **`references/yazim-noktalama.md`:** TDK'ya dayalı yazım ve noktalama kuralları ile İngilizce tipografi izleri.
- **`references/baglaclar-ve-gecisler.md`:** Bağlaçların işlevleri ve anlam tuzakları.
- **`references/cumle-ritmi.md`:** Tekdüze ritmi kırma araçları ve dönüşümlerin anlam uyarıları.

### 3. Yeniden yaz

- **Az ve doğru dokun.** Hedef, iyi bir yazarın bu metni nasıl yazacağıdır. İyi bir cümleye dokunma. Metnin çoğu insan elinden çıkmışsa yalnızca iz taşıyan cümlelere dokun.
- **Önce sil, sonra birleştir, en son dizilimi değiştir.** En etkili düzeltme çoğu zaman bir klişeyi silmektir.
- **Riskli işlemleri tanı.** Anlamı en sık kaydıranlar şunlardır:
  - cümle birleştirme ve bölme
  - edilgeni etkene çevirme
  - bağlaç değiştirme ya da ekleme
  - pekiştirme silme
  - maddeyi düzyazıya çevirme
  - yüklemin zamanını değiştirme

  Bu işlemleri yaptığın her cümleyi denetimde ayrıca kontrol et.
- **Zarf-fiile dikkat.**
  - İşlevini ek değil bağlam belirler.
  - -ıp ve -arak ile bağlanan fiil ana yüklemin kipini alır. "Bildirir ve kaçınabilir" → "bildirip kaçınabilir" yazılırsa bildirim yükümlülüğü düşer.
  - Bir yükümlülüğü bir istisna, hak ya da ikinci bir yükümlülükle birleştirirsen her yükümlülük kendi açık yüklemini korur.
- **Dipnot iddiasının yanında kalır.** Dipnot birden çok yan cümleyi destekliyor olabilirse o cümleyi bölme ya da birleştirme.
- **Bağlaç eklemek ilişki eklemektir.** Bağlaçları sırayla dağıtma ("ama… oysa… ne var ki…"); her ilişki için en uygun olanı seç ya da bağlacı kaldır.
- **Devrik ve eksiltili cümleyi bağlam isterse kullan.** Blogda ve sosyal medyada yerindedir, akademik ve resmî metinde değil.
- **Biçimi metne uydur.** Kısa bir e-postadaki gereksiz başlıkları ve maddeleri düzyazıya çevir; gerçek adım listelerini koru.
- **Emin değilsen dokunma.**

### 4. Denetle

Teslimden önce üç katmanlı denetim yap. Şüphe kalırsa kaynaktaki ifadeye dön.

**a) Betik.** Komut çalıştırabiliyorsan:
1. Kaynağı ve yeni metni sistemin geçici klasöründe iki UTF-8 dosyaya yaz.
2. Şunu çalıştır:

   ```
   python3 -I <skill-klasörü>/scripts/anlam_denetimi.py kaynak.txt yeni.txt
   ```

   Gerekirse şu seçenekleri ekle:
   - `--koru "Başlık;Başka başlık"`: Bu başlıkların altındaki bölümler birebir aynı kalmalıdır.
   - `--terimler "terim;başka terim"` ya da `--terimler terimler.txt`: Korunacaklar listesindeki alan terimleri. Küçük harfle yazılan terimleri ("spirometri", "bilinçli taksir") betik ancak böyle sayar. Kısaltmaları ve büyük harfli adları zaten denetler. Dosyada her satıra bir terim yaz.
   - `--fark`: Değişen cümlelerin tablosunu ekler.
3. İş bitince geçici dosyaları sil.

Betiğin çıktısını şöyle değerlendir:
- **KESİN:** Değişen ya da kaybolan sayı, birim, dipnot, atıf, bağlantı, DOI, alıntı, özel ad, korunan terim ya da korunan bölüm; yeni metne giren görünmez karakter. Hepsini düzelt. Yanlış alarmsa nedenini not et. Doğru bir düzeltmeyi yalnızca uyarı sussun diye geri alma.
- **Görünmez karakter ve sohbet işareti:** Sıfır genişlikli boşluk, yumuşak tire ya da "【4†source】" gibi işaretler sohbet ekranından kopyalanmış metinde kalır (BIC-05). Betik bunları karşılaştırmada yok sayar ve yeni metinde kaldıysa bildirir. Sil ve kullanıcıya sade bir sözle söyle: "Metinde görünmeyen 3 karakter vardı, sildim."
- **KONTROL:** Numaralıdır. Her biri için tek satırlık bir hüküm ver: "karşılığı şu cümlede" ya da "kayma, düzeltildi". Bir anlam sözü azaldıysa ya da başka cümleye geçtiyse karşılığını aynı açıklıkla göster. Dolgu olduğu için silinen sözlerin karşılığı aranmaz; neden dolgu olduğunu yaz.
- **HEDEFLİ SORULAR:** Betiğin kesin olarak yakalayamadığı kaymalar için değişen riskli cümlelere sorulan sorular:
  - [SIRA] Hangi olay önce?
  - [ROL] Kim kime ne yaptı?
  - [NİTELEYİCİ] Niteleyici hangi sayıya bağlı?
  - [SINIR] "En az bir" hangi öğeye bağlı?

  Bunları b) adımında yanıtla.

Düzelttikten sonra betiği yeniden çalıştır. Betik bir süzgeçtir, anlamı okumaz. "Sorun bulunmadı" sonucu b) adımını gereksiz kılmaz.

**Betik çalışmıyorsa:** Korunacaklar listesindeki her öğeyi yeni metinde tek tek bul. Her anlam sözünün karşılığını göster. Hedefli soruları kendin sor. Denetim notuna "elle, betiksiz" yaz.

**b) İki yönlü önerme kontrolü** (her metinde):
- **Kaynaktan yeniye:** Her önerme aynı kesinlik, kip, kapsam, olumsuzluk, koşul, zaman, kaynak ve rolle duruyor mu?
- **Yeniden kaynağa:** Yeni metnin her cümlesi kaynaktan çıkıyor mu? Eklenmiş bir bağ, sebep, sonuç, derece, sıklık ya da özne var mı?
- **Hedefli sorular:** Her soruyu kaynak cümle ve yeni cümle için ayrı ayrı, açıkça yanıtla. Cevaplar farklıysa cümleyi kaynaktaki hâline döndür.
- **Register, hitap ve yazarın sesi** aynı mı? Silinen her şey gerçekten boş muydu?

**c) Bağımsız denetçi.** Şu durumlarda uygula:
- akademik, tıbbi, hukuki ya da resmî metin: çalışanlara ya da kamuya giden kurumsal duyuru ve olay raporu dahil
- kullanıcı "dikkatli ol", "anlam değişmesin" dediğinde

Ürün tanıtımı, pazarlama metni ve sosyal medya paylaşımında isteğe bağlıdır. Ama bu metinler süre, fiyat, onay ya da yükümlülük gibi koşullar içeriyorsa uygula. Denetim notu da aynı kurala uyar.
- Alt ajan açabiliyorsan alt ajana yalnızca şunları ver:
  - kaynak metin ve yeni metin
  - `references/dogrulama.md` talimatı
  - varsa hedefli soruların listesi (senin cevapların olmadan)

  Gerekçelerini ve betik çıktısını verme. Denetçinin bulduğu her sorunu düzelt. Düzeltmeden sonra son metinde a) ve b) adımlarını yinele.
- Alt ajan açamıyorsan b) adımını ikinci kez yap: Bu kez kaynağı cümle cümle oku ve her cümlenin karşılığını yeni metinde ara.

## Çıktı

- Varsayılan olarak **yalnızca düzeltilmiş metni** ver: önsöz yok, kapanış yok. Kaynağın biçimini koru.
- Akademik, tıbbi, hukuki ve resmî metinde metnin altına `---` ayracı ve tek satırlık bir denetim notu ekle. Not metnin parçası değildir. Örnek:

  *Denetim (metne dahil değil): seviye hafif · betik 0 KESİN, 3 KONTROL incelendi · iki yönlü kontrol yapıldı. Son okuma sizde.*

  Gündelik ve kişisel metinde (deneme, blog, sosyal medya, kısa e-posta) denetim notu yazma. Kullanıcı sorarsa söyle. Betik çalışmadıysa bunu yaz. Hiçbir denetim yapmadıysan not yazma. Bir dosya üzerinde çalışıyorsan notu dosyaya değil, kullanıcıya verdiğin özete yaz.
- Denetim satırından önce, şu durumlarda kısa bir not ekle (en çok üç madde):
  - anlamından emin olamadığın için dokunmadığın bir yer
  - fark ettiğin bir olgu hatası ya da çelişki
  - kullanıcının karar vermesi gereken bir üslup tercihi
  - bir isteği anlam sözleşmesi yüzünden tam karşılayamaman
  - bir dolguyu sildiğinde bunu bildirmeyi gerektiren bir durum
- **Öneriler listesi.** Kendiliğinden değiştirmediğin ama okunurluğu artıracak söyleyiş önerilerini metnin altında **tek bir kısa listede** ver. Bunlar okura yabancı iç jargon ve İngilizceden kelime kelime çevrilmiş isim zincirleridir (CEV-06).
  - En fazla 5 madde yaz, en çok etki eden önce. Fazlası varsa yalnızca sayısını söyle: "ayrıca 7 benzer öneri var".
  - Her madde tek satırdır: ifade → önerilen söyleyiş · kısa gerekçe.
  - Akışı soru sorarak durdurma; metni her durumda teslim et.
  - Kullanıcı "uygula" ya da "şu ikisini uygula" derse uygula ve denetimi yinele.
- **Kullanıcıyla sade konuş.** Kullanıcıya yazdığın not, öneri ve özetlerde iç kodları (CEV-06, ANL-14) ve dil bilgisi terimlerini ("kalıp", "ad tamlaması", "kanıtsallık") kullanma. Ne demek istediğini gündelik sözlerle söyle: "İngilizceden kelime kelime çevrilmiş gibi duruyor", "bu söz bir sıklık iddiası ekliyor".
- Kullanıcı değişiklikleri görmek isterse yalnızca değişen cümleler için **Önce | Sonra | Neden** tablosu ver.

## Özel durumlar

- **Metin zaten doğalsa** yalnızca yazım ve noktalama düzelt, bunu bir cümleyle söyle. İyi bir metne uygulanan "doğallaştırma" yalnızca risk ekler.
- **"Kısalt" ya da "samimileştir" isteği:**
  - Yalnızca dolguyu, tekrarı ve süsü çıkar. Hedefe ancak bilgi çıkararak ulaşılıyorsa bilgi çıkarma.
  - Sözleşmeyi koruyan sürümü ver. Altına şunları yaz: ulaşılan uzunluk, hedef için çıkması gereken bilgiler ve her birini çıkarmanın bedeli. Tarihleri, istisnaları ve uyarıları bu listeye koyma.
  - Samimileştirirken hitabı ve kip sözlerini değiştirme.
- **Türkçeleştirme:**
  - Yabancı dildeki metni baştan bu ilkelere uygun Türkçeyle yaz ve çeviri olduğunu belirt. Denetimi kaynak dildeki metne göre yap; özellikle sayılar, adlar, kip ("may, must, shall") ve koşul ("unless, only if") önemli.
  - Metin Türkçeyse ve içinde yabancı sözcükler varsa, "Türkçeleştir" muhtemelen onların karşılığını istemektir. Emin değilsen sor.
- **Karışık dil:**
  - Terimlere ve kısaltmalara dokunma. Örneğin SLA bir taahhüttür, "hedef" değildir.
  - Çeviri istenmedikçe İngilizce cümleleri, arayüz etiketlerini ve hata iletilerini çevirme.
  - "may" bir karar değildir.
- **Tıbbi metin:** İlaç adı, doz, uygulama yolu ve sıklığı, laboratuvar değerleri ve tanı kodları aynen kalır. "Önerilir, endikedir, kontrendikedir" aynı basamakta kalır.
- **Hukuki metin:**
  - Geniş zaman ("sağlar, bildirir") çoğu zaman yükümlülük bildirir. "-ebilir" çoğu zaman yetki bildirir. İkisinin de türü korunur.
  - "yükümlüdür", "en geç", "derhâl", "ve/veya", "ilgili mevzuat çerçevesinde" ve yükümlüyü adlandıran "tarafından" dolgu değildir.
  - "-mekte olup" zinciri bölünürken ilk yüklem kaynağın çekimini korur ("-mektedir"). Yükümlülük bildiren geniş zamana ya da "-yor"a çevrilmez, çünkü bu, kipi değiştirir.
  - Görüşün sahibi değişmez (ANL-22). Olan hukuk ile olması gereken hukuk karışmaz (ANL-23). "İncelenen kararlar arasında rastlanmadı", "karar yok" demek değildir.
- **Uzun belge ve tez:** Kopya üzerinde çalış, belge geneli terim listesi ve ilerleme dosyası tut, değişiklik tablosunu ver (`references/uzun-belge.md`).
- **Okura yabancı iç jargon.** Bazı sözler metnin hedef okuru için yabancıdır. Bunlar yapay zekâ izi değildir ve anlamı da bozmaz, ama metni anlaşılmaz kılar. Üç türü vardır:
  - Çalışma sırasında uydurulmuş etiketler ("tuzaklı metin", "anlam sözleşmesi")
  - Bir meslek grubunun iç dili
  - Genel okura yönelik metinde açıklanmadan kullanılan teknik karşılıklar ("betik", "regresyon vakası")

  Bu sözleri kendiliğinden değiştirme. Terim değişikliği anlamı kaydırabilir (ANL-14), ayrıca yazarın bilinçli seçimi olabilir. Bunun yerine öneriler listesine ekle (Çıktı bölümü) ve somut bir öneri sun: "'tuzaklı metin' okura tanıdık gelmeyebilir; 'anlamın kolayca kayabileceği test metni' gibi açıklayıcı bir ifade düşünebilirsiniz."

  Şu durumlarda işaretleme:
  - Söz, ilk geçtiği yerde açıklanmışsa.
  - Söz, alanın yerleşik terimiyse ve metin o alanın okuruna yazılmışsa ("insidans" bir tıp makalesinde, "OR" bir epidemiyoloji özetinde).
  - Kullanıcı terimi kendisi seçmişse.

  Okurun kim olduğunu metin türünden çıkar: README, duyuru ve sosyal medya paylaşımı genel okura yazılır, makale ve tez uzman okura.
- **Yazarın bilinçli üslubu** belirginse koru (edebi devrik dil, kasıtlı plaza dili, markanın emojisi). Yalnızca yapay zekâdan gelen katmanı temizle. Bir kalıbın ironik pastiş mi, yoksa yapay katman mı olduğunu şöyle ayır: Yakınında ironi işareti varsa pastiştir. İroni işaretleri: kısa alaycı cevap ("Elbette."), abartılı yineleme, tırnak, hemen ardından gelen ters köşe. Metnin geri kalanının sesine aykırı, düz ve bilgi taşımayan bir kalıp ise yapay katmandır. Kararsızsan dokunma ve bunu notta belirt.
- **Yalnızca karşılaştırma isteği** ("şu iki metin aynı şeyi söylüyor mu?"): Metni yeniden yazma. Betiği çalıştır, b) adımını uygula ve bulguları bildir.

## Örnekler

`examples/` klasöründe altı metin türü için tam örnekler var: iş sağlığı duyurusu, iş e-postası, tez özeti, ürün metni, kişisel paylaşım ve tıbbi özet. Her örnekte şunlar var:
- düzeltilmeden önceki metin ve düzeltilmiş hâli
- düzeltilen kalıplar
- bilinçli olarak korunanlar
- akıcı görünen ama anlamı kaydıran yeniden yazımlar

Bir türle ilk kez karşılaştığında ilgili örneğe bak.
