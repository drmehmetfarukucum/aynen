# Yapay zekâ kalıpları

Bu dosya, Türkçe metinde yapay zekâ izi bırakan 51 kalıbı sekiz kümede toplar. Her kalıpta neye benzediği, neden yapay durduğu, nasıl düzeltileceği, hangi durumda dokunulmayacağı ve düzeltirken anlamın nerede kayabileceği yazılıdır. Örnek cümlelerin hepsi bu dosya için yazıldı ve `scripts/anlam_denetimi.py` ile sınandı.

## Kullanmadan önce

- **Anlam önce gelir.** Her öneri `anlam-kaymasi.md`'deki kurallara (ANL-01…ANL-23) tabidir. Bir düzeltme temkini, dereceyi, kapsamı, olumsuzluğu, koşulu, kipi, zamanı, kanıtsallığı, özneyi, karşılaştırmayı, terimi, sayıyı ya da atfı değiştiriyorsa yapılmaz. İki dosya çatışırsa `anlam-kaymasi.md` kazanır.
- **Kalıp kanıt değildir.** Bunlar olasılık işaretleridir. İnsanlar da aynı kalıpları kullanır. Tek bir kalıp bir metni yapay yapmaz; yoğunluğa ve birlikteliğe bak [WP-AI].
- **Register belirler.** Aynı kalıp bir türde iz, başka bir türde olağan dildir. Her kalıbın **Dokunma** satırı bunu söyler. Akademik metinde "-mektedir", hukukta yükümlülük bildiren geniş zaman, tutanakta yükümlüyü adlandıran "tarafından" iz değildir.
- **Yazarın sesi korunur.** Deneme, köşe yazısı ve konuşma metninde retorik soru, ironi, bilinçli tekrar, kısa vurucu cümle ve devrik cümle yazarın seçimidir (ANL-21). Kullanıcının yapay zekâ izinden yakındığı bir yapay zekâ taslağında bu istisnalar geçerli değildir (SKILL.md, "Yapay zekâ taslağı").
- **İyi metne dokunma.** Zaten iyi yazılmış bir metinde değişiklik üretme. Gereksiz her değişiklik yalnızca risk ekler.
- **Silmek de bir değişikliktir.** Bir değerlendirmeyi, uyarıyı ya da atfı silmeden önce sor: Bu söz olmadan iddia daha geniş, daha kesin ya da başkasına ait mi oluyor? Öyleyse dolgu değildir (ANL-15). Sildiğin değerlendirme ve uyarı cümlelerini kullanıcıya bildir.
- **Dedektör vaadi yok.** Bu katalog metni okura daha doğal getirmek içindir, yapay zekâ dedektörlerini atlatmak için değil.

**Kimlik düzeni:** Üç harflik bir küme kısaltması ve iki haneli bir numara (ör. `KLS-03`). Kısaltmalar, ANL kodları gibi Türkçe karakter içermez; böylece arama ve eşleme klavyeden ve büyük-küçük harf dönüşümünden etkilenmez.

**Kaynak etiketleri:** Köşeli ayraçtaki etiketler dosyanın sonundaki **Kaynaklar** bölümüne gider. `[gözlem; kaynak doğrulanamadı]` etiketli bilgi, bu katalog için yapılmış bir gözlemdir ve okunan bir kaynakla doğrulanmamıştır.

**Öteki dosyalar:** Bir kalıbın **Ayrıntı** satırı, aynı konuyu daha geniş anlatan dosyaya gönderir. Noktalama ve yazım kuralları `yazim-noktalama.md`'de (YN, YZ, YA kodları), bağlaçların işlevleri `baglaclar-ve-gecisler.md`'de, cümle dönüşümleri ve ritim `cumle-ritmi.md`'de (D kodları) anlatılır. Kural bu dosyada kısa, orada ayrıntılıdır; ikisi çelişirse ayrıntılı dosya, anlamla ilgili her konuda da `anlam-kaymasi.md` kazanır.

## Dizin

| Küme | Kalıplar |
|---|---|
| **ACL** · Açılış ve kapanış | ACL-01 Açılış dolgusu · ACL-02 Sohbet açılışı ve onay · ACL-03 Sohbet kapanışı · ACL-04 Kapanış dolgusu · ACL-05 Özet kapanış · ACL-06 Şablon değerlendirme kapanışı · ACL-07 Yol haritası duyurusu |
| **KLS** · Klişe ve dolgu sözler | KLS-01 Bağlam klişeleri · KLS-02 "Söz konusu" sıklığı · KLS-03 "Önemli bir rol" ailesi · KLS-04 Önem ve miras şişirmesi · KLS-05 Süs pekiştirme · KLS-06 Moda sözcükler · KLS-07 Reklam dili · KLS-08 Vurgu dolgusu · KLS-09 Dolgu sıfat-fiil |
| **DLB** · Dil bilgisi ve sözdizimi | DLB-01 "-mektedir" yığılması · DLB-02 "Olarak" ve "olup" fazlalığı · DLB-03 "Tarafından" fazlalığı · DLB-04 Ad-fiil yığılması · DLB-05 Ağır yardımcı fiil · DLB-06 Sona eklenen yorum |
| **YPI** · Yapı ve ritim | YPI-01 Cümle uzunluğu tekdüzeliği · YPI-02 Üçlü sıralama · YPI-03 Kalıp tekrarı · YPI-04 Kendi sorup kendi cevaplama · YPI-05 Olumsuz koşutluk · YPI-06 Eş anlamlı döndürme · YPI-07 Ekleme geçişi yığılması |
| **CEV** · Çeviri etkisi | CEV-01 Çeviri deyim · CEV-02 "Sahip olmak" kalıbı · CEV-03 Gereksiz "bir" · CEV-04 Gereksiz zamir · CEV-05 İngilizce anlamıyla kullanılan sözcük · CEV-06 İngilizceden kelime kelime çevrilmiş isim zinciri |
| **NOK** · Noktalama ve yazım | NOK-01 Uzun çizgi · NOK-02 Başlık büyük harfi · NOK-03 Ünlem bolluğu · NOK-04 İki noktalı ilan |
| **BIC** · Biçim ve yerleşim | BIC-01 Madde işaretine düşkünlük · BIC-02 Kalın yazı bolluğu · BIC-03 Emoji · BIC-04 Gereksiz başlık · BIC-05 Sohbet ve şablon kalıntısı · BIC-06 Görüntülenmeyen Markdown işareti |
| **TON** · Ton ve ses | TON-01 Yapay samimiyet · TON-02 Aşırı genelleme · TON-03 Belirsiz atıf · TON-04 Sorumluluk reddi · TON-05 Temkin yığılması · TON-06 Zorunlu iyimserlik |

## İz sayılmayanlar

Şunlar tek başına yapay zekâ izi değildir. Bunları "düzeltme".

- **Kusursuz yazım ve noktalama.** Usta yazarlar da hatasız yazar [WP-AI].
- **Karışık register.** Resmi ve gündelik dilin karışması teknik bir geçmişten ya da birden çok yazardan gelebilir [WP-AI].
- **Tek başına geçiş sözü.** "Ayrıca" gibi sözleri insanlar da kullanır; ancak yığıldığında kalıptır (YPI-07) [WP-AI].
- **Kıvrık tırnak (“ ”).** TDK'nin kendi kılavuzunda kullandığı işarettir [TDK-NOK].
- **Akademik metinde "-mektedir".** Türün olağan dilidir (DLB-01) [AKS11].
- **Sözcük çeşitliliği.** Bulgular çelişkilidir: İngilizce denemelerde ChatGPT'nin sözcük çeşitliliği öğrencilerden yüksek [HER23], Türkçe metinlerde ise düşük bulunmuştur [BA26]. Çeşitlilik tek başına bir ölçüt değildir.

---

## ACL · Açılış ve kapanış

### ACL-01 · Açılış dolgusu

- **Belirti:** Metnin ya da paragrafın genel bir zaman çerçevesiyle açılması: "Günümüzde", "Günümüz dünyasında", "Teknolojinin hızla geliştiği çağımızda", "Hızla değişen dünyamızda".
- **Neden yapay görünür:** Konuyu bir sınır çizmeden geniş bir eğilime bağlar. Yapay zekâ metni sıradan konuları büyük eğilimlere bağlamaya yatkındır [WP-AI]. "Günümüzde" açılışının Türkçe model çıktılarındaki sıklığı ölçülmüş değildir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Söz bir değişimin ya da olgunun zamanını sınırlamıyorsa sil ve cümleye asıl konuyla başla. Sınırlıyorsa koru.
- **Dokunma:** Zamanı sınırlayan sözler ("Son yıllarda bildirimler arttı."); geçmişle bugünü karşılaştıran cümle ("Eskiden …, günümüzde …"); tarih anlatısı; konuşma ve hitabet metninin açılışı; yazarın bilinçli çağ yorumu.
- **Anlam riski:** ANL-15 (zaman sınırı düşer), ANL-08 (zaman), ANL-02 (silinen çerçevede "giderek" gibi bir derece sözü varsa o da gider).
- **Önce → Sonra:** *Günümüzde pek çok belediye, bisiklet yollarını ana caddelere bağlamaktadır.* → *Pek çok belediye, bisiklet yollarını ana caddelere bağlamaktadır.*

### ACL-02 · Sohbet açılışı ve onay

- **Belirti:** Metne yapışmış sohbet yanıtı başı: "Elbette!", "Tabii ki, memnuniyetle!", "Harika bir soru!", "Çok haklısınız.", "İşte …:".
- **Neden yapay görünür:** Sohbet arayüzünde kullanıcıya söylenen sözler metne taşınmıştır; "Çok haklısınız!" gibi onay sözleri de bu dilin parçasıdır [WP-AI].
- **Ne yapılır:** Sil. İçerik ilk cümleden başlasın.
- **Dokunma:** Gerçek bir yazışmada kabul ya da söz ("Elbette, cuma günü gönderirim." bir taahhüttür); aktarılan ya da örnek diyalog; deneme ve köşe yazısında yazarın sesi olarak "Elbette" (bir kabul, ironi ya da itirazın girişi); mektup ve e-postanın olağan selamlaması ("Merhaba Selin Hanım,", "Sayın Müdür,"): Hitap biçimin ve ilişkinin parçasıdır (ANL-11).
- **Anlam riski:** ANL-07 (kabul ve taahhüt düşer), ANL-21 (ironik "Elbette"), ANL-18.
- **Önce → Sonra:** *Elbette! İşte toplantı notlarının kısa bir özeti: Bütçe kalemleri gözden geçirildi ve iki satın alma talebi ertelendi.* → *Toplantı notlarının kısa özeti: Bütçe kalemleri gözden geçirildi ve iki satın alma talebi ertelendi.*

### ACL-03 · Sohbet kapanışı

- **Belirti:** "Umarım yardımcı olur!", "Umarım bu bilgiler işinize yarar.", "Başka bir konuda yardımcı olmamı ister misiniz?", "İsterseniz bunu bir tabloya da dönüştürebilirim."
- **Neden yapay görünür:** Sohbet botunun kullanıcıya yönelik iş birliği dili metne taşınmıştır [WP-AI].
- **Ne yapılır:** Botun dilek bildirdiği ya da hizmet teklif ettiği satırları sil. Gerçek bir iletişim davetini olduğu gibi bırak.
- **Dokunma:** Kullanıcının kendi e-postasındaki "Sorunuz olursa bana yazın." gerçek bir davettir: kipini (rica, emir), koşulunu ve kapsamını koru. Müşteri yazışmasındaki iletişim kanalı bilgisi. E-postanın imza bloğu, unvanı ve olağan kapanış sözü ("Saygılarımla", "İyi çalışmalar"). Resmî yazının "… arz ederim." ya da "… rica ederim." kapanışı makamlar arasındaki ilişkiyi gösterir; değiştirme (ANL-11).
- **Anlam riski:** ANL-03 (davete "her zaman" eklemek), ANL-07 ("yazın" → "yazabilirsiniz": rica izne döner), ANL-17 ("sorunuz olursa" koşulu düşer).
- **Önce → Sonra:** *Ekte vardiya çizelgesinin son hâlini bulabilirsiniz. Umarım bu bilgiler işinize yarar! Başka bir sorunuz olursa lütfen çekinmeden bana yazın.* → *Ekte vardiya çizelgesinin son hâlini bulabilirsiniz. Başka bir sorunuz olursa lütfen çekinmeden bana yazın.*

### ACL-04 · Kapanış dolgusu

