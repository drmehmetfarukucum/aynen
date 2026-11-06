# Bağlaçlar ve geçiş sözleri

Bu dosya, Türkçe bağlaçların ve cümleler arasındaki geçiş sözlerinin hangi ilişkiyi kurduğunu gösterir. Bir eşanlamlılar listesi değildir: Aynı grupta duran iki söz bile çoğu zaman farklı bir ilişki kurar. Amaç, doğallaştırırken bir bağlacı silmenin, bölmenin ya da değiştirmenin ilişkiyi bozup bozmadığına karar vermektir.

## Nasıl okunur

- **İşlev:** Bağlacın iki parça arasında kurduğu ilişki. Bir bağlacın birden çok işlevi olabilir. Hangisinin geçerli olduğunu bağlam belirler.
- **Register:** R resmî (yazışma, mevzuat, tutanak) · G gündelik · A akademik · N nötr (her registerda olağan) · ESK eskimiş ya da edebî.
  Register etiketi kaynak göstermiyorsa bu dosyanın değerlendirmesidir. Kaynağa dayananların yanında kaynak etiketi vardır.
  ESK etiketli sözleri metne sen ekleme. Kaynakta varsa yazarın sesidir, koru (ANL-21). Bir bağlacı sadeleştirirken metnin registerından çıkma: Gündelik bir mesajda R ya da ESK etiketli bir söz yerine aynı işlevli N ya da G sözü seçilir, tersi yapılmaz [değerlendirme].
- **Yerine geçmez:** Bağlacın en sık karıştırıldığı söz ve nedeni.
- **Etiketler:** [TDK-GTS] Güncel Türkçe Sözlük'teki madde anlamlarının kısa özetidir. [değerlendirme] kaynağa değil bu dosyanın yorumuna dayanır. Öteki etiketler dosyanın sonunda açılır.
- ANL kodları `references/anlam-kaymasi.md` dosyasına gönderir.

## Önce: bağlaç gerekli mi?

Yapay zekâ metinlerindeki bağlaç sorunu çoğu zaman sayıyla ilgili değildir. Kanıtlar karışıktır:

- İngilizce öğrenci denemelerini karşılaştıran geniş bir çalışmada ChatGPT metinlerinde söylem belirleyicileri insan metinlerinden **daha az** çıktı [Herbold 2023].
- Biyomedikal özetlerde "additionally", "notably" gibi bazı sözlerin sıklığı dil modelleri yaygınlaştıktan sonra beklenenin çok üstüne çıktı [Kobak 2025].
- Türkçe bir incelemede ChatGPT-3'ün bir metninde aynı kalıp art arda kurulmuştu: genel bir yargı, ardından "Ancak" ile başlayan bir cümle. Bu yapı tekrarı metni tekdüzeleştiriyordu [Coşar 2025, s. 382-383].
- Aynı on konuda yazılmış 147 ChatGPT-4o mini metniyle 147 öğrenci metnini karşılaştıran bir çalışmada "ve" iki grupta da en sık sözcüktü; ama ChatGPT metinlerinde %5,809, öğrenci metinlerinde %3,801 oranında geçti. "Aynı zamanda" ChatGPT metinlerinde en sık 14. sözcüktü, öğrencilerin ilk 50 sözcüğü arasında yoktu [Bergin ve Atasoy 2026, s. 425]. Çalışma "ve"nin hangi işlevle kullanıldığını ayırmaz; öteki bağlaçların sıklığını Türkçede insan metniyle karşılaştıran bir çalışma bulunamadı [kaynak doğrulanamadı].

Bu yüzden iki soru sor: Bağlaç bir ilişki taşıyor mu? Aynı söz ya da aynı kalıp art arda mı geliyor? Bir paragraftaki bağlaç sayısı için eşik yoktur: Sayı tek başına iz değildir [değerlendirme].

**Temel kural**
- Yalnızca ekleme işlevi gören cümle başı sözler silinebilir: *Ayrıca, Bunun yanı sıra, Buna ek olarak.*
- Karşıtlık, kabul, sebep, sonuç, çıkarım, doğrulama ve koşul bağlaçları silinmez. Silinirse kaynaktaki ilişki kaybolur (ANL-06, ANL-17).
- Bağlaç eklemek, kaynakta olmayan bir ilişki eklemektir (ANL-06). Bkz. Anlam tuzakları.

Aşağıdaki beş yol bağlaç yükünü azaltır. Her birinin bir anlam riski var.

### Yol 1: Silme

- **Ne zaman:** Cümle başındaki söz yalnızca "bir madde daha" diyorsa.
- **Önce:** *Yeni vardiya çizelgesi pazartesi yürürlüğe girecek. Bunun yanı sıra dinlenme odasına iki koltuk eklenecek.*
- **Sonra:** *Yeni vardiya çizelgesi pazartesi yürürlüğe girecek. Dinlenme odasına iki koltuk eklenecek.*
- **"eğer" bir yanlış ya da dolgu değildir.** TDK'ye göre şart anlamını güçlendiren bir sözdür [TDK-GTS]. Koşulu -sA eki taşıdığı için "eğer" silinince koşul kaybolmaz, ama pekiştirme düşer. Bu yüzden "eğer"i silmek bir kural değil, üslup kararıdır: Yalnızca aynı paragrafta art arda yığılmışsa azalt [değerlendirme]. Hukuk, sözleşme, talimat ve uzun koşul cümlesinde bırak.
- **Anlam riski**
  - "ayrıca" her zaman ekleme değildir. "Ayrı olarak" ve "ayrı bir önem verilerek" anlamları da vardır [TDK-GTS]. *Bu şikâyet ayrıca incelenecek* cümlesinde "ayrıca" silinirse "ayrı bir işlemle" bilgisi kaybolur.
  - "Bununla birlikte" ekleme, kabul ya da karşıtlık bildirebilir [TDK-GTS]. Hangisi olduğunu bulmadan silme.
  - "Öte yandan" hem başka bir yön hem karşılık bildirebilir [TDK-GTS]. Yalnızca ekleme olduğu açıksa sil.
  - Koşul yan cümlesi uzunsa "eğer" okura koşulun geldiğini baştan haber verir [değerlendirme].
  - Paragraf sonundaki "Sonuç olarak" yalnızca kapanışı duyuruyorsa silinebilir (bkz. `examples/06-tibbi-ozet.md`). Bir bulgudan çıkan sonucu açıyorsa "bu nedenle" işlevindedir, silinmez.

### Yol 2: Noktayla bölme