- **Belirti:** Son paragrafın "Sonuç olarak", "Özetle", "Kısacası", "Tüm bunlar göz önüne alındığında" ile açılması.
- **Neden yapay görünür:** Eski modeller metni "Sonuç" bölümü ve "özetle" sözleriyle kapatmaya yatkındı [WP-AI]. İncelenen bir ChatGPT-4 denemesi de "Sonuç olarak" ile başlayan bir paragrafla biter [COS25, s. 388].
- **Ne yapılır:** Bağlaç yalnızca kapanışı duyuruyorsa sil, ardından gelen cümleyi koru. Bir çıkarımı önceki bulgulara bağlıyorsa koru ya da aynı bağı kuran bir sözle değiştir ("bu yüzden").
- **Dokunma:** Makale ve raporun "Sonuç" başlıklı bölümü (başlığın ve bölümün kendisi); bulgudan yeni bir çıkarım bağlayan "sonuç olarak"; hukuki metinde hükme geçiş; uzun belgede yönetici özeti. Kısa bir özet paragrafının son cümlesinde yalnızca toparlama işi gören "Sonuç olarak" ise dolgudur ve silinebilir.
- **Anlam riski:** ANL-06 (çıkarım bağı düşer), ANL-07 (kapanıştaki önerinin kipi), ANL-01 (temkin).
- **Ayrıntı:** `baglaclar-ve-gecisler.md` → "sonuç olarak / sonuçta", "kısacası" ve Yol 1.
- **Önce → Sonra:** *Sonuç olarak, düzenli mola vermek, uzun süre ekran başında çalışan kişilerde göz yorgunluğunu azaltmaya yardımcı olabilir.* → *Düzenli mola vermek, uzun süre ekran başında çalışan kişilerde göz yorgunluğunu azaltmaya yardımcı olabilir.*

### ACL-05 · Özet kapanış

- **Belirti:** Her paragrafın, paragrafı yineleyen bir cümleyle bitmesi: "Kısacası, …", "Bu da … ne kadar önemli olduğunu göstermektedir."
- **Neden yapay görünür:** Bölüm sonu özetleri eski model çıktılarında belirgindi [WP-AI]. Aynı içeriği yinelemek, yapay zekâ metinlerinde ölçülen sözcük tekrarını artırır [BA26, s. 430].
- **Ne yapılır:** Özet cümlesi paragrafta zaten söyleneni yineliyorsa sil. Yeni bir değerlendirme, derece ya da öneri taşıyorsa koru.
- **Dokunma:** Ders kitabı ve eğitim materyali (özet bir öğretim aracıdır); tez bölümlerinin sonundaki ara özetler; konuşma metni; uzun raporda bölüm özeti.
- **Anlam riski:** ANL-02 (özetteki derece sözü düşer), ANL-06, ANL-15.
- **Önce → Sonra:** *Depo girişindeki yeni rampa eskisinden daha güvenli. Eğimi azaltıldı ve yüzeyine kaymaz kaplama döşendi. Kısacası, yenilenen rampa artık daha güvenli bir geçiş sunuyor.* → *Depo girişindeki yeni rampa eskisinden daha güvenli. Eğimi azaltıldı ve yüzeyine kaymaz kaplama döşendi.*

### ACL-06 · Şablon değerlendirme kapanışı

- **Belirti:** "Tüm bu zorluklara rağmen … umut verici bir gelecek vadetmektedir.", "Her yenilik gibi bunun da hem avantajları hem dezavantajları vardır.", "Doğru adımlar atıldığında … büyük bir potansiyel taşımaktadır."
- **Neden yapay görünür:** Zorlukları ve gelecek beklentisini sıralayan kalıp kapanış paragrafı, yapay zekâ metninin bilinen bir izidir [WP-AI]. "Hem avantajı hem dezavantajı var" denge kalıbının sıklığı ölçülmemiştir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Kalıbı sadeleştir. Değerlendirmeyi, karşıtlık bağını ("rağmen") ve öngörünün temkinini koru. Kaynakta dayanağı olmayan bir öngörü varsa yazara sor.
- **Dokunma:** Akademik tartışmadaki sınırlılıklar ve ileri çalışma önerileri türün gereğidir; proje başvurusunda "beklenen etki"; strateji ve yatırım raporunda değerlendirme.
- **Anlam riski:** ANL-06 (karşıtlık bağı), ANL-01 (öngörünün temkini), ANL-16 (vaat sonuca döner), ANL-08 (gelecek), ANL-03 ("tüm bu" kapsamı).
- **Ayrıntı:** `baglaclar-ve-gecisler.md` → Beklenti çelişkisi ve kabul ("buna rağmen").
- **Önce → Sonra:** *Tüm bu zorluklara rağmen, kooperatifin yeni soğuk hava deposu bölge üreticileri için umut verici bir gelecek vadetmektedir.* → *Tüm bu zorluklara rağmen kooperatifin yeni soğuk hava deposu, bölge üreticilerinin geleceği için umut verici.*

### ACL-07 · Yol haritası duyurusu

- **Belirti:** "Bu yazıda … ele alacağız.", "Gelin, birlikte inceleyelim!", "Aşağıda bu konunun tüm yönlerini ayrıntılı bir şekilde açıklayacağım."
- **Neden yapay görünür:** Kısa bir metinde içeriği önceden duyurmak, içerikten önce gelen bir dolgu katmanı yaratır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Davet ve coşku sözlerini sil. Duyurudaki kapsam bilgisini ("üç yol", "yalnızca kışlık bakım") koru. Duyuruyu bir olguya çevirme.
- **Dokunma:** Akademik makale ve tezde amaç cümlesi ve bölüm planı ("Bu çalışmada … incelenmektedir.") türün gereğidir; uzun rapor ve kılavuzda yönlendirme; ders anlatımı.
- **Anlam riski:** ANL-16 (vaat olguya döner), ANL-03 ("üç yol" → "birkaç yol"), ANL-11 (kaynakta olmayan "biz").
- **Önce → Sonra:** *Bu yazıda, kışın balkon bitkilerini korumanın üç yolunu ayrıntılı bir şekilde ele alacağız. Gelin, birlikte inceleyelim!* → *Bu yazıda kışın balkon bitkilerini korumanın üç yolunu ayrıntılı olarak ele alacağız.*

---

## KLS · Klişe ve dolgu sözler

### KLS-01 · Bağlam klişeleri

- **Belirti:** "Bu bağlamda", "Bu çerçevede", "Bu doğrultuda", "Bu noktada", "Bu açıdan bakıldığında" sözlerinin cümle başlarında sık sık ve belirli bir bağ kurmadan kullanılması.
- **Neden yapay görünür:** "Bağlam" sözlükte olaylar, durumlar ve ilişkilerden oluşan bir örgüyü anlatır [TDK-GTS]. Belirli bir ilişkiyi göstermeden kullanılınca dolguya döner. Sıklık bilgisi gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Söz belirli bir bağ kuruyorsa o bağı açıkça söyleyen bir sözle değiştir ("bu amaçla", "bu konuda"). Kurmuyorsa sil. Arka arkaya gelenlerden yalnızca boş olanı sil.
- **Dokunma:** Resmi yazışma ve mevzuatta "bu çerçevede", "bu doğrultuda" yerleşiktir ve çoğu zaman belirli bir karara ya da talimata gönderme yapar; akademik metinde seyrek kullanımı olağandır.
- **Anlam riski:** ANL-06 (yanlış bağ: "bu doğrultuda" → "bu yüzden" sebep ekler), ANL-16 (amaç), ANL-15 (gönderge).
- **Ayrıntı:** `baglaclar-ve-gecisler.md` → Yol 1 ve İşlev envanteri (yerine konacak sözün ilişkisi).
- **Önce → Sonra:** *Kurul, yangın tatbikatlarının yılda iki kez yapılmasını kararlaştırdı. Bu bağlamda, ilk tatbikat mart ayında yapılacaktır.* → *Kurul, yangın tatbikatlarının yılda iki kez yapılmasını kararlaştırdı. İlk tatbikat mart ayında yapılacaktır.*

### KLS-02 · "Söz konusu" sıklığı

- **Belirti:** Bir paragrafta birden çok "söz konusu"; "bu" ile gösterilebilecek yakın göndergeler için kullanılması; "var" yerine "söz konusu olmak" ("bir gecikme söz konusudur").
- **Neden yapay görünür:** Söz, sözlükte "sözü edilen, üzerinde konuşulan" anlamında bir sıfattır [TDK-GTS]; resmi bir gösterme aracıdır ve gündelik metinde yığılınca bürokratik durur. Sıklık bilgisi gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Gönderge açıksa "bu" yap. "Söz konusu olmak" varlık bildiriyorsa "var" ya da (temkinle) "olabilir" yap. Gönderge belirsizleşecekse adı yinele.
- **Dokunma:** Resmi yazışmada belirli bir belgeyi, kararı ya da kişiyi gösteren "söz konusu" kalır. Hukuk metninde gönderge kesinliği taşır. Önceki bir bölümdeki belirli bir grubu gösteriyorsa "bu X" yap. "Erteleme söz konusu değildir" bir ret ya da olanaksızlık bildirir.
- **Anlam riski:** ANL-15 (gönderge), ANL-19 (belirtililik), ANL-04 ve ANL-07 ("söz konusu değil" = "olmayacak").
- **Önce → Sonra:** *Söz konusu yazılım güncellemesi cuma gecesi yüklenecektir. Söz konusu güncelleme sırasında kısa bir kesinti söz konusu olabilir.* → *Bu yazılım güncellemesi cuma gecesi yüklenecektir. Güncelleme sırasında kısa bir kesinti olabilir.*

### KLS-03 · "Önemli bir rol oynamaktadır" ailesi

- **Belirti:** "önemli bir rol oynamaktadır", "kilit bir rol üstlenmektedir", "katkıda bulunmaktadır", "olanak sağlamaktadır", "zemin hazırlamaktadır", "büyük önem taşımaktadır" kalıplarının aynı metinde yinelenmesi.
- **Neden yapay görünür:** 147 ChatGPT-4o mini metninde en sık deyim "rol oynamak"tır (105 kez). "Olanak sağlamak" 99, "katkıda bulunmak" 87, "zemin hazırlamak" 20 kez geçer. Aynı konulardaki 147 öğrenci metninde "rol oynamak" en sık 50 deyim arasında yoktur; "katkıda bulunmak" 7 kez geçer [BA26, s. 427]. Sözlükte "rol oynamak"ın mecaz anlamı zaten "önemli etkisi olmak"tır [TDK-GTS].
- **Ne yapılır:** İlişkinin türünü koruyarak kalıbı çeşitlendir. Katkıysa "payı var", "katkı sağlar"; önem değerlendirmesiyse "için önemlidir". Hiçbirini neden fiiline ("belirler", "artırır", "çok etkiler") çevirme.
- **Dokunma:** Akademik metinde tek tük "önemli rol oynar" olağandır; başka bir çalışmanın bulgusunu aktaran cümlede söz aynen kalır; tiyatro ve sinemada gerçek rol.
- **Anlam riski:** ANL-05 (katkı nedenselliğe döner), ANL-02 ("önemli", "kilit", "kritik" ayrı derecelerdir), ANL-22 (aktarılan bulgu).
- **Önce → Sonra:** *Kütüphaneler, okuma alışkanlığının gelişmesinde önemli bir rol oynamaktadır. Gezici kütüphaneler de kırsal bölgelerde kitaba erişime katkıda bulunmaktadır.* → *Kütüphanelerin okuma alışkanlığının gelişmesinde önemli bir payı var. Gezici kütüphaneler de kırsal bölgelerde kitaba erişime katkı sağlıyor.*

### KLS-04 · Önem ve miras şişirmesi