- **Ne yapar:** Uzun bir cümleyi ikiye böler. Bağlaç kalır, ikinci cümlenin başına geçer.
- **Önce:** *Yeni tartı cihazı ölçümü daha hızlı yapıyor, ancak her sabah sıfır ayarı gerektiriyor ve bu ayar en az beş dakika sürüyor.*
- **Sonra:** *Yeni tartı cihazı ölçümü daha hızlı yapıyor. Ancak her sabah sıfır ayarı gerektiriyor ve bu ayar en az beş dakika sürüyor.*
- **Anlam riski**
  - **Kapsam:** Cümle başındaki koşul, sebep, temkin ya da olumsuzluk sonraki yüklemleri de kapsıyor olabilir. Bölünce kapsam ilk cümlede kalır.
    ✗ *Rapor onaylanırsa ekip genişletilecek ve bütçe artırılacak.* → *Rapor onaylanırsa ekip genişletilecek. Bütçe artırılacak.* (Bütçe artışı koşulsuz oldu. ANL-17)
  - **Ortak ek:** *toplanmış ve incelenmiştir* gibi bir yapıda -tir iki yüklemi birden kapsar. Bölerken ilk yüklemi de tam biçimine getir: *toplanmıştır.* Yalın bırakılan -mış aktarım gibi okunabilir (ANL-09).
  - **Dipnot:** Dipnot işareti kendi iddiasının yanında kalır. Bkz. `cumle-ritmi.md` → Dönüşümler ve `uzun-belge.md`.

### Yol 3: Zarf-fiille birleştirme