- **Belirti:** Sıradan bir olguyu büyük bir anlama bağlayan kalıplar: "önemini bir kez daha gözler önüne sermiştir", "kalbinde kalıcı bir iz bırakmıştır", "yeni bir çağın kapılarını aralamaktadır", "bir mihenk taşıdır", "tarihe geçmiştir".
- **Neden yapay görünür:** Yapay zekâ metni konuyu önem, miras ve geniş eğilim sözleriyle şişirir [WP-AI]. ChatGPT metinlerinde "iz bırakmak" 12, "ilham vermek" 10, "gözler önüne sermek" 5, "kapı aralamak" 5 kez geçer; hiçbiri öğrenci metinlerinin en sık 50 deyimi arasında değildir [BA26, s. 427].
- **Ne yapılır:** Mecazı aynı güçte sade bir sözle değiştir ("gözler önüne sermek" → "göstermek"). Değerlendirmeyi silme, çünkü bir iddiadır. Dayanaksız görünüyorsa yazara sor.
- **Dokunma:** Anma yazısı, tören konuşması, tarih anlatısı, edebi metin; yazarın bilinçli üslubu.
- **Anlam riski:** ANL-02 (değerlendirmenin gücü), ANL-22 (yorum olguya döner), ANL-15 ("bir kez daha" bilgisi).
- **Önce → Sonra:** *Mahalle derneğinin düzenlediği fidan dikme etkinliği, gönüllülüğün gücünü bir kez daha gözler önüne sermiş ve katılımcıların kalbinde kalıcı bir iz bırakmıştır.* → *Mahalle derneğinin düzenlediği fidan dikme etkinliği, gönüllülüğün gücünü bir kez daha göstermiş ve katılımcılarda kalıcı bir iz bırakmıştır.*

### KLS-05 · Süs pekiştirme

- **Belirti:** Ölçülebilir bir büyüklük bildirmeyen, çoğu zaman üst üste binen pekiştirmeler: "son derece kritik", "inanılmaz derecede", "muazzam", "hayati öneme sahip", "olağanüstü".
- **Neden yapay görünür:** 2024 PubMed özetlerinde fazla kullanılan sözcüklerin hemen hepsi içerik değil üslup sözcüğüdür; 319 sözcüğün yaklaşık üçte ikisi fiil, altıda biri sıfattır ("crucial" örnekler arasındadır) [KOB25]. "Kritik" sözlükte "endişe verici, çok tehlikeli (durum)" ya da "nazik" anlamındadır; "çok önemli" anlamındaki kullanım sözlükte yoktur [TDK-GTS].
- **Ne yapılır:** Pekiştirme yığılmasında birini bırak ("son derece kritik bir öneme sahip" → "son derece önemli"). Tek bir süsü eş güçte sade bir sözle değiştir ("inanılmaz derecede hızlı" → "çok hızlı"). Gücü düşürme.
- **Dokunma:** Derece sözleri ("büyük ölçüde", "anlamlı düzeyde", "neredeyse") iddianın parçasıdır (ANL-02); tıpta ve mühendislikte "kritik" bir terimdir (kritik hasta, kritik sıcaklık); güvenlik uyarısındaki vurgu; reklamda ve konuşma dilinde abartı türün sesidir.
- **Anlam riski:** ANL-02 (güç düşer ya da artar), ANL-14 (terim), ANL-07 (uyarının gücü).
- **Önce → Sonra:** *Laboratuvarda koruyucu gözlük takmak son derece kritik bir öneme sahiptir.* → *Laboratuvarda koruyucu gözlük takmak son derece önemlidir.*

### KLS-06 · Moda sözcükler

- **Belirti:** "yolculuk" (öğrenme yolculuğu, sürdürülebilirlik yolculuğu), "serüven", "ekosistem" (girişim ekosistemi), "sinerji", "vizyon", "değer katmak", "keşfetmek".
- **Neden yapay görünür:** Sözlükte "yolculuk"un mecaz anlamı bir zamana ya da mekâna zihinsel olarak gitmektir; "ekosistem" yalnızca ekolojik bir sistemdir [TDK-GTS]. Süreç ya da kurum ağı anlamındaki kullanımlar sözlükte yoktur. İncelenen bir ChatGPT-4 denemesinde "yolculuk" 3, "serüven" 2 kez geçer ve metin bir "keşif yolculuğu" mecazıyla biter [COS25, s. 381–382, 388].
- **Ne yapılır:** Mecazın arkasındaki somut sözü kullan ("kariyer yolculuğu" → "kariyer", "sürdürülebilirlik yolculuğu" → "sürdürülebilirlik çalışmaları"). Somut karşılık kaynaktan çıkmıyorsa uydurma. Sade karşılık aynı şeyi anlatmıyorsa ("sinerji" ile "iş birliği" aynı değildir) sözü bırak.
- **Dokunma:** "Dijital dönüşüm" ve "kentsel dönüşüm" sözlükte kayıtlı birleşik sözlerdir [TDK-GTS]; program, proje ve kurum adları; biyolojide "ekosistem"; gezi yazısında gerçek "yolculuk"; yazarın bilinçli mecazı.
- **Anlam riski:** ANL-11 (kaynakta olmayan somut özne ya da eylem), ANL-14 (terim ve özel ad), ANL-16 (süreç tamamlanmış gibi görünür).
- **Önce → Sonra:** *Şirketimizin sürdürülebilirlik yolculuğunda tedarikçilerimizle güçlü bir sinerji yaratmayı hedefliyoruz.* → *Sürdürülebilirlik çalışmalarımızda tedarikçilerimizle güçlü bir sinerji yaratmayı hedefliyoruz.*

### KLS-07 · Reklam dili

- **Belirti:** Bilgi veren metinde tanıtım sözleri: "eşsiz", "büyüleyici", "göz kamaştırıcı", "benzersiz bir deneyim", "zengin kültürel mirasıyla", "doğanın kalbinde", "başarıya imza atmak".
- **Neden yapay görünür:** Basın bülteni ya da gezi rehberi diline kayan tanıtım üslubu 2023–2025 modellerinde belirgindi [WP-AI].
- **Ne yapılır:** Övgüyü eş güçte sade bir değerlendirmeyle değiştir ya da kaynakta varsa somut bilgiye bağla. Ürünle ilgili somut bir övgüyü silme; eş güçte sade bir sözle değiştir. Ürünle ilgisi olmayan genel bir slogan ya da kapanış yargısı ("teknoloji geleceği şekillendirmeye hazır") dolgudur: Sil ve kısa notta sildiğini bildir (TON-06 ile aynı kural).
- **Dokunma:** Tanıtım broşürü, turizm metni, ürün sayfası, davetiye; kullanıcı yalnızca "doğallaştır" dediyse övgünün gücünü koru.
- **Anlam riski:** ANL-02 (değerlendirmenin gücü), ANL-22 (övgünün sahibi: kurum mu, bağımsız bir kaynak mı), ANL-06 (araç bağı: "satarak").
- **Önce → Sonra:** *Kooperatif, ilk yılında 4.000 kavanoz reçel satarak göz kamaştırıcı bir başarıya imza attı.* → *Kooperatif ilk yılında 4.000 kavanoz reçel satarak çok büyük bir başarı elde etti.*

### KLS-08 · Vurgu dolgusu

- **Belirti:** "Şunu belirtmek gerekir ki", "Unutulmamalıdır ki", "Önemle vurgulamak gerekir ki", "Altını çizmek gerekir ki", "Akılda tutulması gereken nokta şudur:".
- **Neden yapay görünür:** Eski modeller bir şeyin "belirtilmesinin önemli olduğunu" söyleyen öğretici uyarılar eklemeye yatkındı [WP-AI].
- **Ne yapılır:** Kalıbı sil, ardından gelen önermeyi koru. Kalıp okurdan bir şey istiyorsa (bir uyarıysa) bu gücü yüklemde koru.
- **Dokunma:** Güvenlik talimatında ve eğitim materyalinde "Unutmayın:" bir uyarıdır; hukuki görüşte "belirtmek gerekir ki" yazarın görüşünü işaretleyebilir; konuşma metni.
- **Anlam riski:** ANL-07 (uyarının gücü), ANL-22 (görüş işareti), ANL-04 ("Unutulmamalıdır" olumsuz biçimlidir; silerken kutbu karıştırma).
- **Önce → Sonra:** *Şunu belirtmek gerekir ki, kampanya yalnızca mağaza içi alışverişlerde geçerlidir.* → *Kampanya yalnızca mağaza içi alışverişlerde geçerlidir.*

### KLS-09 · Dolgu sıfat-fiil

- **Belirti:** Ad zaten belliyken eklenen sıfat-fiiller: "elde edilen bulgular", "yapılan çalışmalar", "gerçekleştirilen analizler", "kullanılan yöntem", "mevcut durum", "ilgili birimler", "sorumlu olan birim". Aracı bildiren ada eklenen "kullanılarak" ve "yöntemiyle": "regresyon analizi kullanılarak değerlendirildi", "görüşme yöntemiyle toplandı".
- **Neden yapay görünür:** Talimatla ayarlanmış modeller bilgi yoğun, ad ağırlıklı bir üsluba kayar [REI25]. Türkçede bunun sıfat-fiil öbekleriyle görünmesi gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Sıfat-fiil ayırt edici bir bilgi taşımıyorsa sil ("elde edilen bulgular" → "bulgular", "sorumlu olan birim" → "sorumlu birim"). Ayırt ediyorsa koru. "… kullanılarak" ve "… yöntemiyle" yalnızca aracı yineliyorsa ada "ile" ekle: "analiz kullanılarak" → "analizle".
- **Dokunma:** "Bu çalışmada elde edilen bulgular" başka çalışmalardan ayırır; "yapılan" ile "planlanan" ayrı durumlardır; "mevcut yönetmelik" yürürlükteki düzenlemeyi gösterir; hukukta "ilgili" belirli bir bağlantı kurar; "olan" bir grubu ötekilerden ayırıyorsa kalır ("riskli olan iki hat"). Akademik yöntem bölümünde yöntemin, ölçeğin ve testin adı bilgidir: Yalnızca "kullanılarak" ya da "yöntemiyle" fazlalığı sadeleşir, ad silinmez.
- **Anlam riski:** ANL-15 (sınır çizen söz), ANL-16 (yapılan/planlanan), ANL-23 (yürürlük), ANL-08, ANL-14 (yöntem ve test adı).
- **Ayrıntı:** Uzun sıfat-fiil zincirini çözmek için `cumle-ritmi.md` → D4.
- **Önce → Sonra:** *Yapılan anket çalışmasından elde edilen veriler, katılımcıların yarısından fazlasının servis saatlerini uygun bulmadığını göstermektedir.* → *Anket verileri, katılımcıların yarısından fazlasının servis saatlerini uygun bulmadığını göstermektedir.*

---

## DLB · Dil bilgisi ve sözdizimi

### DLB-01 · "-mektedir" yığılması