- **Ne yapar:** "ve" ile bağlı iki yüklemden birini zarf-fiile çevirir.
- **Ne zaman:** İki yüklemin öznesi, zamanı, kipi ve olumsuzluğu aynıysa.
- **Önce:** *Teknisyen kapağı açtı ve filtreyi değiştirdi.*
- **Sonra:** *Teknisyen kapağı açıp filtreyi değiştirdi.*
- **Anlam riski**
  - **Kip aktarımı:** -ıp almış fiil kendi zaman ve kip ekini taşımaz, ana yüklemin ekini paylaşır [Doğan 2023, s. 36, Delice'den aktararak]. Kipleri farklı iki yüklemi -ıp ile bağlama: "bildirir ve durdurabilir" → "bildirip durdurabilir" yazılırsa bildirim yükümlülüğü olanağa döner. Örnek ve ayrıntı: `cumle-ritmi.md` → D1, ANL-07.
  - **İşlev bağlamdan çıkar:** -ıp sıra da eşzamanlılık da bildirebilir; -ınca ve -arak yeni bir sebep ya da şart ilişkisi ekleyebilir [Akay Ahmed ve Ekşi 2023, s. 19-20, 31]. Ayrıntı: `cumle-ritmi.md` → D1, D2, D7.
  - **Özne:** Ediskun'a göre -ıp almış fiil sonraki fiille aynı kişi tarafından yapılır. Farklı özneli örnekler de vardır [Akay Ahmed ve Ekşi 2023, s. 20]. Özneleri farklı iki cümleyi -ıp ile bağlarsan kimin ne yaptığı belirsizleşebilir (ANL-19).

### Yol 4: de/da ile ekleme

- **Ne yapar:** Cümle başındaki ekleme sözünü atar, ekleneni "de/da" ile işaretler. TDK "da" bağlacına "-den başka" ve "ek olarak" anlamlarını verir [TDK-GTS].
- **Önce:** *Kurul bütçe taslağını onayladı. Ayrıca satın alma takvimini kabul etti.*
- **Sonra:** *Kurul bütçe taslağını onayladı. Satın alma takvimini de kabul etti.*
- **Anlam riski**
  - **Konum:** "de/da" hemen önündeki öğeyi kapsar (ANL-12). *Satın alma takvimini de kabul etti* başka bir belgenin daha kabul edildiğini söyler. *Kurul da takvimi kabul etti* ise başka birinin daha kabul ettiğini söyler.
  - **Öteki işlevler:** -sA almış fiilden sonra "da", "bile" anlamıyla koşulu geçersiz kılar [TDK-GTS]. *Onay gelirse iş başlar* ile *Onay gelse de iş başlar* aynı şeyi söylemez (ANL-17). Bazı cümlelerde "da" "ama" anlamı da taşır [TDK-GTS].
  - **Yazım:** Bağlaç olan "de/da" ayrı yazılır; ayrıntı `yazim-noktalama.md` → YN-97, YN-23.

### Yol 5: Virgülle sıralama

- **Ne yapar:** Aynı özneye bağlı, art arda "ve" ile zincirlenmiş yüklemleri virgülle sıralar. Son "ve" kalır. TDK'ye göre virgül eş görevli sözcükleri ve sıralı cümleleri ayırır [TDK-YK].
- **Ne zaman:** Üç ya da daha çok yüklem aynı özneye bağlıysa, zamanları ve kipleri aynıysa ve aralarında yalnızca sıra ya da ekleme ilişkisi varsa.
- **Önce:** *Teknisyen sensörü söktü ve temizledi ve yeniden taktı.*
- **Sonra:** *Teknisyen sensörü söktü, temizledi ve yeniden taktı.*
- **Anlam riski**
  - **Sıra:** Virgüllü dizide de olayların sırası korunur. Öğelerin yerini değiştirme (ANL-08).
  - **Bağın türü:** Zincirde bir "veya" ya da "ya da" varsa ona dokunma; "ve" ile "veya" aynı şey değildir (ANL-18).
  - **Kip ve kapsam:** Kipleri ya da olumsuzlukları farklı yüklemleri tek diziye toplama. Cümle başındaki bir koşul diziye katılan her yüklemi kapsar hâle gelebilir (ANL-17).
  - **Yazım:** "ve"nin önüne virgül konmaz; ayrıntı `yazim-noktalama.md` → YN-23, YZ-02.

### Bağlacı koruyup sadeleştirmek

Bazen bağlaç gereklidir ama ağırdır. O zaman aynı işlevi gören daha sade bir söz seç. Önce işlevi aşağıdaki envanterden doğrula, sonra registerı koru: Yazılı derlemde "ama" kurmacada, "fakat" daha resmî türlerde öne çıkar [Zeyrek 2014].

- **Önce:** *Ölçümler tekrarlandı. Bununla birlikte, ikinci ölçümde de aynı sapma görüldü.*
- **Sonra:** *Ölçümler tekrarlandı. Ancak ikinci ölçümde de aynı sapma görüldü.*
- Burada "Bununla birlikte" kabul olarak okunuyor: Ölçümün tekrarı, sapmanın kaybolmasını bekletir. "Ancak" aynı ilişkiyi kurar. Bağlaç "Ayrıca" olsaydı kabul ilişkisi kaybolurdu.

## İşlev envanteri

Her madde şu sırayla verilir: söz · işlev · register · kaynak. Altında yerine geçmediği söz ve yeni bir örnek vardır.

### Ekleme

**ve** · ekleme, sıralama · N · [TDK-GTS], [TDK-YK]
- TDK yalnızca iki öğe ya da cümle arasında "bir bağ" olduğunu söyler. Bağın türünü bağlam belirler. Önüne ve arkasına virgül konmaz [TDK-YK].
- Yerine geçmez: *veya* (ANL-18).
- Örnek: *Form doldurulur ve birim sorumlusuna verilir.*

**ile** (bağlaç) · ekleme · N · [TDK-GTS]
- Aynı görevdeki iki öğeyi bağlar. İki cümleyi bağlamaz.
- Yerine geçmez: edat olan *ile*. *Kalıp ile pres değiştirildi* (ikisi de değişti) ≠ *Kalıp presle değiştirildi* (pres araçtır).
- Örnek: *Kalıp ile pres aynı gün değiştirildi.*

**de / da** · ekleme; pekiştirme; -sA'dan sonra koşulsuzluk; bazen "ama" · N · [TDK-GTS], [TDK-YK]
- TDK bu söze on beş anlam verir. Bu dosya için önemli olanlar: "-den başka", "ek olarak", şartın geçerli olmadığını anlatan "bile".
- Yerine geçmez: cümle başındaki *ayrıca*; "de" konunca kapsam yanındaki öğeye daralır (ANL-12). *-sa da* ≠ *-sa* (ANL-17).
- Örnek: *Depo da denetlenecek.* · *Yağmur yağsa da tatbikat yapılacak.*

**ayrıca** · ekleme; "ayrı olarak"; "ayrı bir önem verilerek" · N · [TDK-GTS]
- Yerine geçmez: "ayrı olarak" anlamındayken silinmez ve *de* ile değiştirilmez.
- Örnek: *Ayrıca kantin saatleri değişti.* (ekleme) · *Bu talep ayrıca değerlendirilecek.* (ayrı olarak)

**bunun yanı sıra / buna ek olarak** · ekleme · R, A · [TDK-GTS]
- TDK "yanı sıra" için "...nın yanında" karşılığını verir. Yol 1'e göre silinebilir.
- Yerine geçmez: *bununla birlikte* (kabul ya da karşıtlık da olabilir).
- Örnek: *Bunun yanı sıra giriş kartları yenilenecek.*

**üstelik** · ekleme, çoğu zaman yükü artırarak · G, N · [TDK-GTS]
- TDK karşılıkları: ayrıca, bir de, bundan başka; bile. "bile" karşılığı, eklenen bilginin öncekini ağırlaştırabildiğini gösterir.
- Yerine geçmez: yansız *ayrıca*; ağırlaştırma kaybolur [değerlendirme].
- Örnek: *Sevkiyat gecikti, üstelik iki koli hasarlı geldi.*

**hem … hem (de)** · ekleme; bazen karşıtlık · N · [TDK-GTS], [TDK-YK], [Doğan 2023]
- TDK: görevdeş öğeleri eşitlik ya da karşıtlık işleviyle bağlar, *ne … ne*'nin karşıtıdır. Tekrarlı bağlaçlardan önce ve sonra virgül konmaz [TDK-YK]. Tek *ve*'ye göre ek bir vurgu taşır [Doğan 2023, s. 34, Gucker'den aktararak].
- Yerine geçmez: *ya … ya* (seçenek), *ne … ne* (olumsuz).
- Örnek: *Yeni form hem kısa hem anlaşılır.*

**hem de** · ekleme ve güçlendirme · N · [TDK-GTS]
- Yerine geçmez: düz *ve*; güçlendirme kaybolur.
- Örnek: *Rapor zamanında, hem de eksiksiz teslim edildi.*

**keza** · "aynı biçimde" · ESK, R · [TDK-GTS]
- Önceki hükmün başka bir öğe için de aynen geçerli olduğunu söyler, yeni bir hüküm eklemez [değerlendirme].
- Yerine geçmez: *ayrıca*; o yeni bilgi ekler.
- Örnek: *Ön kapı akşam altıda kilitlenir; arka kapı keza.*

### Güçlendirme ve ölçek

**hatta** · güçlendirme: aynı yönde daha uç bir öğe ekler · N · [TDK-GTS], [AÜ-TUR237]
- TDK: bile, dahi, üstelik, hem de anlamlarında anlamı kuvvetlendirir. Korkmaz üsteleme bildiren bağlayıcılar arasında sayar [AÜ-TUR237].
- Yerine geçmez: *ayrıca*; ölçek kaybolur (ANL-02). *yani*; yeniden söyleme değildir.
- Örnek: *Sistem yavaşladı, hatta iki kez tamamen durdu.*

**kaldı ki** · ek gerekçe · R, N · [TDK-GTS], [TDK-YK]
- TDK karşılıkları: bundan başka, bununla birlikte. İddiayı destekleyen bir gerekçe daha ekler. Bu gerekçe çoğu zaman öncekinden güçlüdür [değerlendirme]. "ki" ayrı yazılır [TDK-YK].
- Yerine geçmez: *çünkü*; asıl gerekçeyi değil ek gerekçeyi verir.
- Örnek: *Taşınmayı bu ay bitirmek zor; kaldı ki yeni binanın elektriği henüz bağlanmadı.*

**bile / dahi** · güçlendirme ve odak · N; dahi R · [TDK-GTS], [İşsever]
- Kendinden önceki öğeyi belirginleştirir [TDK-GTS]. Odağı işaretler, yeri neyi kapsadığını belirler [İşsever] (ANL-12).
- Yerine geçmez: *de*. "de" yalnızca ekler; "bile" öğeyi beklenenin en uç noktası gibi sunar [değerlendirme].
- Örnek: *Stajyer bile hatayı fark etti.* ≠ *Stajyer hatayı bile fark etti.*

### Karşıtlık

**ama** · karşıtlık; beklenmeyen sonuç; uyarı ve koşul; pekiştirme · N, G · [TDK-GTS], [Zeyrek 2014]
- TDK beş anlam verir: çelişkili iki cümleyi bağlama, uyarma ya da şartlı bir ifadeyi bağlama, beklenmeyen bir sonucu sebebine bağlama, pekiştirme, dikkat çekme. İki bağlacı karşılaştıran bir derlem çalışmasına göre kurmacada "fakat"a tercih edilir. Kabul ve edimsel çıkarım okumasına "fakat"tan daha kolay açılır [Zeyrek 2014].
- Yerine geçmez: *oysa* (aşağıya bak); zarf olan *ancak* ("yalnızca").
- Örnek: *Ateşi düştü ama öksürüğü sürüyor.*

**fakat** · karşıtlık · R, A · [TDK-GTS], [Zeyrek 2014]
- Araştırma makalesi, monografi gibi daha resmî türlerde "ama"ya tercih edilir [Zeyrek 2014].
- Yerine geçmez: "ama"nın uyarı ve pekiştirme kullanımları. TDK bu anlamları "fakat" için vermez.
- Örnek: *Başvuru alındı, fakat ekleri eksik.*

**lakin** · karşıtlık · ESK · [TDK-GTS]
- TDK'de "ama" ve "ancak" maddelerine gönderilir. Akademik ve iş metninde eski durur [değerlendirme].
- Örnek: *Yol kısaydı lakin dikti.*

**ancak** · bağlaç: karşıtlık · zarf: yalnızca; güçlükle; en erken · R, A · [TDK-GTS], [AÜ-TUR237]
- Korkmaz zıtlık bildiren bağlayıcılar arasında sayar [AÜ-TUR237].
- Yerine geçmez: zarf anlamındayken *ama*. *Ancak yöneticiler girebilir* (yalnızca onlar) ≠ *Ama yöneticiler girebilir.* "Ancak … -sa" gerekli koşul bildirir (ANL-17).
- Örnek: *Taslak hazır; ancak hukuk birimi henüz görmedi.*

**yalnız** (bağlaç) · karşıtlık, çekince · G · [TDK-GTS]
- TDK: "ama, fakat" anlamında. Zarf olarak "sadece" demektir.
- Yerine geçmez: zarf olan *yalnız*. Cümle başında mı, bir öğenin önünde mi, ona bak.
- Örnek: *Gelebilirsin, yalnız kapı altıda kapanıyor.*

**oysa / oysaki / hâlbuki** · karşıtlık: iki durumu karşı karşıya koyar · N · [TDK-GTS], [Erenbaş 2022], [TDK-YK]
- TDK: aralarında karşıtlık bulunan iki cümleyi "tersine olarak, aksine" anlamıyla bağlar. "oysa", "o ise" yapısından kalıplaşmış bir cümle başı edatıdır [Erenbaş 2022, s. 483]. "oysaki" ve "hâlbuki" bitişik yazılır [TDK-YK].
- Çoğu zaman sanılanla gerçek olanı ya da iki ayrı durumu karşılaştırır [değerlendirme].
- Yerine geçmez: kabul bildiren *ama*. *Yorgundu ama vardiyayı tamamladı* cümlesinde "oysa" uymaz: Karşılaştırılan iki durum yok, bir beklenti bozuluyor [değerlendirme].
- Örnek: *Kurul toplantının kısa süreceğini düşünüyordu; oysa gündemde on iki madde vardı.*

**ise** · karşılaştırmalı karşıtlık · N, A · [Erenbaş 2022]
- Ergin iki "ise" ayırır: koşul bildiren "ise" ile karşılaştırma içinde bağlama ve pekiştirme yapan edat "ise" [Erenbaş 2022, s. 485, Ergin'den aktararak]. Edat "ise" karşılaştırılan öğenin hemen arkasına gelir.
- Yerine geçmez: koşul *ise*. *Rapor hazır ise gönderin* (koşul) ≠ *Rapor ise hazır* (karşılaştırma). "ama" ile değiştirilince karşılaştırılan öğe belirsizleşebilir.
- Örnek: *Sabah vardiyasında arıza çıkmadı; gece vardiyasında ise iki arıza kaydedildi.*

**öte yandan** · başka bir yön; karşılık · R, A · [TDK-GTS]
- TDK: diğer taraftan, başka bir yönden, karşılık olarak. Hem ekleme hem karşıtlık okunabilir.
- Yerine geçmez: körlemesine *ayrıca* ya da *ama*. Önce hangisi olduğunu bul.
- Örnek: *Yeni yazılım hızlı; öte yandan lisans ücreti yüksek.*

**aksine / tersine** · düzeltici karşıtlık · N · [TDK-GTS]
- TDK: beklenenin aksine, karşıt olarak; bilakis. Önceki beklentinin ya da sözün tersinin doğru olduğunu söyler.
- Yerine geçmez: *ama*. "ama" bir karşıtlık kurar; "aksine" öncekini çürütür [değerlendirme].
- Örnek: *Gürültü azalmadı; aksine arttı.*

### Beklenti çelişkisi ve kabul

**yine de** · kabul: duruma rağmen · N · [TDK-GTS], [AÜ-TUR237]
- TDK "yine" maddesinde "öyle de olsa" ve "buna rağmen, bununla birlikte" anlamlarını verir. Korkmaz zıtlık bağlayıcıları arasında sayar [AÜ-TUR237].
- Yerine geçmez: *yine* ("bir kez daha").
- Örnek: *Hava soğuktu; yine de tatbikat açık alanda yapıldı.*

**buna rağmen / buna karşın** · kabul · N, R · [TDK-GTS]
- TDK "karşın" için bir şeyin gerekenin ya da mantığın tersine yapıldığını anlatır; "rağmen" aynı maddeye gönderilir.
- Yerine geçmez: *bu nedenle*; ilişkinin yönünü tersine çevirir.
- Örnek: *Uyarı levhası asıldı; buna rağmen yasak alana girişler sürdü.*

**ne var ki** · karşıtlık, çoğu zaman bir engeli açar · R, edebî · [TDK-GTS]
- TDK: aralarında aykırılık bulunan cümleleri bağlar. "Engel" yorumu [değerlendirme].
- Örnek: *Proje onaylandı; ne var ki ödenek gelecek yıla kaldı.*

**bununla birlikte / bununla beraber** · ekleme ya da kabul ya da karşıtlık · R, A · [TDK-GTS]
- TDK üç anlam verir: buna ek olarak; bunun böyle olduğuna bakmayarak; karşıtlama. Bkz. Anlam tuzakları.
- Örnek: *Örneklem küçüktü. Bununla birlikte bulgular önceki ölçümlerle uyumlu.* (kabul)

**gerçi** · kabul: karşı bir noktayı önceden tanır · G, N · [TDK-GTS]
- TDK: "her ne kadar … ise de". Asıl iddia çoğu zaman ardından "ama" ile gelir [değerlendirme].
- Yerine geçmez: *çünkü*.
- Örnek: *Gerçi bina eski, ama tesisatı yeni.*

**-sa da / her ne kadar … -sa da** · koşulsuzluk, kabul · N · [TDK-GTS]
- TDK "da" maddesi: şart bildiren fiilden sonra "bile" anlamıyla şartın geçerli olmadığını anlatır.
- Yerine geçmez: yalın *-sa*; koşula döner (ANL-17).
- Örnek: *Toplantıya katılamasan da tutanağı imzalaman gerekir.*

### Sebep

**çünkü** · sebep · N · [TDK-GTS], [TDK-YK]
- TDK: şu sebeple; zira. "ki" kalıplaştığı için bitişik yazılır [TDK-YK]. Sebebi yeni bilgi olarak sunar [değerlendirme].
- Yerine geçmez: *madem*, *kaldı ki*.
- Örnek: *Tatbikat ertelendi, çünkü yangın merdiveni boyanıyor.*

**zira** · sebep · R, ESK · [TDK-GTS], [AÜ-TUR237]
- TDK'de "çünkü" maddesine gönderilir. Korkmaz sebep bildiren bağlayıcılar arasında sayar [AÜ-TUR237].
- Örnek: *Başvurular yeniden incelenecek; zira bazı belgeler okunamıyor.*

**-dığı için / nedeniyle / sebebiyle** · sebep · N; nedeniyle R, A · [TDK-GTS]
- TDK "için" maddesinde neden-sonuç ve "-den dolayı" anlamlarını verir. Aynı söz amaç da bildirir.
- Yerine geçmez: *-dığında* (zaman), *-mek için* (amaç). ANL-06, ANL-16.
- Örnek: *Sensör arızalı olduğu için ölçüm elle yapıldı.*

**madem / mademki** · ortak kabul edilmiş sebep · G, N · [TDK-GTS], [TDK-YK]
- TDK: "değil mi ki", "-diği için", "-diğine göre" anlamlarında sebep gösterir. Bu karşılıklar sebebi iki tarafın da bildiği bir durum olarak sunar. Ardından çoğu zaman bir öneri ya da istek gelir [değerlendirme]. "mademki" bitişik yazılır [TDK-YK].
- Yerine geçmez: *çünkü* (yeni bilgi olan sebep); *eğer* (gerçekleşip gerçekleşmediği bilinmeyen koşul).
- Örnek: *Madem form hazır, bugün gönderilsin.*

### Sonuç

**bu nedenle / bu yüzden / bundan dolayı** · sonuç · N; bu nedenle A, R; bu yüzden G · [TDK-GTS], [AÜ-TUR237]
- TDK "bundan dolayı" için "bunun için; bu yüzden, bu sebeple" karşılıklarını verir. Korkmaz "bu nedenle"yi sonuç bildiren bağlayıcılar arasında sayar [AÜ-TUR237].
- Yerine geçmez: *demek ki* (çıkarım), *nitekim* (kanıt), *böylece* (varılan sonuç).
- Örnek: *Yol buzlanmıştı. Bu nedenle servis yarım saat gecikti.*

**dolayısıyla** · sonuç; "dolaylı olarak" · A, R · [TDK-GTS]
- TDK iki anlam verir: dolaylı olarak; (edat) sebebiyle. Cümle başında sonuç bildiren kullanımı akademik metinde sıktır; bu dosya için okunan makalelerde de böyle geçer [değerlendirme].
- Yerine geçmez: *demek ki*.
- Örnek: *Ölçüm aralığı kısaltıldı; dolayısıyla veri sayısı arttı.*

**böylece / böylelikle** · bir sürecin vardığı sonuç; "bu biçimde" · N · [TDK-GTS]
- TDK: tam böyle, bu biçimde; en sonunda. Sonucun gerçekleştiğini söyler.
- Yerine geçmez: *amacıyla, için*. Niyet bildiren söz "böylece" yapılırsa amaç gerçekleşmiş sonuca döner (ANL-16).
- Örnek: *Kayıtlar tek tabloda toplandı; böylece aynı kişiye ait iki dosya kalmadı.*

**sonuç olarak / sonuçta** · sonuç ya da özet; "sonuçta" ayrıca "nasıl olsa" · N; sonuçta G · [TDK-GTS]
- TDK "sonuçta" için "sonuç olarak, son kertede" ve "nasıl olsa" anlamlarını verir. Özeti açıyorsa silinebilir. Bir bulgudan çıkan sonucu açıyorsa korunur (Yol 1).
- Örnek: *Sonuçta herkes aynı formu dolduracak.* ("nasıl olsa" anlamında)

### Konuşanın çıkarımı

**demek ki** · konuşanın çıkarımı · G, N · [TDK-GTS], [TDK-YK]
- TDK "demek" maddesinde "yani, anlaşılan" anlamını verir. Dünyadaki bir sebep-sonuç bağını değil, konuşanın kanıttan vardığı yargıyı bildirir [değerlendirme]. "ki" ayrı yazılır [TDK-YK].
- Yerine geçmez: *bu yüzden, dolayısıyla*; çıkarım nedensel bir iddiaya döner (ANL-05).
- Örnek: *Koridor ıslak; demek ki temizlik yeni yapılmış.*

**öyleyse / o hâlde** · çıkarım; çoğu zaman bir karar ya da öneri açar · G, N; o hâlde R · [TDK-GTS], [Erenbaş 2022]
- TDK: bu durum karşısında, sonuç olarak denilebilir ki. "öyleyse" koşul kökenlidir: "o", "ile" ve "ise" öğelerinden kalıplaşmıştır [Erenbaş 2022, s. 473].
- Yerine geçmez: betimleyici bir raporda *bu nedenle*. Konuşanın yargısı olguya döner [değerlendirme].
- Örnek: *Anahtar kayıp değil, nöbetçide. Öyleyse kilit değiştirilmesin.*

**yani** · açıklama, yeniden söyleme · G, N · [TDK-GTS]
- TDK: "demek oluyor ki"; "sözün kısası, doğrusu".
- Yerine geçmez: *örneğin*; "yani" eşdeğeri verir, "örneğin" bir üyeyi. *hatta*; ölçek bildirmez.
- Örnek: *Sözleşme on iki ay, yani bir yıl sürecek.*

**meğer / meğerse** · sonradan fark etme · G · [TDK-GTS]
- TDK: önceden bilinmeyen, sonradan anlaşılan bir durumu bildirir. Çoğu zaman -mış ile kurulur [değerlendirme]. Bu -mış'ı -dı yapma (ANL-09).
- Yerine geçmez: *oysa*; o karşılaştırır, keşif bildirmez.
- Örnek: *Alarmın bozuk olduğu sanılıyordu; meğer pili bitmiş.*

### Doğrulama

**nitekim** · doğrulama; "sonuç olarak" · A, R · [TDK-GTS], [AÜ-TUR237]
- TDK iki anlam verir: gerçekten, hakikaten; sonuç olarak. Korkmaz üsteleme bildiren bağlayıcılar arasında sayar [AÜ-TUR237]. Sık görülen kullanımı, önceki bir iddiayı ya da beklentiyi sonradan gelen bir olguyla doğrulamaktır [değerlendirme].
- Yerine geçmez: doğrulama kullanımında *bu nedenle*; sonraki olgu öncekinin kanıtıdır, sonucu değildir. Sözlük "sonuç olarak" anlamını da verdiği için hangi anlamda kullanıldığını bağlamdan bul. Emin değilsen değiştirme.
- Örnek: *Eski kabloların ısınacağı önceki raporda yazılmıştı; nitekim ilk hafta iki priz eridi.*

### Örnekleme ve özetleme

**örneğin** · örnekleme · N · [TDK-GTS]
- Yerine geçmez: *yani*. Örnek bütünü vermez; "yani" yapılırsa kapsam değişir (ANL-03).
- Örnek: *Bazı belgeler, örneğin imza sirküleri, elden alınır.*

**kısacası / velhasıl / hâsılı** · özetleme · G; velhasıl, hâsılı ESK · [TDK-GTS]
- TDK: kısa söylemek gerekirse.
- Yerine geçmez: *bu nedenle*. Özet yeni bir iddia eklememeli [değerlendirme].
- Örnek: *Kısacası teslim tarihi değişmedi.*

### Koşul

**eğer / şayet** · koşulu pekiştirme · N; şayet R · [TDK-GTS]
- TDK: şart anlamını güçlendirmek için şartlı cümlenin başına gelir. Koşulu -sA eki taşır (Yol 1).
- Yerine geçmez: *madem*.
- Örnek: *Eğer basınç düşerse vana kapanır.*

**-dığı takdirde** · koşul · R · [TDK-GTS]
- TDK "takdirde" için "...-dığı zaman" karşılığını verir. Resmî metinde koşul bildirir [değerlendirme]. Olumsuz biçimi (*verilmediği takdirde*) koşulun kutbunu taşır (ANL-17).
- Yerine geçmez: *-dığı sürece* (aşağıya bak).
- Örnek: *Belge süresinde verilmediği takdirde başvuru geçersiz sayılır.*

**-dığı sürece** · süren koşul · N, R · [kaynak doğrulanamadı]
- Sonuç, koşul sürdükçe geçerlidir. TDK sözlüğünde ayrı madde olarak yok.
- Yerine geçmez: *-dığı takdirde, -sa*; bunlar koşulun ne kadar süreceğini söylemez.
- Örnek: *Kart etkin olduğu sürece turnike açılır.*

**yeter ki** · tek koşul · G, N · [TDK-GTS], [TDK-YK]
- TDK: "ancak, şu şartla". Sonucu bu tek koşula bağlar. "ki" ayrı yazılır [TDK-YK].
- Yerine geçmez: yalın *eğer*; koşulun tek koşul olduğu bilgisi düşebilir (ANL-17).
- Örnek: *Rapor bugün çıkar, yeter ki son imza atılsın.*

### Seçenek

**veya / ya da** · seçenek · N; veya R, A · [TDK-GTS], [TDK-YK]
- TDK "veya" için iki anlam verir: ayrı ama aynı değerdeki iki şeyden ikincisinin önüne gelir; konu birden çok şey için aynı anda söz konusuysa da kullanılır. Yani "veya" her zaman "yalnızca biri" demek değildir. "ya da" ayrı yazılır. "ve, veya" bağlaçlarının önüne ve arkasına virgül konmaz [TDK-YK].
- Yerine geçmez: *ve* (ANL-18).
- Örnek: *Başvuru e-postayla veya elden yapılabilir.*

**yahut / veyahut** · seçenek; "yahut" ayrıca "daha doğrusu" · ESK · [TDK-GTS]
- "yahut" sözden caymayı da bildirebilir. O zaman seçenek değil düzeltmedir.
- Örnek: *Pazartesi yahut salı uğrarım.*

**ya … ya (da)** · seçenek: biri olacak ya da biri seçilmeli · N · [TDK-GTS], [TDK-YK]
- Virgül konmaz [TDK-YK].
- Yerine geçmez: *ister … ister* (fark gözetmeme), *hem … hem* (ikisi birden).
- Örnek: *Formu ya bugün ya da pazartesi teslim edin.*

**ister … ister** · seçenekler arasında fark gözetmeme · N · [TDK-GTS], [TDK-YK]
- TDK: seçeneklerden herhangi birinin onanmasında sakınca olmadığını anlatır. Sonuç seçime bağlı değildir.
- Yerine geçmez: *ya … ya*; seçim zorunluluğu bildirir.
- Örnek: *İster sabah ister öğleden sonra gelin, sıra numarası alınır.*

**gerek … gerek(se)** · birlikte kapsama · R, ESK · [TDK-GTS]
- TDK: birleştirme, eşitlik, istenileni seçme gibi anlamlar katar. Çoğu bağlamda "her ikisi de" diye okunur [değerlendirme].
- Yerine geçmez: *ya … ya*.
- Örnek: *Gerek kadrolu gerek geçici personel eğitime katılacak.*

### Dışlama ve düzeltme

**ne … ne** · dışlama: ikisi de değil · N · [TDK-GTS], [TDK-YK], [Doğan 2023]
- TDK: olumsuzluk anlamı veren tekrarlı söz, *hem … hem*'in karşıtı. Yüklem çoğu zaman olumludur. TDK yüklemin olumsuz kullanıldığı yapıları ayrıca sayar. Doğan "birlikte bağlama edatları" arasında sayar [Doğan 2023, s. 36]. Virgül konmaz [TDK-YK].
- Yerine geçmez: *ve*, *hem … hem*; kutup döner (ANL-04).
- Örnek: *Ne alarm çaldı ne kayıt düştü.*

**değil** (bağlaç) · düzeltme: birini reddeder, ötekini kabul eder · N · [TDK-GTS]
- Yerine geçmez: *ama*.
- Örnek: *Toplantı salı değil, perşembe.*

### ki

**ki** · açıklama; pekiştirme; "o kadar … ki" yapısında derece ve sonuç · N · [TDK-GTS], [TDK-YK]
- TDK: anlamca ilgili cümleleri bağlar; özneyi ya da tümleci güçlendirir; "öyle, o kadar" sözlerinden sonra güç katar; şaşma bildirir. Yazımı (ayrı "ki" ve bitişik yazılan kalıplaşmış sözler): `yazim-noktalama.md` → YN-99.
- Yerine geçmez: "o kadar … ki" yapısını "çok … ve" yapmak; sonuç bağı düşer [değerlendirme].
- Örnek: *Salon öyle kalabalıktı ki kapı kapanmadı.*

## Anlam tuzakları

**Bağlaç eklemek, kaynakta olmayan bir ilişki eklemektir.** İki cümle bağlaçsız yan yana duruyorsa kaynak aralarındaki ilişkiyi açıkça söylememiştir. Okurun belki çıkaracağı bir ilişkiyi bağlaçla kesinleştirmek de eklemedir (ANL-06).

✗ *Kayıtlar dijital ortama taşındı. Arşiv odası boşaltıldı.* → *Kayıtlar dijital ortama taşındığı için arşiv odası boşaltıldı.* (Kaynakta sebep yok.)

- **Önce:** *Kayıtlar dijital ortama taşındı. Arşiv odası boşaltıldı.*
- **Sonra:** *Kayıtlar dijital ortama taşındı ve arşiv odası boşaltıldı.*

Aşağıdaki çiftler eş anlamlı sanılır ama değildir. Her birinde soldaki söz sağdakiyle değiştirilirse ilişki değişir.

| Çift | Fark | ✗ Kayma | ANL |
|---|---|---|---|
| ama ≠ oysa | "ama" bir beklentiyi bozar. "oysa" iki durumu karşı karşıya koyar. | *Yorgundu ama vardiyayı tamamladı.* → *Yorgundu, oysa vardiyayı tamamladı.* (kabul, iki durumun karşılaştırmasına döndü) | ANL-06 |
| ancak (zarf) ≠ ama | Zarf olan "ancak" sınırlar. | *Ancak bakım ekibi bu kapıyı kullanabilir.* → *Ama bakım ekibi bu kapıyı kullanabilir.* ("yalnızca" düştü) | ANL-03, ANL-17 |
| madem ≠ eğer | "madem" gerçekleşmiş bir durumu sebep yapar. "eğer" durumu belirsiz bırakır. | *Madem bütçe onaylandı, alım başlasın.* → *Bütçe onaylanırsa alım başlasın.* (olgu koşula döndü) | ANL-17 |
| demek ki ≠ bu yüzden | Çıkarım ile sebep farklıdır. | *Kapının önünde çamurlu iz var; demek ki biri bahçeden girmiş.* → *…; bu yüzden biri bahçeden girmiş.* (iz, girişin sebebi oldu) | ANL-05, ANL-06, ANL-09 |
| nitekim (doğrulama) ≠ bu nedenle | Kanıt ile sonuç farklıdır. | *Sistemin yükü kaldırmayacağı söylenmişti; nitekim ilk gün çöktü.* → *…; bu nedenle ilk gün çöktü.* (uyarı, çökmenin sebebine döndü) | ANL-06 |
| böylece ≠ amacıyla | Gerçekleşen sonuç ile niyet farklıdır. | *Bekleme süresini kısaltmak amacıyla ikinci bir gişe açıldı.* → *İkinci bir gişe açıldı; böylece bekleme süresi kısaldı.* | ANL-16 |
| bununla birlikte ≠ ayrıca | Kabul, eklemeye dönmez. | *Örneklem küçüktü. Bununla birlikte bulgular önceki ölçümlerle uyumlu.* → *Örneklem küçüktü. Ayrıca bulgular önceki ölçümlerle uyumlu.* (sınırlılık ile bulgu arasındaki gerilim kayboldu) | ANL-06 |
| hatta ≠ ayrıca | "hatta" aynı yönde daha uç bir öğe ekler. | *Kuyruk uzadı, hatta kapının dışına taştı.* → *Kuyruk uzadı, ayrıca kapının dışına taştı.* | ANL-02 |
| -sa da ≠ -sa | Koşulsuzluk ile koşul zıttır. | *Onay gelse de iş başlar.* → *Onay gelirse iş başlar.* | ANL-17 |
| -dığı sürece ≠ -dığı takdirde | Süren koşul ile tetikleyen koşul farklıdır. | *Hasta ateşli olduğu sürece izinli sayılır.* → *Hasta ateşli olduğu takdirde izinli sayılır.* (izin süresinin ateşe bağlı olduğu bilgisi düştü) | ANL-17 |
| hem … hem ≠ ya … ya | İkisi birden ile biri yeter farklıdır. | *Hem ehliyet hem kimlik istenir.* → *Ya ehliyet ya kimlik istenir.* | ANL-18 |
| ne … ne ≠ hem … hem | Yüklem olumlu olsa da anlam olumsuzdur. | *Ne sözleşme ne fatura imzalandı.* → *Hem sözleşme hem fatura imzalandı.* | ANL-04, ANL-18 |

**Denetimde bak:** Kaynaktaki her bağlaç yeni metinde aynı iki parça arasında, aynı işlevle duruyor mu? Yeni metindeki her bağlacın kaynakta bir karşılığı var mı?

Denetim betiği bazı bağlaçların sayısını izler, işlevini okumaz. Bu tablodaki kaymalarla yapılan sınamada betik bir kısmına yalnızca bir KONTROL satırı verdi (ör. ama → oysa, demek ki → bu yüzden). Bir kısmını ise hiç görmedi (ör. hatta → ayrıca, -dığı sürece → -dığı takdirde, hem … hem → ya … ya). Uyarı çıkmaması ilişkinin korunduğunu göstermez.

## Dağıtma tuzağı

Aynı ilişki için sırayla farklı bağlaç kullanmak da bir yapay zekâ izidir. Bir paragrafta art arda *Ancak … Bununla birlikte … Öte yandan … Buna karşın …* gelir, ama dördü de aynı ilişkiyi taşır.

- **Kanıt:** Wikipedia'nın yapay zekâ metni rehberi, aynı sözü tekrarlamamak için eşanlamlılar arasında dolaşmayı ("elegant variation") daha çok eski modellerde görülen bir iz olarak sayar. Olası nedeni olarak bazı modellerin tekrarı cezalandıran ayarlarını gösterir [WP-AI]. İngilizce denemelerde ChatGPT metinlerinin sözcük çeşitliliği insan metinlerinden yüksek çıktı [Herbold 2023]. İngilizce haber metinlerinde ise sonuç tersineydi [Muñoz-Ortiz 2024]. Yani iz, türe ve modele göre değişir.
- **Ters iz:** Aynı bağlacı her cümlenin başına koymak da iz olabilir. ChatGPT-3'ün Türkçe bir metninde ardışık cümleler aynı "Ancak" kalıbıyla kurulmuştu [Coşar 2025, s. 382-383].
- **Neden sorun:** Her bağlaç farklı bir ilişkiye işaret eder. "Bununla birlikte" kabul, "öte yandan" karşılık da bildirebilir. Dört farklı söz okuru dört farklı ilişki aramaya iter [değerlendirme].
- **Kural:** Aynı ilişki için aynı bağlaç ya da hiç bağlaç. Farklı ilişki için farklı bağlaç. Eşanlamlılar arasında dolaşma; bağlaç gereksinimini azalt: Aynı türden maddeleri tek cümlede topla, karşılaştırmada "ise" kullan.

**Önce:** *Anket 300 çalışana ulaştı. Ancak yanıt oranı düşük kaldı. Bununla birlikte, soruların bir kısmı boş bırakıldı. Öte yandan, gece vardiyasına ulaşılamadı.*

**Sonra:** *Anket 300 çalışana ulaştı. Ancak yanıt oranı düşük kaldı, soruların bir kısmı boş bırakıldı ve gece vardiyasına ulaşılamadı.*

Üç cümle aynı ilişkiyi taşıyor: anketin sınırlılıkları. Tek "Ancak" bunu korur. **Uyarı:** Bu birleştirme, üç maddenin aynı türden olduğuna karar vermektir. Kaynakta maddelerden biri gerçekten başka bir ilişki taşıyorsa (ör. "Bununla birlikte" bir kabulü açıyorsa) onu ayrı tut.

Akademik metinde aynı ilişki için aynı bağlacın tekrarı tutarlılık sağlar. Tek başına iz sayılmaz [değerlendirme].

## Yazım ve noktalama

Bağlaçların yazımı ve çevresindeki virgül `yazim-noktalama.md`'de toplanmıştır: de/da (YN-97), ki ve bitişik yazılan ki'li sözler (YN-99), "ve, veya" ile tekrarlı bağlaçlarda virgül (YN-23, YZ-02), ara söz (YN-17, YN-37), şart ekinden sonra virgül (YN-23).

## Kaynaklar

Erişim tarihi hepsi için 5 Kasım 2026.

- **[TDK-GTS]** Türk Dil Kurumu. *Güncel Türkçe Sözlük.* https://sozluk.gov.tr — Bakılan maddeler: ama, ancak, fakat, lakin, yalnız, oysa, oysaki, hâlbuki, ne var ki, yine, karşın, rağmen, bununla birlikte, bununla beraber, gerçi, aksine, tersine, öte yandan, çünkü, zira, için, nedeniyle, sebebiyle, madem, mademki, bundan dolayı, bu yüzden, dolayısıyla, böylece, sonuçta, demek, öyleyse, o hâlde, yani, meğer, nitekim, örneğin, kısacası, velhasıl, ayrıca, yanı sıra, üstelik, hatta, kaldı ki, bile, dahi, da, ve, ile, hem, hem … hem …, hem de, keza, eğer, şayet, takdirde, yeter ki, veya, ya da, yahut, ya … ya …, ister, gerek … gerek …, ne … ne …, değil, ki.
- **[TDK-YK]** Türk Dil Kurumu. *Yazım Kılavuzu* (çevrim içi), "Bazı Kelime ve Eklerin Yazılışı" ve "Noktalama İşaretleri" bölümleri. https://yazim.tdk.gov.tr/content/03-bazi-kelime-ve-eklerin-yazilisi.html · https://yazim.tdk.gov.tr/content/09-noktalama-isaretleri.html
- **[Zeyrek 2014]** Zeyrek, Deniz. "On the distribution of the contrastive-concessive discourse connectives *ama* 'but/yet' and *fakat* 'but' in written Turkish." Suihkonen, P. ve Whaley, L. J. (ed.), *On Diversity and Complexity of Languages Spoken in Europe and North and Central Asia*, Studies in Language Companion Series 164, John Benjamins, 2014, s. 251-274. https://doi.org/10.1075/slcs.164.09zey — Yalnızca yayıncı sayfasındaki özet okundu: https://www.benjamins.com/catalog/slcs.164.09zey
- **[Erenbaş 2022]** Erenbaş Pehlivan, Seher. "Çağdaş Türk Lehçelerinde /–sA/ Ekli Bağlama Edatları." *Uluslararası Türk Lehçe Araştırmaları Dergisi (TÜRKLAD)* 6/2 (2022): 467-499. https://dergipark.org.tr/tr/download/article-file/2778783
- **[Doğan 2023]** Doğan, Ahmet Turan. "Türkiye Türkçesinde Birlikte Bağlama Edatları Üzerine." *Uluslararası Türk Lehçe Araştırmaları Dergisi (TÜRKLAD)* 7/1 (2023): 31-44. https://dergipark.org.tr/tr/download/article-file/2842440 — s. 36'da Delice'nin (2012) -Ip görüşü aktarılır; Delice'nin çalışması ayrıca okunmadı.
- **[Akay Ahmed ve Ekşi 2023]** Akay Ahmed, Asuman ve Ekşi, Sibel. "Functional Use of Gerunds in Teaching Turkish as a Foreign Language." *International Journal of Languages' Education and Teaching* 11/4 (2023): 15-32. https://dergipark.org.tr/tr/download/article-file/3696513
- **[AÜ-TUR237]** Ankara Üniversitesi Açık Ders Malzemeleri. *TUR237 Türkiye Türkçesi Sözcük Türleri, 12. hafta: Bağlaçlar.* https://acikders.ankara.edu.tr/mod/resource/view.php?id=88502 — Korkmaz'ın (*Türkiye Türkçesi Grameri*, 2014, s. 1095-1136) işlevsel sınıflandırması bu nottan aktarıldı; kitabın kendisi okunmadı.
- **[Deniz ve Demir 2019]** Deniz, Kemalettin ve Demir, Elif. "İşlevlerine Göre Bağlaçları Konu Edinen Araştırmalar." *Millî Eğitim* 48 (Özel Sayı 1) (2019): 903-915. https://dergipark.org.tr/en/download/article-file/931223 — Türkçe öğretiminde bağlaçları işlevlerine göre inceleyen 21 çalışmayı derler. Bu dosyadaki işlev gruplarının (ekleme, karşıtlık, sebep, sonuç, açıklama, pekiştirme, şart, seçme) yaygınlığına dayanak olarak kullanıldı.
- **[İşsever]** İşsever, Selçuk. *Türkçede Bilgi Yapısının Gerçekleşmesi: Konu ve Odak* (ders notu). Ankara Üniversitesi Açık Ders Malzemeleri. https://acikders.ankara.edu.tr/mod/resource/view.php?id=115977
- **[Coşar 2025]** Coşar, Asiye Mevhibe. "Söz Dizimi Açısından ChatGPT'nin Türkçesine Bir Bakış." *Uludağ Üniversitesi Fen-Edebiyat Fakültesi Sosyal Bilimler Dergisi* 26/48 (2025): 377-389. (Makalenin kendi atıf satırı 2025 yılını verir; kabul tarihi 4 Kasım 2024.)
- **[Bergin ve Atasoy 2026]** Bergin, Burak ve Atasoy, Arzu. "Söz Varlığı Unsurları Bağlamında Yapay Zekâ ve Öğrenci Metinleri Üzerine Bir İnceleme." *Uluslararası Türkçe Öğretimi Araştırmaları Dergisi* 6/2 (2026): 415-438. https://dergipark.org.tr/tr/download/article-file/5339956 — s. 425, Tablo 9 (en sık 50 sözcük). https://doi.org/10.21550/sosbilder.1568554
- **[Herbold 2023]** Herbold, Steffen; Hautli-Janisz, Annette; Heuer, Ute; Kikteva, Zlata; Trautsch, Alexander. "AI, write an essay for me: A large-scale comparison of human-written versus ChatGPT-generated essays." arXiv:2304.14276v1, 2023. https://arxiv.org/abs/2304.14276
- **[Kobak 2025]** Kobak, Dmitry; González-Márquez, Rita; Horvát, Emőke-Ágnes; Lause, Jan. "Delving into LLM-assisted writing in biomedical publications through excess vocabulary." arXiv:2406.07016v5, 3 Temmuz 2025. https://arxiv.org/abs/2406.07016
- **[Muñoz-Ortiz 2024]** Muñoz-Ortiz, Alberto; Gómez-Rodríguez, Carlos; Vilares, David. "Contrasting Linguistic Patterns in Human and LLM-Generated News Text." *Artificial Intelligence Review* 57 (2024): 265. https://arxiv.org/abs/2308.09067
- **[WP-AI]** Wikipedia (WikiProject AI Cleanup). "Wikipedia:Signs of AI writing", "Lexical diversity/elegant variation" ve "High density of 'AI vocabulary' words" bölümleri. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