- **Belirti:** E-posta, blog, duyuru ya da ürün açıklamasında art arda yüklemlerin "-mektedir/-maktadır" ile kurulması.
- **Neden yapay görünür:** "-mAktA" günlük konuşmada hemen hiç kullanılmaz; ağırlıkla resmi, idari, ticari, akademik ve öğretici metinlerde görülür, edebi metinde de yaygın değildir [AKS11, s. 337]. Bu dağılımı Ergin (1977) ve Göksel ve Kerslake (2005) de kaydeder [AKS11'in aktarımıyla, s. 336–337]. Akaslan farkın biçemsel değil sözcelemsel olduğunu savunur; kullanım dağılımı ise değişmez. "-mekte-dir" ayrıca her zaman kesinlik katar [AKS11, s. 336]. Gündelik metinde zincirleme kullanım bürokratik bir ses verir.
- **Ne yapılır:** Gündelik registerda süren durumu "-iyor", genel doğruyu geniş zamanla yaz. Zamanı ve görünüşü koru. "-mıştır"ı yalnızca tamamlanmışlık bildiriyorsa "-dı" yap (ANL-09).
- **Dokunma:** Akademik, resmi, idari ve hukuki metinde "-mektedir" zinciri türün olağan dilidir; hafif seviyede akademik metne dokunma; dergi ya da kurum kuralı belirler; mevzuatta geniş zaman yükümlülük bildirir.
- **Anlam riski:** ANL-08 (süren durum bitmiş olaya döner), ANL-09, ANL-10 (-DIr kesinliği), ANL-07.
- **Ayrıntı:** `cumle-ritmi.md` → Teşhis (3. işaret) ve D6.
- **Önce → Sonra:** *Kafeteryada bu hafta bakım çalışması yapılmaktadır. Bu nedenle öğle yemeği ikinci katta verilmektedir.* → *Kafeteryada bu hafta bakım çalışması yapılıyor. Bu nedenle öğle yemeği ikinci katta veriliyor.*

### DLB-02 · "Olarak" ve "olup" fazlalığı

- **Belirti:** İşlevsiz "olarak": "yaklaşık olarak 40", "ilk olarak … ikinci olarak", "X olarak bilinen". İki yüklemi "olup" ile tek cümleye bağlamak: "toplanmış olup değerlendirilmiştir".
- **Neden yapay görünür:** Resmi yazışma kalıplarının her türe taşınmasıdır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** İşlevsiz "olarak"ı sil ("yaklaşık 40", "önce"). "Olup" ile bağlanmış yüklemleri "ve" ile bağla ya da iki cümleye ayır. Her yüklemin zamanını ve kipini koru.
- **Dokunma:** "Olarak" bir görev, nitelik ya da biçim bildiriyorsa bilgidir ("gözlemci olarak katıldı", "geçici olarak kapatıldı", "yazılı olarak bildirilir"); "genel olarak" bir kapsam ya da temkin sözüdür, silinirse iddia genişler (ANL-03, ANL-15); resmi yazışma ve mevzuatta "olup" yerleşik bir bağlama aracıdır.
- **Anlam riski:** ANL-07 (birleştirince kip aktarımı), ANL-06 (virgülle bağlarken sebep okuması), ANL-01 ve ANL-03 ("yaklaşık" sayının yanında kalır), ANL-19 ("temsilci olarak" düşerse rol kaybolur).
- **Önce → Sonra:** *Yeni otopark yaklaşık olarak 120 araç kapasiteli olup ilk olarak personelin kullanımına açılacaktır.* → *Yeni otopark yaklaşık 120 araç kapasitelidir ve önce personelin kullanımına açılacaktır.*

### DLB-03 · "Tarafından" fazlalığı

- **Belirti:** Etken cümlenin daha doğal olduğu yerde edilgen ve "tarafından": "Liste sorumlu hemşire tarafından hazırlandı.", "Etkinlik ekibimiz tarafından organize edilmiştir."
- **Neden yapay görünür:** "Tarafından", edilgen cümlede eylemi yapanı gösteren edattır [TDK-GTS]. Gündelik metinde sık kullanımının İngilizcedeki "by" yapısını andırdığı gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Eylemi yapan belliyse ve tek yüklem varsa etken cümleye çevir. Yapanı, eylemin türünü (yaptı mı, yaptırdı mı) ve zamanı koru. Birden çok yüklem varsa "tarafından"ın hangilerini kapsadığına bak; emin değilsen bırak.
- **Dokunma:** Sözleşme, tutanak, karar ve raporda yükümlüyü ya da imzalayanı adlandıran "tarafından" bilgidir; künye ("… tarafından çevrilmiştir"); akademik metinde edilgen anlatım tercihi.
- **Anlam riski:** ANL-11 (eylemi yapan), ANL-19 (çatı ve ettirgen), ANL-12 (vurgunun yeri).
- **Ayrıntı:** Edilgen kalması gereken cümlede "tarafından" yerine "-ce" için `cumle-ritmi.md` → D4.
- **Önce → Sonra:** *Yeni nöbet listesi sorumlu hemşire tarafından hazırlandı.* → *Yeni nöbet listesini sorumlu hemşire hazırladı.*

### DLB-04 · Ad-fiil yığılması

- **Belirti:** Eylemi ada çevirip yardımcı fiile yüklemek: "değerlendirilmesi yapılmalıdır", "incelenmesinin ardından", "yapılmasının sağlanması", "artırılmasına yönelik çalışmaların yürütülmesi".
- **Neden yapay görünür:** Talimatla ayarlanmış modeller adlaştırmayı insanlardan yaklaşık 1,5–2 kat (GPT-4o yaklaşık 2,1 kat) sık kullanır [REI25]. ChatGPT denemelerinde de adlaştırma daha sıktır [HER23]. Bu bulgular İngilizce içindir; Türkçe için ölçülmemiştir.
- **Ne yapılır:** Eylemi yüklemde fiil olarak söyle. Kipi (gereklilik, öneri), çatıyı ve sırayı koru. "Sağlanması" birinin bir işi yaptırmasını ya da güvence altına almasını bildiriyorsa bu katmanı koru.
- **Dokunma:** Mevzuat ve resmi yazı (adlaştırma yükümlüyü bilinçli olarak açık bırakabilir); başlık ve madde başlıkları; terimleşmiş adlar ("risk değerlendirmesi").
- **Anlam riski:** ANL-07 (gereklilik), ANL-19 ("yapılmasının sağlanması" ile "yapılması" aynı değildir), ANL-11, ANL-16.
- **Önce → Sonra:** *Toplantı tutanağının incelenmesinin ardından bütçe kaleminin yeniden değerlendirilmesi yapılmalıdır.* → *Toplantı tutanağı incelendikten sonra bütçe kalemi yeniden değerlendirilmelidir.*

### DLB-05 · Ağır yardımcı fiil

- **Belirti:** Yalın fiil yerine "gerçekleştirmek", "sağlamak", "bulunmak", "yer almak": "toplantı gerçekleştirildi", "katılım sağlandı", "ziyarette bulunuldu", "listede yer almaktadır"; "var" yerine "bulunmaktadır": "binada iki acil çıkış bulunmaktadır".
- **Neden yapay görünür:** Sözlük "gerçekleştirmek"in karşılıkları arasında düpedüz "yapmak"ı verir [TDK-GTS]. "Sağla-" ChatGPT metinlerinde %0,522, öğrenci metinlerinde %0,377 oranında geçer; "sun-" yalnızca ChatGPT metinlerinin en sık 50 sözcüğü arasındadır; "olanak sağlamak" 99, "… hâline gelmek" 61 kez geçer [BA26, s. 426–427].
- **Ne yapılır:** Yalın fiili kullan: "katılım sağladı" → "katıldı", "gerçekleştirildi" → "yapıldı". Gündelik metinde varlık bildiren "bulunmaktadır" → "var". Zamanı ve görünüşü koru.
- **Dokunma:** Mevzuatta "sağlar" bir yükümlülük fiilidir (ANL-07); bir amacı ya da hayali "gerçekleştirmek" yerindedir; "yer almak" bir listede ya da kurulda bulunma bilgisi taşır.
- **Anlam riski:** ANL-07 (mevzuat), ANL-19 (ettirgen ile yalın), ANL-16 ("gerçekleştirildi" ≠ "planlandı").
- **Önce → Sonra:** *Dünkü eğitime 35 çalışan katılım sağlamış ve tatbikat başarıyla gerçekleştirilmiştir.* → *Dünkü eğitime 35 çalışan katılmış ve tatbikat başarıyla yapılmıştır.*

### DLB-06 · Sona eklenen yorum

- **Belirti:** Bir olgunun ardından "-arak", "bu da" ya da virgülle eklenen genel değerlendirme: "…toplayarak iş yükünü azaltmakta ve kaliteye katkı sağlamaktadır", "…, bu da ekibin uyumunu bir kez daha kanıtlamaktadır".
- **Neden yapay görünür:** Yapay zekâ metni cümle sonuna "-ing" öbekleriyle kaynaksız bir önem yorumu ekler [WP-AI]. Talimatla ayarlanmış modeller şimdiki zaman ortaçlı yan cümleleri insanlardan 2–5 kat sık kullanır [REI25]. Türkçede bu işi "-arak" ve "bu da" eklentilerinin gördüğü gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Zinciri böl: olguyu bir yüklemle söyle, sonucu "böylece" ya da "bu" ile bağla. Araç, sebep ve sonuç bağının hangi yüklemleri kapsadığını koru. Değerlendirmeyi silme; dayanaksız görünüyorsa yazara sor.
- **Dokunma:** Akademik tartışmada "…, bu da … düşündürmektedir" bir çıkarımı bulguya bağlar: temkini ve bağı koru. Haberde aktarılan değerlendirme.
- **Anlam riski:** ANL-06 (bağın kapsamı), ANL-05, ANL-01, ANL-19 ("artırılması" ≠ "artması").
- **Ayrıntı:** "böylece" ile "amacıyla" farkı için `baglaclar-ve-gecisler.md` → Sonuç; zinciri bölerken kapsam için `cumle-ritmi.md` → D3.
- **Önce → Sonra:** *Yeni kayıt sistemi, başvuruları tek ekranda toplayarak personelin iş yükünü azaltmakta ve hizmet kalitesinin artırılmasına katkı sağlamaktadır.* → *Yeni kayıt sistemi başvuruları tek ekranda topluyor; böylece personelin iş yükünü azaltıyor ve hizmet kalitesinin artırılmasına katkı sağlıyor.*

---

## YPI · Yapı ve ritim

### YPI-01 · Cümle uzunluğu tekdüzeliği

- **Belirti:** Bir paragraftaki cümlelerin neredeyse hepsinin aynı uzunlukta ve aynı kuruluşta olması.
- **Neden yapay görünür:** İnsan haber metinlerinde cümle uzunluğunun dağılımı model metinlerinden daha geniştir [MUN24]. Türkçe için bir uzunluk ölçümü bulunamadı; ancak ChatGPT'nin Türkçe bir denemesinde aynı öge dizilişinin yinelendiği gösterilmiştir [COS25, s. 382].
- **Ne yapılır:** Anlamı bozmadan iki kısa cümleyi birleştir ya da uzun bir cümleyi böl. Birleştirirken kaynakta olmayan bir bağlaç ("ama", "çünkü") ekleme. "-ıp" ile bağladığın yüklemlerin kipi aynı olsun.
- **Dokunma:** Talimat, prosedür ve güvenlik yönergesi bilinçli olarak kısa ve tekdüzedir; hukuk metninde cümle bölmek atıf düzenini bozabilir; yazarın bilinçli ritmi (kısa vurucu cümle dizisi).
- **Anlam riski:** ANL-06 (bağ eklemek), ANL-07 (-ıp ile kip aktarımı), ANL-08 (sıra), ANL-17.
- **Ayrıntı:** `cumle-ritmi.md` → Teşhis, Araçlar, D1 ve D9 (birleştirirken uyum).
- **Önce → Sonra:** *Atölye cumartesi sabahı saat onda başlayacak. Katılımcıların kendi önlüklerini getirmeleri gerekiyor. Malzemeler atölye tarafından sağlanacak. Etkinlik öğleden sonra saat ikide sona erecek.* → *Atölye cumartesi sabahı saat onda başlayıp öğleden sonra saat ikide sona erecek. Malzemeleri atölye sağlayacak; katılımcıların kendi önlüklerini getirmeleri gerekiyor.*

### YPI-02 · Üçlü sıralama

- **Belirti:** Sıfat, ad ya da yan cümlelerin hep üçlü gelmesi; üçüncü öğenin ilk ikisinden birini yinelemesi.
- **Neden yapay görünür:** Öğeleri üçlü gruplamak yapay zekâ metninin bilinen bir alışkanlığıdır ve yüzeysel noktaları kapsamlı gösterir [WP-AI]. ChatGPT'nin Türkçe denemesinde "daha güçlü ve daha mutlu" türünden koşut nitelik çiftleri kalıp hâlinde yinelenir [COS25, s. 382].
- **Ne yapılır:** Yalnızca gerçekten aynı şeyi söyleyen öğeyi sil. Yakın anlamlı nitelikler çoğu zaman ayrı iddialardır: "sezgisel, kullanıcı dostu ve kolay anlaşılır" üç iddiadır. Eş anlamlı sayılan sözcükler bile cümleye ayrı anlam katkısı yapabilir [AKB26]. Emin değilsen dokunma.
- **Dokunma:** Hitabet, slogan ve deneme (yazarın sesi); gerçekten üç aşamalı bir süreç; mevzuattaki sayımlar.
- **Anlam riski:** ANL-03 ve ANL-18 (sayımdan öğe düşer), ANL-02, ANL-14.
- **Önce → Sonra:** *Yeni randevu sistemi hızlı, pratik ve çabuk bir kullanım sunuyor.* → *Yeni randevu sistemi hızlı ve pratik bir kullanım sunuyor.*

### YPI-03 · Kalıp tekrarı

- **Belirti:** Ardışık cümlelerin aynı iskeletle kurulması: "Bazıları için X … Bazıları için Y … Bazıları için Z"; aynı "Ancak … ve … bizi daha … yapar" yapısının paragraf paragraf yinelenmesi.
- **Neden yapay görünür:** ChatGPT-3'ün Türkçe denemesinde aynı öge dizilişi ve aynı cümle iskeleti defalarca yinelenir; yazar bunu hazır kalıpların kendi içinde yinelenmesine bağlar [COS25, s. 382]. ChatGPT metinleri aynı sözcük ve deyimleri öğrenci metinlerinden daha sık yineler [BA26, s. 430–431].
- **Ne yapılır:** Yinelenen iskeletlerden birini ya da ikisini farklı kur (öğe sırası, eksiltili cümle). Her önermeyi ve niceleyiciyi koru.
- **Dokunma:** Bilinçli tekrar (anafora) yazarın sesidir; şiir, hitabet, slogan; şartname ve mevzuatta aynı kuruluş bir kesinlik aracıdır.
- **Anlam riski:** ANL-21 (bilinçli tekrar), ANL-12 (öğe sırası değişince vurgu kayar), ANL-20 (dağılım).
- **Ayrıntı:** `cumle-ritmi.md` → Teşhis (2. işaret), D7 ve Odak ve vurgu.
- **Önce → Sonra:** *Bazı öğrenciler için kütüphane bir çalışma alanıdır. Bazı öğrenciler için kütüphane bir buluşma yeridir. Bazı öğrenciler için ise kütüphane sessiz bir sığınaktır.* → *Kütüphane bazı öğrenciler için bir çalışma alanı, bazıları için bir buluşma yeri. Bazıları içinse sessiz bir sığınak.*

### YPI-04 · Kendi sorup kendi cevaplama

- **Belirti:** "Peki bu ne anlama geliyor? Çok basit: …", "Sonuç mu? …", "Neden mi? Çünkü …".
- **Neden yapay görünür:** Bilgi metninde cevabı hemen gelen soru okura bir şey sormaz, yalnızca sahne kurar [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Soruyu ve cevabı tek bir bildirim cümlesine çevir. Sebep bağını ("çünkü" → "nedeni") ve sorudaki varsayımı koru.
- **Dokunma:** Deneme, köşe yazısı, konuşma metni ve ders anlatımında retorik soru yazarın sesidir; sık sorulan sorular sayfası; röportaj; cevabı verilmeyen gerçek soru.
- **Anlam riski:** ANL-18 (soru bildirime döner), ANL-21 (retorik soru), ANL-06 (sebep bağı).
- **Ayrıntı:** `cumle-ritmi.md` → Araçlar (soru cümlesi).
- **Önce → Sonra:** *Peki neden bu kadar çok çalışan servis saatinden şikâyet ediyor? Çünkü son sefer, vardiya bitiminden yalnızca beş dakika sonra kalkıyor.* → *Bu kadar çok çalışanın servis saatinden şikâyet etmesinin nedeni, son seferin vardiya bitiminden yalnızca beş dakika sonra kalkması.*

### YPI-05 · Olumsuz koşutluk ve düzeltici çerçeve

- **Belirti:** Kimsenin ileri sürmediği bir yanılgıyı düzelterek söze girmek: "Bu yalnızca bir X değil, aynı zamanda bir Y'dir.", "Mesele X değil, Y.", "X yerine Y'ye bakmak gerekir."
- **Neden yapay görünür:** "Yalnızca X değil, Y de" ve "X değil, Y" kalıpları yapay zekâ metninin bilinen izleridir; 2026 ortasından sonraki modellerde "X yerine Y" diye düzelten çerçeveler de görülür [WP-AI]. "Aynı zamanda" ChatGPT metinlerinde en sık 14. sözcüktür (295 kez); öğrenci metinlerinde en sık 50 sözcük arasında yoktur [BA26, s. 425].
- **Ne yapılır:** "Yalnızca X değil, aynı zamanda Y" → "hem X hem Y". Karşıtlık gerçek bir görüşe cevapsa (kaynakta o görüş varsa) koru.
- **Dokunma:** Tartışma ve eleştiri metninde gerçek bir karşı görüşe cevap; hukukta "X değil, Y uygulanır" bir ayrım hükmüdür; yazarın sesi.
- **Anlam riski:** ANL-04 (olumsuzluğun neye bağlı olduğu), ANL-12 ("yalnızca" odağı), ANL-18.
- **Ayrıntı:** "yalnızca"nın yeri için `cumle-ritmi.md` → Odak ve vurgu; "hem … hem" ve "değil" için `baglaclar-ve-gecisler.md` → İşlev envanteri.
- **Önce → Sonra:** *Bu park yalnızca bir oyun alanı değil, aynı zamanda mahallenin buluşma noktasıdır.* → *Bu park hem bir oyun alanı hem de mahallenin buluşma noktası.*

### YPI-06 · Eş anlamlı döndürme

- **Belirti:** Aynı şeyi her cümlede başka bir adla anmak: "uygulama … platform … çözüm … araç"; "çalışanlar … personel … ekip üyeleri".
- **Neden yapay görünür:** Eski modellerdeki tekrar cezası, aynı özne için eş anlamlılar arasında dolaşmaya yol açar. İşaret tek başına kesin değildir [WP-AI].
- **Ne yapılır:** Adların aynı şeyi gösterdiği açıksa ("bu platform", "bu çözüm") kaynağın ilk kullandığı terime dön ve tutarlı kullan. Açık değilse dokunma ve kullanıcıya sor.
- **Dokunma:** Adlar farklı şeyleri gösteriyorsa (çalışan ≠ işçi ≠ personel; uygulama ≠ platform); hukuk ve tıp terimleri; edebi metinde bilinçli çeşitleme.
- **Anlam riski:** ANL-14 (terim), ANL-03 (kapsam: "platform" daha geniş olabilir), ANL-15 (gönderge).
- **Ayrıntı:** Bağlaçlar arasında dolaşma için `baglaclar-ve-gecisler.md` → Dağıtma tuzağı; uzun belgede terim listesi için `uzun-belge.md` → 3.
- **Önce → Sonra:** *Yeni randevu uygulaması ilk ayda 2.000 kez indirildi. Bu platformun en çok kullanılan özelliği hatırlatıcı oldu. Kullanıcılar bu çözümün sade arayüzünü de beğendi.* → *Yeni randevu uygulaması ilk ayda 2.000 kez indirildi. Uygulamanın en çok kullanılan özelliği hatırlatıcı oldu. Kullanıcılar uygulamanın sade arayüzünü de beğendi.*

### YPI-07 · Ekleme geçişi yığılması

- **Belirti:** Cümlelerin art arda "Ayrıca", "Bunun yanı sıra", "Aynı zamanda", "Buna ek olarak" ile açılması; aynı cümlede iki ekleme işareti ("Ayrıca depo da denetlenecek.").
- **Neden yapay görünür:** "Yanı sıra" ChatGPT metinlerinde 45, öğrenci metinlerinde 6 kez geçer; "aynı zamanda" ChatGPT metinlerinde 295 kez geçer [BA26, s. 425, 428]. Geçiş sözü tek başına zayıf bir işarettir [WP-AI].
- **Ne yapılır:** Yalnızca ekleme işlevi gören cümle başı sözleri sil ya da azalt. Karşıtlık, sebep ve sonuç bağlaçlarını ("ancak", "bu yüzden", karşıtlık bildiren "öte yandan") silme. Yerine "de/da" koyacaksan odağın doğru öğede olduğuna bak. Aynı cümlede iki ekleme işareti varsa birini bırak; "ayrıca" "ayrı olarak" anlamındaysa o ekleme işareti değildir, kalır.
- **Dokunma:** Gerekçeleri tek tek sayan dilekçe ve rapor dili; madde madde gerekçe.
- **Anlam riski:** ANL-06 (karşıtlık ya da sebep bağı silinir), ANL-12 ("de" odağı), ANL-18.
- **Ayrıntı:** `baglaclar-ve-gecisler.md` → Yol 1, Yol 4, "ayrıca" maddesi ve Dağıtma tuzağı.
- **Önce → Sonra:** *Yeni ofiste her katta bir dinlenme alanı var. Bunun yanı sıra, otoparkta elektrikli araçlar için şarj noktaları bulunuyor. Ayrıca, bina metro istasyonuna yürüme mesafesinde.* → *Yeni ofiste her katta bir dinlenme alanı var. Otoparkta elektrikli araçlar için şarj noktaları bulunuyor. Bina metro istasyonuna yürüme mesafesinde.*

---

## CEV · Çeviri etkisi

### CEV-01 · Çeviri deyim

- **Belirti:** İngilizce deyimlerin sözcüğü sözcüğüne çevirisi: "günün sonunda" (sonuçta), "masaya getirmek" (beraberinde getirmek, katmak), "fark yaratmak", "oyunun kurallarını değiştirmek", "kutunun dışında düşünmek", "aynı sayfada olmak"; e-postanın başında "Umarım bu e-posta sizi iyi bulur."
- **Neden yapay görünür:** "Günün sonunda", "masaya getirmek" ve "fark yaratmak" Güncel Türkçe Sözlük'te deyim olarak yer almaz. Türkçede yerleşik "masaya yatırmak" ise başka anlamdadır: bir konuyu araştırmak, enine boyuna tartışmak [TDK-GTS]. Bu kalıpların İngilizceden geçtiği gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Türkçedeki yerleşik karşılığı aynı anlam ve güçte kullan. Mecazın ne kastettiği belli değilse sor ("aynı sayfada olmak": aynı fikirde olmak mı, aynı bilgiye sahip olmak mı?). E-postadaki çeviri iyi dilek cümlesini aynı işi gören olağan bir sözle değiştir ("Umarım iyisinizdir.") ya da kullanıcıya sorarak sil; ardından gelen selamlamaya ve hitaba dokunma (ACL-02).
- **Dokunma:** Gerçek anlamda kullanım ("Günün sonunda kasayı sayarız." = akşam); kullanıcının ekip içi yazışmada bilerek kullandığı iş jargonu; alıntı.
- **Anlam riski:** ANL-08 (gerçek zaman bildiren "günün sonunda"), ANL-02, ANL-14.
- **Önce → Sonra:** *Yeni proje yöneticimiz, sağlık sektöründeki on yıllık deneyimini masaya getiriyor. Günün sonunda, hepimiz aynı hedef için çalışıyoruz.* → *Yeni proje yöneticimiz, sağlık sektöründeki on yıllık deneyimini beraberinde getiriyor. Sonuçta hepimiz aynı hedef için çalışıyoruz.*

### CEV-02 · "Sahip olmak" kalıbı

- **Belirti:** Mülkiyet bildirmeyen yerde "sahip olmak": "büyük bir öneme sahiptir", "dört bölüme sahiptir", "yüksek bir potansiyele sahip", "geniş bir bilgi birikimine sahip".
- **Neden yapay görünür:** Sözlükte "sahip olmak"ın tek anlamı mülkiyette olmak, elde bulundurmaktır [TDK-GTS]. Nitelik bildiren kullanımın İngilizcedeki "have" yapısını andırdığı gözleme dayanır [gözlem; kaynak doğrulanamadı]. İncelenen bir ChatGPT-4 denemesi hayatı "birçok renk ve dokuya sahip" bir tabloya benzetir [COS25, s. 388].
- **Ne yapılır:** Türkçenin kendi yapısını kullan: "önemlidir", "dört bölümden oluşur", "potansiyeli yüksek", "bilgi birikimi geniş", "özeti vardır". Dereceyi ve dağılımı koru.
- **Dokunma:** Mülkiyet ve hak bildiren kullanım ("iki patente sahiptir"; hukukta "oy hakkına sahiptir"); ayrı bir deyim olan "sahip çıkmak".
- **Anlam riski:** ANL-02 (derece), ANL-20 ("her bölüm bir özete sahip" dağılımı), ANL-14.
- **Önce → Sonra:** *Rapor dört bölüme sahiptir ve her bölüm ayrıntılı bir özete sahiptir.* → *Rapor dört bölümden oluşur ve her bölümün ayrıntılı bir özeti vardır.*

### CEV-03 · Gereksiz "bir"

- **Belirti:** Belirsizlik ya da sayı bildirmeyen "bir": "hızlı bir şekilde", "büyük bir memnuniyetle", "olumlu bir etki yaratmak", "bir öğretmen olarak".
- **Neden yapay görünür:** "Bir", ChatGPT metinlerinin en sık ikinci sözcüğüdür (%3,271; öğrenci metinlerinde %2,625) [BA26, s. 425]. Fazlalığın İngilizcedeki "a/an" kullanımını andırdığı gözleme dayanır [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** "Bir" belirsizlik ya da sayı bildirmiyorsa sil ya da kalıbı sadeleştir: "hızlı bir şekilde" → "hızla", "büyük bir memnuniyetle" → "büyük memnuniyetle".
- **Dokunma:** Sayı ya da belirsiz bir kişi bildiren "bir" ("Her çalışan bir hekimle görüştü."); "bir" düşünce adın belirli okunduğu yerler ("rapor hazırladı" ile "raporu hazırladı" farklıdır).
- **Anlam riski:** ANL-20 (dağılım), ANL-19 (belirtililik), ANL-03.
- **Önce → Sonra:** *Talebiniz hızlı bir şekilde değerlendirilecek ve size büyük bir memnuniyetle dönüş yapılacaktır.* → *Talebiniz hızla değerlendirilecek ve size büyük memnuniyetle dönüş yapılacaktır.*

### CEV-04 · Gereksiz kişi ve iyelik zamiri

- **Belirti:** Kişi ekinin zaten gösterdiği zamiri yinelemek: "Biz ekip olarak sizin görüşlerinizi önemsiyoruz.", "Ben şahsen düşünüyorum ki …", "bizim ürünümüz".
- **Neden yapay görünür:** Türkçede kişi ve iyelik ekleri özneyi ve iyeyi zaten gösterir; vurgu ya da karşıtlık yokken zamiri yinelemek çeviri sesi verir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Zamir karşıtlık ya da vurgu bildirmiyorsa sil. "Ben şahsen düşünüyorum ki" → "Bence" (görüş işareti kalır).
- **Dokunma:** Karşıtlık ve odak bildiren zamir ("Bu kararı biz değil, kurul verdi."); resmi yazışmada kurumun kendini adlandırması; görüş işaretleri (ANL-22).
- **Anlam riski:** ANL-11 (özne), ANL-12 (odak), ANL-22 (görüşün sahibi).
- **Önce → Sonra:** *Biz ekip olarak sizin geri bildirimlerinizi çok önemsiyoruz.* → *Ekip olarak geri bildirimlerinizi çok önemsiyoruz.*

### CEV-05 · İngilizce anlamıyla kullanılan sözcük

- **Belirti:** Türkçede başka anlamı olan bir sözcüğü İngilizce karşılığının anlamıyla kullanmak: "dramatik bir düşüş", "agresif bir büyüme hedefi", "kritik bir adım", "sorunu adreslemek".
- **Neden yapay görünür:** Sözlükte "dramatik" sahne oyununa özgü, gerilimli, coşku veren ya da acıklı; "agresif" saldırgan; "kritik" endişe verici ya da nazik demektir. "Adreslemek" sözlükte yoktur [TDK-GTS].
- **Ne yapılır:** Kastedilen anlamı aynı derecede karşılayan Türkçe sözü seç: "dramatik bir düşüş" → "keskin bir düşüş", "adreslemek" → "ele almak". "Ele almak" ile "çözmek" farklıdır; kaynak çözüldüğünü söylemiyorsa "çözmek" yazma.
- **Dokunma:** Sözcük Türkçe anlamıyla kullanıldığında ("dramatik bir sahne", "agresif davranış"); tıpta ve mühendislikte terim olan "kritik"; marka ve kampanya adları.
- **Anlam riski:** ANL-02 (büyüklük ve hız), ANL-14 (terim), ANL-16 ("ele almaya başladı" → "çözdü").
- **Önce → Sonra:** *Yeni yazılımla birlikte iade taleplerinde dramatik bir düşüş yaşandı ve ekip kalan şikâyetleri adreslemeye başladı.* → *Yeni yazılımla birlikte iade taleplerinde keskin bir düşüş yaşandı ve ekip kalan şikâyetleri ele almaya başladı.*


### CEV-06 · İngilizceden kelime kelime çevrilmiş isim zinciri

- **Belirti:** İngilizce bir kavram adının sözcük sözcük ad tamlaması zinciriyle Türkçeye dökülmesi. Örnekler: "anlam kayması tuzağı" (*meaning-drift trap*), "iz kataloğu" (*trace catalogue*), "kullanıcı yolculuğu haritası" (*user journey map*), "karar verme süreci yönetimi". Tamlama dil bilgisi açısından doğrudur, ama Türkçe yazan biri aynı şeyi çoğu zaman böyle adlandırmaz.
- **Neden yapay görünür:** İngilizce kavramları ad yığınlarıyla kurar. Türkçe aynı ilişkiyi çoğu zaman bir sıfat-fiil ya da açıklayıcı bir öbekle söyler: "anlamın en sık kaydığı durumlar". Uzun ad zincirleri okurun ilişkiyi kendisinin çözmesini gerektirir (DLB-04 ile akraba) [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Kendiliğinden değiştirme. Tamlamanın yerleşik bir terim mi, yazarın bilinçli seçtiği bir ad mı, yoksa çeviri etkisi mi olduğu metinden her zaman çıkmaz. Yanlış tahmin bir terimi bozar. Bunun yerine öneriler listesine ekle (SKILL.md › Çıktı): ifade → önerilen söyleyiş · tek satırlık gerekçe. Önerilen söyleyiş anlamı korumalı; sayı, kapsam ve iddianın gücü aynı kalır. Kullanıcı onaylarsa uygula ve denetimi yinele.
- **Dokunma:**
  - Türkçede yerleşmiş terimler: "kullanıcı deneyimi", "risk değerlendirmesi", "iş sağlığı ve güvenliği".
  - Alanın kendi terminolojisi.
  - Kurum, ürün ve proje adları.
  - Metinde ilk geçtiği yerde tanımlanmış terimler.
  - Uzman okura yazılmış metinde o alanın bilinen kısaltmalı kavramları.
- **Anlam riski:** ANL-14 (terim): Yerleşik bir terimi açıklamaya çevirmek anlamını genişletebilir ya da daraltabilir. ANL-03 (kapsam): "23 anlam kayması tuzağı" → "anlamın kaydığı bazı durumlar" yazılırsa sayı ve kapsam kaybolur.
- **Önce → Sonra (öneri):** *Rehberde 23 anlam kayması tuzağı yer alıyor.* → *Rehberde anlamın kayabileceği 23 durum yer alıyor.* ("en sık kaydığı" yazmak, kaynakta olmayan bir sıklık iddiası eklerdi.)

---

## NOK · Noktalama ve yazım

### NOK-01 · Uzun çizgi

- **Belirti:** Ara sözü ya da açıklamayı uzun çizgiyle (—), çoğu zaman iki yanı boşluklu olarak ayırmak.
- **Neden yapay görünür:** TDK uzun çizgiyi yalnızca satır başına alınan konuşmalar için tanımlar; ara söz virgül, kısa çizgi ya da ayraçla ayrılır [TDK-NOK]. Modeller uzun çizgiyi insanlardan çok kullanır, ama işaret tek başına zayıftır. 2026 sonbaharından sonra bazı modellerin uzun çizgiden tümüyle kaçındığı, bunun yerine virgüle ve noktaya yüklendiği bildiriliyor [WP-AI].
- **Ne yapılır:** Ara sözü virgülle ayır; virgül cümleyi karıştırıyorsa ayraç kullan. Tek çizgiyi yalnızca gerçekten bir açıklama getiriyorsa iki noktaya çevir.
- **Dokunma:** Roman ve öyküde konuşma çizgisi; tasarım ve başlık düzeni; kullanıcının kendi metninde bütün belge boyunca tutarlı kullandığı ara söz çizgisi (bir yayın tercihi olabilir; emin değilsen sor); çeviri alıntı.
- **Anlam riski:** ANL-12 (ara sözün bağlı olduğu öğe), ANL-17 (ara söz bir koşul ya da istisna taşıyorsa), ANL-06 (iki noktaya çevirince sebep ya da açıklama okuması).
- **Ayrıntı:** `yazim-noktalama.md` → YZ-01 (bütün dönüşümler ve bir kayma örneği), YN-17, YN-37, YN-39.
- **Önce → Sonra:** *Yeni okuma salonu — hafta sonları dahil — gece yarısına kadar açık.* → *Yeni okuma salonu, hafta sonları dahil, gece yarısına kadar açık.*

### NOK-02 · Başlık büyük harfi

- **Belirti:** Ara başlıklarda ve madde etiketlerinde "ve, ile, da" gibi bağlaçların da büyük harfle başlaması; cümle içinde özel ad olmayan sözlerin büyük harfle yazılması ("Müşteri Deneyimi öne çıkıyor"); aynı belgede başlık düzenlerinin karışması.
- **Neden yapay görünür:** Başlıkta her sözcüğü büyük yazmak yapay zekâ metninde sık görülür [WP-AI]. Türkçede bu tek başına iz değildir: Kitap, bildiri ve makalede alt başlıktaki sözcüklerin ilk harfleri büyük yazılır [TDK-BH, E]. Her sözcüğü büyük yazılan eser ve kurum adlarında ise "ve, ile, ya, veya, ki, da, de" ve soru eki küçük kalır [TDK-BH, md. 21 uyarı]. İz olan; büyütülmüş bağlaç, cümle içine taşınan büyük harf ve tutarsızlıktır.
- **Ne yapılır:** Belgenin kendi başlık düzenini bul ve koru. Yalnızca büyütülmüş bağlacı ve soru ekini küçült, tutarsız başlıkları belgenin kendi düzenine getir, cümle içindeki gereksiz büyük harfi küçült. E-posta ve blog başlıkları için TDK'de kural yoktur; kullanıcı istemedikçe başlık düzenini değiştirme.
- **Dokunma:** Tez, kitap ve makalede kurum kılavuzuna ya da TDK kuralına göre yazılmış başlıklar; özel adlar, kurum ve eser adları (her sözcük büyük harfle başlar); cümle içinde belirli bir kurulu, birimi, programı ya da belgeyi adlandıran büyük harf.
- **Anlam riski:** ANL-14 (özel ad küçültülünce ad olmaktan çıkar), ANL-15 (belirli bir gönderge genele döner).
- **Ayrıntı:** `yazim-noktalama.md` → YZ-03, YN-65, YN-67, YA-08.
- **Önce → Sonra:**

  Önce:

  ```text
  ## Gece Vardiyasında Uyku Ve Beslenme

  Gece çalışanlar için kısa öneriler.
  ```

  Sonra:

  ```text
  ## Gece Vardiyasında Uyku ve Beslenme

  Gece çalışanlar için kısa öneriler.
  ```

### NOK-03 · Ünlem bolluğu

- **Belirti:** Bilgi cümlelerinin ünlemle bitmesi; bir paragrafta birden çok ünlem; art arda ünlem ("!!").
- **Neden yapay görünür:** TDK ünlemi duygu, seslenme ve uyarı sözleri ile ayraç içindeki alay için tanımlar [TDK-NOK]. Düz bilgi cümlesindeki ünlem bu işlevlerin dışında kalır. Model metinlerindeki sıklığı ölçülmemiştir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Bilgi cümlesindeki ünlemi noktaya çevir, art arda ünlemi teke indir. Uyarı, hatırlatma, seslenme ve gerçek duygu ünlemini koru.
- **Dokunma:** Güvenlik uyarısı ("Dikkat! Zemin ıslak."); reklam, davet, kutlama, sosyal medya ve çocuklara yönelik metin; yazarın coşkusu; ayraç içindeki alay ünlemi "(!)".
- **Anlam riski:** ANL-07 (uyarının gücü), ANL-21 (alay ünlemi silinirse ironi kaybolur).
- **Ayrıntı:** `yazim-noktalama.md` → YZ-08, YN-33, YN-34, YA-05.
- **Önce → Sonra:** *Kayıtlar pazartesi başlıyor! Kontenjan 40 kişiyle sınırlı! Formu doldurmayı unutmayın!* → *Kayıtlar pazartesi başlıyor. Kontenjan 40 kişiyle sınırlı. Formu doldurmayı unutmayın!*

### NOK-04 · İki noktalı ilan

- **Belirti:** Bir sonucu ya da "sırrı" iki noktayla sahneye çıkarmak: "Gerçek şu:", "Sonuç:", "İşin sırrı basit:", "Anketten çıkan sonuç şu:".
- **Neden yapay görünür:** TDK'ye göre iki nokta, örnek ya da açıklama verilecek cümlenin sonuna konur [TDK-NOK]; yani kullanım doğrudur. İz olan, bilgiyi her seferinde bir açılışla sahnelemektir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** İlan kalıbını kaldır, bilgiyi doğrudan söyle. Bilginin kaynağını ("ankete göre") koru. İki nokta gerçek bir örnek ya da açıklama getiriyorsa bırak.
- **Dokunma:** Liste ve örnek tanıtımı; tutanak ve form alanları ("Sonuç: Onaylandı" bir alan adıdır); sözlük ve tanım düzeni.
- **Anlam riski:** ANL-15 (kaynak), ANL-09 (aktarım), ANL-06.
- **Ayrıntı:** İki noktadan sonra büyük ya da küçük harf için `yazim-noktalama.md` → YN-26, YZ-07.
- **Önce → Sonra:** *Anketten çıkan sonuç şu: Katılımcıların çoğu karma çalışma modelini tercih ediyor.* → *Ankete göre katılımcıların çoğu karma çalışma modelini tercih ediyor.*

---

## BIC · Biçim ve yerleşim

### BIC-01 · Madde işaretine düşkünlük

- **Belirti:** Akıcı anlatım gerektiren yerde (e-posta, mektup, kısa açıklama) bilginin maddelere bölünmesi; maddelerin kalın bir etiket ve iki noktayla açılması ("**Ulaşım:** …").
- **Neden yapay görünür:** Bilgiyi kalın etiketli dikey listelerle sunmak, yapay zekâ metninin bilinen bir biçim izidir [WP-AI].
- **Ne yapılır:** Maddeleri düzyazıya çevir. Sırayı, sayıyı ve her maddenin kapsamını koru. Etiket bir bilgi taşıyorsa ("Dönüş:") cümleye aktar. Maddeler arasında kaynakta olmayan bir sebep ya da sıra bağı kurma.
- **Dokunma:** Prosedür, kontrol listesi, malzeme listesi, mevzuat bentleri, toplantı gündemi; kullanıcının istediği biçim.
- **Anlam riski:** ANL-06 (bağ eklemek), ANL-18 (maddeler "ve" ile mi "veya" ile mi bağlı?), ANL-17 (bir maddedeki koşulun ötekilere yayılması), ANL-08 (sıra).
- **Önce → Sonra:**

  Önce:

  ```text
  Merhaba Selin Hanım,

  Cuma günkü ziyaret için plan şöyle:

  - **Ulaşım:** Servis saat 9.00'da kapıda olacak.
  - **Öğle yemeği:** Tesisin yemekhanesinde verilecek.
  - **Dönüş:** Servis saat 16.00'da ayrılacak.
  ```

  Sonra:

  ```text
  Merhaba Selin Hanım,

  Cuma günkü ziyarette servis saat 9.00'da kapıda olacak. Öğle yemeği tesisin yemekhanesinde verilecek. Dönüş servisi saat 16.00'da ayrılacak.
  ```

### BIC-02 · Kalın yazı bolluğu

- **Belirti:** Düzyazıda bir paragrafta birden çok kalın söz öbeği; "**Önemli:**" gibi kalın uyarı etiketleri.
- **Neden yapay görünür:** Sohbet modelleri düzyazıda kalın yazıyı aşırı kullanır [WP-AI].
- **Ne yapılır:** Süs kalınları kaldır. Uyarı sözcüğünü ("Önemli:") ve gerçek bir son tarihi ya da yasağı koru; gerekirse yalnızca onu kalın bırak.
- **Dokunma:** Kullanım kılavuzu, sık sorulan sorular, sözlük, form; bir terimin ilk tanımı; kurumun yazım kılavuzundaki vurgu kuralı.
- **Anlam riski:** ANL-07 (uyarının gücü), ANL-15 ("**Yalnızca üyeler için**" gibi kapsam bilgisi), ANL-17.
- **Önce → Sonra:**

  Önce:

  ```text
  Ekibimiz **her pazartesi** toplanır ve **haftalık hedefleri** belirler. **Önemli:** Toplantıya katılamayacak olanlar **en geç pazar akşamı** bilgi vermelidir.
  ```

  Sonra:

  ```text
  Ekibimiz her pazartesi toplanır ve haftalık hedefleri belirler. Önemli: Toplantıya katılamayacak olanlar en geç pazar akşamı bilgi vermelidir.
  ```

### BIC-03 · Emoji

- **Belirti:** Başlık ve madde başlarında süs emojisi (🚀, ✅, 💡, 📌); resmi ya da bilgi veren metinde emoji.
- **Neden yapay görünür:** Yapay zekâ metninde emojiler çoğu zaman bölüm başlıklarının ve madde başlarının önüne konur [WP-AI].
- **Ne yapılır:** Süs emojisini sil. Emoji bir anlam taşıyorsa (✅ tamamlandı, ❌ yok ya da yapılmadı) bunu sözle yaz. Metinde zaten yazıyorsa yalnızca emojiyi sil.
- **Dokunma:** Sosyal medya; kullanıcının kendi mesajlaşma üslubu; durumu emojiyle gösteren tablolar.
- **Anlam riski:** ANL-04 (❌ bir olumsuzluk taşır), ANL-16 (✅ tamamlanma bilgisi), ANL-21 (ironik emoji).
- **Önce → Sonra:**

  Önce:

  ```text
  🚀 Yeni sürüm yayında!

  - ✅ Karanlık tema eklendi
  - ❌ Çevrim dışı mod bu sürümde yok
  ```

  Sonra:

  ```text
  Yeni sürüm yayında.

  - Karanlık tema eklendi
  - Çevrim dışı mod bu sürümde yok
  ```

### BIC-04 · Gereksiz başlık

- **Belirti:** Birkaç paragraflık bir metne başlık hiyerarşisi kurmak ("## Giriş", "## Sonuç"); e-postaya ara başlık eklemek; birden çok birinci düzey başlık.
- **Neden yapay görünür:** Modeller yanlış başlık düzeyleri kullanır; eski modeller kısa metinlere bile "Sonuç" bölümü ekler [WP-AI].
- **Ne yapılır:** Kısa metinde başlıkları kaldır, geçişi konu cümlesiyle yap. Başlığın taşıdığı kapsam bilgisini ("Yalnızca merkez şube") metne aktar.
- **Dokunma:** Rapor, tez, kılavuz, web sayfası; kullanıcının şablonu; başlıklar arası gönderme yapılan belgeler.
- **Anlam riski:** ANL-15 (başlıktaki kapsam ya da tanım bilgisi), ANL-03.
- **Önce → Sonra:**

  Önce:

  ```text
  ## Giriş

  Bu not, kasım ayı stok sayımının sonucunu özetler.

  ## Sonuç

  Sayımda 3 kalemde eksik bulundu.
  ```

  Sonra:

  ```text
  Bu not, kasım ayı stok sayımının sonucunu özetler. Sayımda 3 kalemde eksik bulundu.
  ```

### BIC-05 · Sohbet ve şablon kalıntısı

- **Belirti:** "İşte istediğiniz metin:"; doldurulmamış yer tutucular ("[Kurum Adı]", "[Tarih]", "XX"); "Bir yapay zekâ olarak …", "Son bilgi güncellememe göre …"; "Bu bölümü kendi bilgilerinizle güncelleyin." Sohbet ekranından kopyalanan metinde kalan görünmez karakterler (sıfır genişlikli boşluk, yumuşak tire) ve "【4†source】", "turn0search0" gibi kaynak işaretleri.
- **Neden yapay görünür:** Kullanıcıya yönelik sohbet sözleri, doldurulmamış şablon kalıpları, "bir yapay zekâ dil modeli olarak" girişleri ve bilgi kesim tarihi uyarıları yapay zekâ çıktısının açık izleridir [WP-AI]. Görünmez karakterler ve kaynak işaretleri kopyalama artığıdır; okur görmez ama sayıyı ya da sözcüğü bölebilir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Sohbet ve kimlik cümlelerini sil. Görünmez karakterleri ve kaynak işaretlerini sil; denetim aracı bunları bildirir. Yer tutucuyu kendin doldurma: görünür bırak ve kullanıcıya hangi bilginin eksik olduğunu söyle.
- **Dokunma:** Kullanıcının bilerek hazırladığı şablon ya da form; yapay zekâ üzerine yazılmış bir metin; "Son güncelleme: 3 Mart" gibi gerçek bir sürüm notu.
- **Anlam riski:** ANL-11 (yer tutucuya ad uydurmak özne eklemektir), ANL-15 ("2024 verilerine göre" gerçek bir sınırdır), ANL-08.
- **Önce → Sonra:**

  Önce:

  ```text
  İşte istediğiniz duyuru metni:

  Değerli [Kurum Adı] çalışanları, yıllık sağlık taramamız 12 Mayıs'ta yapılacaktır.
  ```

  Sonra:

  ```text
  Değerli [Kurum Adı] çalışanları, yıllık sağlık taramamız 12 Mayıs'ta yapılacaktır.
  ```

### BIC-06 · Görüntülenmeyen Markdown işareti

- **Belirti:** Markdown'ı göstermeyen bir ortama (e-posta, kelime işlemci, form, SMS, düz metin) yapıştırılmış metinde çıplak işaretler: `**Önemli:**`, `## Başlık`, `---` ayracı, satır içi kod için ters tırnak, madde başında `* `.
- **Neden yapay görünür:** Sohbet modelleri Markdown üretir. Markdown'ı işlemeyen bir ortamda yıldızlar, diyez işaretleri, "---" ayraçları ve kod blokları olduğu gibi görünür [WP-AI].
- **Ne yapılır:** Metnin gideceği ortam belliyse ve orada Markdown görüntülenmiyorsa işaretleri kaldır. İşaretin taşıdığı bilgiyi sözle koru: Başlığın metnini, "Önemli:" gibi uyarı sözünü, madde sırasını ve sayısını bırak. Hedef ortam belli değilse dokunma ve kullanıcıya sor.
- **Dokunma:** Markdown'ı gösteren ortamlar (README, wiki, not uygulaması, bu skill'in kendi dosyaları); kod blokları ve satır içi kod (içerik koddur; betik bunları birebir denetler); kullanıcının bilerek kullandığı işaretler.
- **Anlam riski:** ANL-07 (uyarı sözü düşerse uyarının gücü), ANL-15 (başlıktaki kapsam bilgisi), ANL-18 (madde sırası ve bağlantısı).
- **Ayrıntı:** Kalın yazı ve başlık sayısı için BIC-02 ve BIC-04.
- **Önce → Sonra:**

  Önce (düz metin e-postaya yapıştırılmış):

  ```text
  ## Tatbikat duyurusu

  **Önemli:** Yarınki yangın tatbikatı saat 10.00'da başlayacak. Toplanma alanı B otoparkı.
  ```

  Sonra:

  ```text
  Tatbikat duyurusu

  Önemli: Yarınki yangın tatbikatı saat 10.00'da başlayacak. Toplanma alanı B otoparkı.
  ```

---

## TON · Ton ve ses

### TON-01 · Yapay samimiyet

- **Belirti:** Okurla zorlama yakınlık: "Merak etmeyin!", "Hadi gelin, birlikte keşfedelim!", "Siz de benim gibi …", "Sevgili okur", "Hepimiz bu duyguyu biliriz, değil mi?".
- **Neden yapay görünür:** Sohbet modelleri kullanıcıya yönelik konuşma dilini metne taşır [WP-AI]. İncelenen bir ChatGPT-4 denemesinde "biz" 289 sözcükte 6 kez geçer [COS25, s. 381]. Okura yakınlık kalıplarının Türkçedeki sıklığı ölçülmemiştir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Güvence ve davet kalıplarını ("Merak etmeyin", "hadi gelin") sil ya da sadeleştir. Bir bilgi, öneri ya da yazarın kendisi hakkında bir beyan varsa koru. Kapsayıcı "hepimiz" bir kapsam iddiasıysa daraltma ya da genişletme.
- **Dokunma:** Kişisel blog, köşe yazısı, konuşma metni, çocuklara yönelik metin, topluluk bülteni; yazarın kendi samimi sesi.
- **Anlam riski:** ANL-03 ("hepimiz"), ANL-11 (özne), ANL-18 ("değil mi?" sorusu), ANL-21.
- **Önce → Sonra:** *Kombinin filtresini değiştirmek sanıldığı kadar zor değil. Merak etmeyin, hadi gelin adım adım birlikte bakalım!* → *Kombinin filtresini değiştirmek sanıldığı kadar zor değil. Adım adım birlikte bakalım.*

### TON-02 · Aşırı genelleme

- **Belirti:** Dayanaksız evrensel çerçeveler: "Herkesin bildiği gibi", "Hepimiz biliyoruz ki", "toplumun her kesimi", "her zaman", "asla".
- **Neden yapay görünür:** Yapay zekâ metni bir ya da iki kaynağa dayanan görüşleri yaygın bir kabul gibi sunar [WP-AI].
- **Ne yapılır:** Bilgi taşımayan genelleme çerçevesini ("Herkesin bildiği gibi") sil; önermeyi ve temkinini koru. Niceleyici bir iddianın parçasıysa ("her zaman", "tüm") kendiliğinden daraltma; yazara sor.
- **Dokunma:** Kaynakta gerçekten evrensel bir iddia ("Tüm çalışanlar eğitime katılır." bir mevzuat hükmüdür); atasözü, deneme, hitabet.
- **Anlam riski:** ANL-03 (niceleyici), ANL-20 (dağılım), ANL-22 (yaygın kabul ile yazarın görüşü).
- **Önce → Sonra:** *Herkesin bildiği gibi, düzenli bakım yapılmayan kombiler daha çok yakıt tüketebilir.* → *Düzenli bakım yapılmayan kombiler daha çok yakıt tüketebilir.*

### TON-03 · Belirsiz atıf

- **Belirti:** Adı verilmeyen otoritelere dayanmak: "Uzmanlar … belirtiyor", "Yapılan pek çok araştırma göstermektedir ki", "Birçok kaynağa göre".
- **Neden yapay görünür:** Yapay zekâ metni iddiaları adı verilmeyen "uzmanlara" ya da "eleştirmenlere" bağlar [WP-AI].
- **Ne yapılır:** Kalıbı sadeleştir ama atfı ve niceleyiciyi ("pek çok") koru. Kaynak metinde ya da kullanıcıda varsa adlandır. Kaynak uydurma. Atfı silme: Silinirse iddia yazarın kendi iddiasına döner. Kullanıcıya kaynağın eksik olduğunu bildir.
- **Dokunma:** Haberde kaynağı gizli tutulan aktarım; aktarımın kendisi bir bilgidir.
- **Anlam riski:** ANL-15 (kaynak), ANL-22 (görüşün sahibi), ANL-03 ("pek çok"), ANL-09 (aktarım).
- **Önce → Sonra:** *Yapılan pek çok araştırma göstermektedir ki, öğle uykusu dikkat süresini artırabilir.* → *Pek çok araştırmaya göre öğle uykusu dikkat süresini artırabilir.*

### TON-04 · Sorumluluk reddi ve öğretici uyarı

- **Belirti:** Uzun, kendini yineleyen uyarılar: "Lütfen unutmayın ki bu bilgiler yalnızca genel bilgilendirme amaçlıdır …", "Her bireyin durumu farklıdır.", "Mutlaka bir uzmana danışın."
- **Neden yapay görünür:** 2023–2024 modelleri öğretici uyarılar ekler; 2024–2025 modelleri ise bir bilginin "kamuya açık olmadığını" söyleyen kaçamak cümleler kurar [WP-AI].
- **Ne yapılır:** Uyarıyı kısalt ama içeriğini koru: kapsamı ("yalnızca"), olumsuzluğu ("yerine geçmez"), öneri kipini ("danışmanız önerilir") ve gücünü ("mutlaka"). Uyarıyı tümden silmek bir bilgiyi silmektir; kullanıcıya sor.
- **Dokunma:** Tıbbi, hukuki ve mali metinde uyarı çoğu zaman bir yükümlülük ya da sorumluluk bilgisidir; ilaç prospektüsü, sözleşme, yatırım metni.
- **Anlam riski:** ANL-07 (öneri ile emir), ANL-03 ("yalnızca"), ANL-04 (olumsuzluk), ANL-02 ("mutlaka").
- **Önce → Sonra:** *Lütfen unutmayın ki bu yazıda yer alan bilgiler yalnızca genel bilgilendirme amaçlıdır ve hiçbir şekilde profesyonel tıbbi tavsiye yerine geçmez; herhangi bir sağlık sorununuz varsa mutlaka bir hekime danışmanız önerilir.* → *Bu yazıdaki bilgiler yalnızca genel bilgilendirme amaçlıdır ve hiçbir şekilde profesyonel tıbbi tavsiye yerine geçmez. Bir sağlık sorununuz varsa mutlaka hekime danışmanız önerilir.*

### TON-05 · Temkin yığılması

- **Belirti:** Aynı önermede aynı işi gören birden çok temkin: "belki de … olabilir", "muhtemelen … olabileceği düşünülebilir".
- **Neden yapay görünür:** Temkin tek başına iz değildir: İngilizce denemelerde ChatGPT öğrencilerden daha az epistemik işaret kullanır [HER23]. İz olan, aynı işi gören temkinlerin üst üste binmesidir [gözlem; kaynak doğrulanamadı].
- **Ne yapılır:** Aynı işi gören iki temkinden birini sil. Biri ötekinden güçlüyse ve hangisinin kastedildiği belli değilse ("muhtemelen … olabilir") dokunma ya da yazara sor. Temkinler farklı işler görüyorsa (olasılık, yaklaşıklık, kanıta dayalı çıkarım) hiçbirini silme.
- **Dokunma:** Akademik ve tıbbi metinde "düşündürmektedir" ile "olabilir" farklı işler görür; hukukta "kanaatimizce" bir görüş işaretidir.
- **Anlam riski:** ANL-01 (temkin), ANL-02 (derece), ANL-22 (görüş işareti).
- **Önce → Sonra:** *Gecikmenin nedeni belki de sunucu bakımı olabilir.* → *Gecikmenin nedeni sunucu bakımı olabilir.*

### TON-06 · Zorunlu iyimserlik

- **Belirti:** Olumsuz bir olgunun ardından gelen hazır iyimser özdeyiş ya da olumsuzu fırsata çeviren kalıp: "Her zorluk aslında yeni bir fırsattır!", "Bu süreç bir büyüme fırsatına dönüştü."
- **Neden yapay görünür:** İnsan haber metinleri korku ve iğrenme gibi olumsuz duyguları model metinlerinden daha güçlü dile getirir [MUN24]. İncelenen bir ChatGPT-4 denemesi, korkutucu bulunan değişimi bir büyüme göstergesine bağlar [COS25, s. 388].
- **Ne yapılır:** Olayla ilgisi olmayan genel bir özdeyişi sil ve kısa notta sildiğini bildir. Olayla ilgili somut bilgiyi, olumlu ya da olumsuz, aynı güçte koru. Kaynakta olmayan iyimser bir yorum ekleme, olumsuz olguyu yumuşatma.
- **Dokunma:** Motivasyon konuşması, kurum içi moral yazısı, kişisel gelişim metni; yazarın bilinçli tutumu.
- **Anlam riski:** ANL-02 (olumsuzun gücü), ANL-04, ANL-06 ("yine de" karşıtlığı), ANL-16.
- **Ayrıntı:** "yine de" ve öteki kabul bağlaçları için `baglaclar-ve-gecisler.md` → Beklenti çelişkisi ve kabul.
- **Önce → Sonra:** *Fuar katılımı beklenenden düşük kaldı; yine de standımıza gelen ziyaretçilerle verimli görüşmeler yaptık. Her zorluk, aslında yeni bir fırsattır!* → *Fuar katılımı beklenenden düşük kaldı; yine de standımıza gelen ziyaretçilerle verimli görüşmeler yaptık.*

---

## Yeni kalıp eklerken

- Mevcut kimlikleri yeniden numaralandırma. Yeni kalıp kendi kümesinin sonuna, sıradaki numarayla girer (ör. BIC-06). Silinen bir kalıbın numarası boş kalır, başka kalıba verilmez.
- Aynı blok düzenini kullan: Belirti, Neden yapay görünür, Ne yapılır, Dokunma, Anlam riski, gerekiyorsa Ayrıntı, Önce → Sonra. **Dokunma** satırı zorunludur: Kalıbın olağan dil olduğu en az bir register ya da durumu yaz.
- "Neden yapay görünür" satırını okunan bir kaynağa dayandır ya da `[gözlem; kaynak doğrulanamadı]` diye işaretle. Sayı ve sayfa yalnızca okunan tam metinden yazılır.
- Önce → Sonra çiftini yeni ve kurgusal bir cümleyle yaz, `scripts/anlam_denetimi.py` ile sına. Betik KESİN vermemeli; her KONTROL satırına ve hedefli soruya hüküm ver. "Sonra" kaynaktaki her bilgiyi aynı güçte taşımalı.
- Kural başka bir başvuru dosyasında ayrıntılı anlatılıyorsa burada kısa tut ve **Ayrıntı** satırıyla oraya gönder.

## Kaynaklar

Erişim tarihi hepsi için 5 Kasım 2026'dır. Sayfa numaraları yalnızca okunan tam metinlerden verilmiştir.

- **[TDK-NOK]** Türk Dil Kurumu. *Yazım Kılavuzu: Noktalama İşaretleri* (uzun çizgi, kısa çizgi, virgül, ünlem, iki nokta, tırnak). https://yazim.tdk.gov.tr/content/09-noktalama-isaretleri.html ve https://tdk.gov.tr/icerik/yazim-kurallari/noktalama-isaretleri-aciklamalar/
- **[TDK-BH]** Türk Dil Kurumu. *Büyük Harflerin Kullanıldığı Yerler* (md. 21 ve uyarısı; E; iki noktadan sonra büyük harf). https://tdk.gov.tr/icerik/yazim-kurallari/buyuk-harflerin-kullanildigi-yerler/
- **[TDK-GTS]** Türk Dil Kurumu. *Güncel Türkçe Sözlük.* Sorgulanan maddeler: bağlam, söz konusu, rol, rol oynamak, kritik, hayati, son derece, sahip olmak, tarafından, gerçekleştirmek, katkıda bulunmak, zemin hazırlamak, yolculuk, ekosistem, dönüşüm, sinerji, dramatik, agresif, masaya yatırmak; sözlükte bulunamayanlar: günün sonunda, masaya getirmek, fark yaratmak, adreslemek. https://sozluk.gov.tr
- **[AKS11]** Akaslan, Talat (2011). "–mAktA (ve –Iyor)." *Turkish Studies* 6/4, 331–352. https://arastirmax.com/tr/system/files/dergiler/79199/makaleler/6/4/arastirmax-makta-iyor.pdf (Ergin 1977: 291–292 ve Göksel & Kerslake 2005: 83, 332 bu makalenin aktarımıyla kullanıldı.)
- **[BA26]** Bergin, Burak ve Atasoy, Arzu (2026). "Söz varlığı unsurları bağlamında yapay zekâ ve öğrenci metinleri üzerine bir inceleme." *Uluslararası Türkçe Öğretimi Araştırmaları Dergisi* 6(2), 415–438. https://dergipark.org.tr/tr/download/article-file/5339956 (DOI: https://zenodo.org/doi/10.5281/zenodo.21986509). Veri: ChatGPT-4o mini'nin ve Türkçe öğretmeni adaylarının aynı on konuda yazdığı 147'şer metin.
- **[COS25]** Coşar, Asiye Mevhibe (2025). "Söz dizimi açısından ChatGPT'nin Türkçesine bir bakış." *Uludağ Üniversitesi Fen-Edebiyat Fakültesi Sosyal Bilimler Dergisi* 26(48), 377–389. https://doi.org/10.21550/sosbilder.1568554 · tam metin: https://dergipark.org.tr/tr/download/article-file/4293409
- **[AKB26]** Akboğa, Vural (2026). "Gereksiz sözcük kullanımından doğduğu düşünülen anlatım bozukluklarına anlambilimsel bir bakış." *Akademik Dil ve Edebiyat Dergisi* 10(1), 265–285. https://dergipark.org.tr/tr/pub/akaded/article/1875762 (yalnızca özet okundu).
- **[KOB25]** Kobak, Dmitry; González-Márquez, Rita; Horvát, Emőke-Ágnes; Lause, Jan (2025). "Delving into LLM-assisted writing in biomedical publications through excess vocabulary." *Science Advances* 11(27). Ön baskı: https://arxiv.org/abs/2406.07016 (üslup sözcükleri bulgusu: https://arxiv.org/html/2406.07016v2).
- **[REI25]** Reinhart, Alex ve ark. (2025). "Do LLMs write like humans? Variation in grammatical and rhetorical styles." *PNAS* 122(8). Ön baskı: https://arxiv.org/html/2410.16107v2
- **[HER23]** Herbold, Steffen; Hautli-Janisz, Annette; Heuer, Ute; Kikteva, Zlata; Trautsch, Alexander (2023). "A large-scale comparison of human-written versus ChatGPT-generated essays." *Scientific Reports* 13. https://arxiv.org/abs/2304.14276 (yalnızca özet okundu).
- **[MUN24]** Muñoz-Ortiz, Alberto; Gómez-Rodríguez, Carlos; Vilares, David (2024). "Contrasting linguistic patterns in human and LLM-generated news text." *Artificial Intelligence Review* 57, 265. https://arxiv.org/abs/2308.09067 (yalnızca özet okundu).
- **[WP-AI]** Wikipedia (WikiProject AI Cleanup). "Wikipedia:Signs of AI writing." https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing. Topluluk tarafından güncellenen, gözleme dayalı bir rehberdir; kendisi de işaretlerin kanıt olmadığını vurgular. BIC-06 için "Markup irregularities" bölümü okundu.
