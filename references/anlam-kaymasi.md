# Anlam kayması tuzakları

Bu dosya, Türkçe bir metni doğallaştırırken anlamın nerede sessizce kaydığını gösterir. `kaliplar.md` neyin yapay durduğunu, bu dosya ise düzeltirken neyin bozulmaması gerektiğini anlatır. `kaliplar.md`, `yazim-noktalama.md`, `baglaclar-ve-gecisler.md` ya da `cumle-ritmi.md` ile çatışırsa bu dosya kazanır.

Kaynakta bir olgu, hesap ya da tarih hatası görürsen düzeltme: Metne dokunmadan kullanıcıya bildir. Hatayı düzeltmek de içeriği değiştirmektir.

Her tuzakta üç satır var: **Kayma** (yanlış dönüşüm), **Güvenli** (anlamı koruyan biçim) ve **Bak** (denetimde neye bakılacağı). Denetim betiği (`scripts/anlam_denetimi.py`) bu tuzakların çoğunda ilgili sözcüklerin sayısı değişince uyarı verir, ama anlamı okuyan sensin.

## Dizin

- ANL-01 Temkin ve olasılık
- ANL-02 Derece sözü iddianın parçasıdır
- ANL-03 Kapsam ve niceleyiciler
- ANL-04 Olumsuzluk
- ANL-05 İlişki nedensellik değildir
- ANL-06 Neden-sonuç bağı eklemek ya da silmek
- ANL-07 Kip: türü ve gücü
- ANL-08 Zaman ve görünüş
- ANL-09 Kanıtsallık: -dı ve -mış
- ANL-10 -DIr eki
- ANL-11 Özne ve eylemi yapan
- ANL-12 Odak ve kapsam sözlerinin yeri
- ANL-13 Karşılaştırmanın yönü ve tabanı
- ANL-14 Alan terimleri
- ANL-15 "Boş" sanılan ama bilgi taşıyan sözler
- ANL-16 Amaç, sonuç ve olayın durumu
- ANL-17 Koşul ve istisna
- ANL-18 Mantıksal bağ ve soru
- ANL-19 Roller: hâl ekleri, çatı, -lı/-sız
- ANL-20 Niceleyicinin dağılımı
- ANL-21 Yazarın sesi ve söz sanatları
- ANL-22 Görüşün sahibi ve hukuki statüsü
- ANL-23 Olan hukuk ile olması gereken hukuk

---

### ANL-01 · Temkin ve olasılık

Temkin sözleri (olabilir, -abilir/-ebilir, muhtemelen, düşündürmektedir, işaret etmektedir, yaklaşık, kısmen) yazarın ne kadar emin olduğunu söyler. Akademik ve tıbbi metinde en sık kayan bilgi budur.

- **Kayma:** *Bu bulgu, gece çalışmasının bel ağrısıyla ilişkili olabileceğini düşündürmektedir.* → *Gece çalışması bel ağrısıyla ilişkilidir.*
- **Güvenli:** *Bu bulgu, gece çalışmasının bel ağrısıyla ilişkili olabileceğini düşündürüyor.* (Akademik metinde "-mektedir" de kalabilir.)
- **Kayma:** *Yaklaşık 100 kişi geldi.* → *Muhtemelen 100 kişi geldi.* (Sayının yaklaşık olduğu bilgisi, sayının doğru olma olasılığına dönüştü.)
- **Kayma:** *Bulgular ilacın etkili olabileceğini düşündürüyor.* → *İlaç etkili olabilir.* (İddianın bulgulara dayandığı bilgisi düştü.)
- **Bak:** Kaynaktaki her temkin sözünün yeni metinde aynı önermeye bağlı bir karşılığı var mı? Temkin sözleri farklı işler görür: olasılık (olabilir), sayısal yaklaşıklık (yaklaşık), kısmi kapsam (kısmen), kanıta dayalı çıkarım (düşündürmektedir). İki söz aynı işi görüyorsa ("olabilir" + "muhtemelen") biri silinebilir. Farklı işler görüyorsa hiçbiri "çift temkin" diye silinmez.

### ANL-02 · Derece sözü iddianın parçasıdır

İki tür pekiştirme vardır. **Süs:** eşsiz, muazzam, son derece kritik, inanılmaz. Bunlar eş güçte sade bir sözle değiştirilir (KLS-05). Övgü bildirenler ("eşsiz", "büyüleyici") bir değerlendirmedir; silmeden önce kullanıcıya sorulur (KLS-07). **Derece:** büyük ölçüde, önemli ölçüde, anlamlı düzeyde, belirgin biçimde, hafifçe, kısmen, neredeyse. Bunlar ölçülebilir bir iddianın büyüklüğünü söyler ve korunur.

- **Kayma:** *Yeni havalandırma sistemi toz maruziyetini büyük ölçüde azalttı.* → *Yeni havalandırma sistemi toz maruziyetini azalttı.*
- **Kayma (ekleme):** *Çalışma alanı verimliliği etkiler.* → *Verimlilik büyük ölçüde çalışma alanına bağlıdır.*
- **Güvenli:** Derece sözünü koru. Süs pekiştirmeyi silerken bile iddianın gücünü düşürüyorsan bir eşdeğerini bırak: *son derece kritik bir rol oynar* → *çok önemli bir rol oynar*. "Çok etkiler" yazma: Önem değerlendirmesini nedensel bir iddiaya çevirir (ANL-05).
- **Bak:** Kaynakta olmayan bir derece sözü eklendi mi? Kaynaktaki bir derece sözü düştü mü?

### ANL-03 · Kapsam ve niceleyiciler

bazı, birkaç, birçok, çoğu, tüm, her, hiçbir, genellikle, nadiren, en az, en fazla, neredeyse ve yarısı gibi sözler iddianın kimi ya da neyi kapsadığını söyler.

- **Kayma:** *Bazı çalışanlar molaları yetersiz buluyor.* → *Çalışanlar molaları yetersiz buluyor.* (Sınırlı bir iddia genellemeye dönüştü. Okur çoğu zaman "hepsi" diye anlar.)
- **Kayma (ekleme):** *Yaz aylarında sıvı tüketimi ihmal edilebiliyor.* → *Yaz aylarında sıvı tüketimi çoğu zaman ihmal ediliyor.* (Kaynakta "çoğu zaman" yok, "-ebiliyor" da kesinleşti.)
- **Güvenli:** Niceleyiciyi aynen ya da eş kapsamlı bir sözle koru (birçok ↔ pek çok; çoğu ↔ büyük kısmı).
- **Bak:** "bazı/birçok/çoğu/tüm" birbirine dönüştü mü? Kaynakta olmayan bir sıklık sözü (genellikle, çoğu zaman, her zaman) eklendi mi?

### ANL-04 · Olumsuzluk

Olumsuzluk Türkçede çoğu zaman ekle gelir (-mA-, -mAz, -mAdAn) ve uzun bir cümlede gözden kaçar.

- **Kayma:** *Yaş grupları arasında anlamlı bir fark bulunmamıştır.* → *Yaşın bir etkisi yoktur.* ("Anlamlı fark bulunmadı", "etki yok" demek değildir: Kanıt yokluğu yokluğun kanıtı değildir.)
- **Kayma:** *Başarısız değil.* → *Başarılı.* (Olumsuzun olumsuzu her zaman zıt anlamlı değildir.)
- **Kayma:** *Olmadığı söylenemez.* → *Olmadığı söylenebilir.*
- **Kayma (kapsam):** *Gelmen gerekmiyor.* → *Gelmemen gerekiyor.* (Yükümlülüğün yokluğu, yapmama yükümlülüğüne dönüştü.)
- **Kayma (gizli olumsuzluk):** *Ne bütçe ne personel konusunda karar alındı.* → *Bütçe ve personel konusunda karar alındı.* (Yüklem olumlu, anlam olumsuz. Aynı tuzak "pek ... değil" ve "-mış gibi, sanki" yapılarında da var.)
- **Kayma (olumsuz emir):** *Burada beklemeyin.* → *Burada bekleyin.*
- **Güvenli:** Olumsuzluğu aynı öğede tut: *anlamlı bir fark bulunmadı*, *başarısız sayılmaz*.
- **Bak:** Olumsuz yüklem ve "değil/yok/hiç" sayısı aynı mı? Değiştiyse hangi önermenin kutbu döndü? Yüklem sayımı "ne ... ne", "pek ... değil" ve "-mış gibi" yapılarını görmez, bunları ayrıca ara. Olumsuzluk kipe mi bağlı ("gerekmiyor"), eyleme mi ("gelmemen")?

### ANL-05 · İlişki nedensellik değildir

"İlişkili, bağlantılı, birlikte görülür, -dıkça ... artar" sözleri bir eşlik bildirir. "Artırır, azaltır, yol açar, neden olur, etkiler, sağlar, belirler" ise neden bildirir.

- **Kayma:** *Gürültü maruziyeti işitme kaybıyla ilişkili bulunmuştur.* → *Gürültü maruziyeti işitme kaybını artırmaktadır.*
- **Kayma:** *Düzenli uyku akademik başarıda önemli bir rol oynar.* → *Düzenli uyku akademik başarıyı belirler.* ("rol oynamak" katkıdır, "belirlemek" tek başına belirleyicilik)
- **Güvenli:** *Gürültü maruziyeti işitme kaybıyla ilişkili bulundu.* / *Düzenli uyku akademik başarı için önemlidir.*
- **Bak:** "ilişki" sözü kayboldu da yerine bir neden fiili mi girdi?

### ANL-06 · Neden-sonuç bağı eklemek ya da silmek

İki cümleyi birleştirmek ya da bir bağlaç seçmek, aralarına bir ilişki koymak demektir. Zarf-fiillerin kurduğu ilişkiyi ek değil bağlam belirler. Sık görülen işlevler şunlardır:
- **-ıp:** sıra ya da aynı olayın parçaları (*gülüp eğleniyorlardı* bir sıra bildirmez)
- **-arak:** tarz ya da araç
- **-ınca:** zaman, çoğu zaman sebep de sezdirir
- **-dığı için / -dığından:** sebep (*geldiğinden* sebep, *geldiğinde* zaman)
- **-dıkça:** orantı ya da tekrar (*ihtiyaç oldukça* "ihtiyaç olduğu her seferde" demektir, "arttıkça" demek değildir)
- **-ken:** eşzamanlılık ya da karşıtlık
- **-madan:** öncelik ya da yokluk

- **Kayma (silme):** *Molaları elli dakikada bire çektik. Bu düzenleme sayesinde bel ağrısı şikâyetleri azaldı.* → *Molaları elli dakikada bire çektik. Bel ağrısı şikâyetleri de azaldı.* (Şikâyetlerin azalmasını düzenlemeye bağlayan bilgi kayboldu.)
- **Kayma (ekleme):** *Her baret ayrı bir numarayla kayıtlı. Hiçbiri ortak kullanılmıyor.* → *Baretler numaralı olduğu için hiçbiri ortak kullanılmıyor.* (Kaynakta böyle bir sebep yok.)
- **Kayma (zincir):** *Havalandırma yenilendi. Bu, toz düzeyini düşürdü. Bu da öksürük şikâyetlerini azalttı.* → *Havalandırmanın yenilenmesiyle toz düzeyi düştü, öksürük şikâyetleri azaldı.* (A → B → C zinciri, A'nın iki ayrı sonucuna dönüştü.)
- **Güvenli:** *Havalandırmanın yenilenmesi toz düzeyini düşürdü, bu da öksürük şikâyetlerini azalttı.*
- **Bak:** Kaynaktaki her "sayesinde, için, nedeniyle, bu yüzden, bu da" bağı yeni metinde aynı iki öğe arasında duruyor mu? Yeni metindeki her bağın kaynakta bir karşılığı var mı?

### ANL-07 · Kip: türü ve gücü

Kip sözleri tek bir merdiven oluşturmaz, farklı türleri vardır:
- **olasılık:** olabilir, muhtemelen
- **çıkarım:** *Bu saatte evde olmalı.*
- **yetenek:** yapabilir
- **izin ve yetki:** *İşveren ceza kesebilir.*
- **öneri:** önerilir, tavsiye edilir
- **gereklilik:** yapılmalıdır, gerekir
- **yükümlülük ve yasak:** zorunludur, yasaktır

Tür de değişmez, aynı tür içindeki güç de. "-abilir" ve "-malı" eklerinin hangi türde kullanıldığını bağlamdan belirle.

- **Kayma:** *Eğitimin 12 Aralık'a kaydırılmasının uygun olacağı düşünülmektedir.* → *Eğitimi 12 Aralık'a kaydırıyoruz.* (öneri → karar)
- **Kayma:** *Hastaya parasetamol önerildi.* → *Hastaya parasetamol verilmelidir.* (geçmişteki öneri → genel zorunluluk)
- **Kayma (tür):** *İşçi sözleşmeyi feshedebilir.* → *İşçinin sözleşmeyi feshetmesi olasıdır.* (hak → olasılık) · *Bu saatte evde olmalı.* → *Bu saatte evde bulunması gerekir.* (tahmin → yükümlülük)
- **Kayma (mevzuat):** *İşveren, çalışanların sağlık gözetimini sağlar.* → *İşveren sağlık gözetimini sağlayabilir.* Mevzuat dilinde geniş zaman ("sağlar, bildirir") çoğu zaman yükümlülük bildirir. Tanım ya da yetki bildiren geniş zamanı da (*Bu Yönetmelik ... kapsar*) yükümlülüğe çevirme.
- **Kayma (birleştirme):** *Çalışan durumu amirine bildirir ve çalışmaktan kaçınma hakkını kullanabilir.* → *Çalışan durumu amirine bildirip çalışmaktan kaçınabilir.* (-ıp ile bağlanan yüklem ana yüklemin kipini aldı, bildirim yükümlülüğü isteğe bağlı hâle geldi.)
- **Kayma (gömme):** *Sahaya girerken baret takılması zorunludur; ancak bu kural yalnızca üretim alanı için geçerlidir.* → *Baret kuralı yalnızca üretim alanında geçerlidir.* (Yükümlülük artık söylenmiyor, yalnızca anılıyor. Hızlı okuyan, baret takması gerektiğini kaçırır.)
- **Güvenli:** Kip sözünü aynı basamakta tut. *tavsiye edilmektedir* → *önerilir*; *zorunludur* → *zorunlu*. Yükümlülükle istisnasını birleştirirken yükümlülüğü açık yüklemle söyle: *Üretim alanına girerken baret takmak zorunlu.*
- **Bak:** "gerek, -malı, zorunlu, öner, tavsiye, -abil" sayısı ve yeri aynı mı?

### ANL-08 · Zaman ve görünüş

*-mektedir / -yor* süren bir durumu, *-miştir / -dı* tamamlanmış bir olayı, *-ecek* geleceği, *-yordu* geçmişte süreni bildirir. "henüz, hâlâ, artık, yeniden" de zamana dairdir.

- **Kayma:** *Çalışmada okulların hijyen koşulları incelenmektedir.* → *Çalışmada okulların hijyen koşulları incelenmiştir.* (Bazı dergiler ve bölümler için doğru olabilir ama yazarın kararıdır. "Hafif" düzeltmede dokunma.)
- **Kayma:** *Çalışanlar evden çalışmanın zorluklarını deneyimlemektedir.* → *Çalışanlar evden çalışmanın zorluklarını yaşayarak öğrendi.* (süren durum → bitmiş olay, üstüne "öğrendi" bilgisi)
- **Kayma:** *Test süreci henüz başlamamıştır.* → *Test süreci başlamadı.* ("henüz" başlayacağını sezdirir)
- **Kayma:** *Muayeneye kadar çalışabilir.* → *Muayeneden sonra çalışabilir.*
- **Kayma:** *Görevli gelmişti.* → *Görevli geldi.* · *İşlem sürüyor.* → *İşlem sürecek.*
- **Bak:** Yüklemlerin zamanı ve görünüşü aynı mı? "henüz, hâlâ, artık, önce, sonra, kadar, itibaren, boyunca, en geç, en erken" yerinde ve aynı olaya bağlı mı?

### ANL-09 · Kanıtsallık: -dı ve -mış

Türkçede *-dı* bilgiyi doğrudan bilinen bir olgu gibi sunar. *-mış* ise aktarım, çıkarım, sonradan fark etme ya da tamamlanmışlık bildirebilir. *-dı* konuşanın olaya tanık olduğunu kanıtlamaz (*Cumhuriyet 1923'te ilan edildi.*), ama bilginin sunuluşunu belirler. Olay ve kaza raporlarında, tanık ifadelerinde ve aktarılan bilgide bu ayrım bir olgudur.

- **Kayma:** *Vardiya amirinin aktardığına göre işçi merdivenden düşmüş.* → *İşçi merdivenden düştü.* (aktarılan bilgi, doğrudan bilinen olguya dönüştü, kaynak da silindi)
- **Kayma (ters yön):** *Saat 14.35'te ilk müdahale yapıldı.* → *Saat 14.35'te ilk müdahale yapılmış.* (kesin bilinen olay, duyuma dönüştü)
- **Güvenli:** Aktarılan bilgide -mış'ı ve "göre, aktardığına göre, iddiaya göre" sözlerini koru.
- **Dikkat:** Akademik "-mıştır" (*bulunmuştur, saptanmıştır*) çoğu zaman tamamlanmış görünüş bildirir, duyulan geçmiş değildir. Ama çıkarım da bildirebilir: *Değerlendirmeye göre katılımcılar soruyu yanlış anlamıştır.* → *Katılımcılar soruyu yanlış anladı.* Bu dönüşüm çıkarımı doğrudan saptamaya çevirir. İşlevi bağlamdan belirle.
- **Bak:** Duyulan geçmiş biçimleri ve aktarım sözleri yeni metinde aynı önermelerde mi?

### ANL-10 · -DIr eki

Ekeylemdeki *-dır* resmi ve akademik metinde kesin bir saptama bildirir (*Bulgular anlamlıdır.*). Gündelik konuşmada ise bir tahmin bildirebilir (*Şimdi evdedir.* "Herhalde evde."). Ek düşürülünce ya da eklenince kesinlik değişebilir.

- **Kayma:** Gündelik bir mesajdaki *Kargo yarın elinizdedir.* (tahmin) → resmi bir bildirimde *Kargo yarın teslim edilecektir.* (taahhüt)
- **Güvenli:** Hafif seviyede *-dır*'a dokunma. Orta seviyede, *-dır* kesinlik ya da tahmin bildirmiyorsa ve metnin resmiyeti korunuyorsa düşürülebilir (*Bulgular önemlidir.* → *Bulgular önemli.* gündelik registerda). Gündelik metinde bir tahmin bildiriyorsa yerine *herhalde, muhtemelen* koyarak tahmini görünür kıl ya da olduğu gibi bırak.

### ANL-11 · Özne ve eylemi yapan

Edilgen bir cümleyi etkene çevirmek, birine bir eylem yüklemek demektir.

- **Kayma:** *Bu protokol, kurumun sağlık hizmetlerine yeni bir soluk getirecek.* → *Bu protokolle sağlık hizmetlerimizi genişleteceğiz.* (Özne "protokol"ken "biz" oldu, "genişletmek" diye kaynakta olmayan somut bir taahhüt eklendi.)
- **Kayma:** *Toplantı perşembe günü yapılacaktır.* → *Perşembe günü toplanıyoruz.* (konuşan belli değilken "biz" eklendi)
- **Kayma (hitap):** *Formu cuma gününe kadar doldurmanızı rica ederiz.* → *Formu cuma gününe kadar doldur.* ("siz" "sen"e, rica emre döndü. Hitap ve kişi, yazanla okur arasındaki ilişkiyi taşır. Betik bu kaymaya uyarı vermedi.)
- **Kayma (makam):** Resmî yazıda *Gereğini arz ederim.* → *Gereğini rica ederim.* (Resmî yazışma yönetmeliğine göre üst ve aynı düzeydeki makamlara giden yazı "arz ederim", alt makamlara giden yazı "rica ederim" ile biter [RYY md. 16/12]. Değişiklik yazının kime gittiğini değiştirir.)
- **Güvenli:** *Bu protokol, kurumun sağlık hizmetlerini ileriye taşıyacak.* / *Toplantı perşembe günü yapılacak.* / Hitabı (siz ya da sen, "Sayın", "Hanım", "Bey") ve resmî yazının kapanış ibaresini olduğu gibi bırak.
- **Bak:** Yeni metinde kaynakta olmayan bir özne (biz, ekip, kurum adı) var mı? Mecazın yerine kaynaktan çıkmayan somut bir eylem konmuş mu? Hitap ve kişi ekleri (-nız, -ın) kaynaktakiyle aynı mı?

### ANL-12 · Odak ve kapsam sözlerinin yeri

Türkçede yansız dizilişte vurgu çoğu zaman yüklemden hemen önceki öğededir (tonlama ve bağlam bunu değiştirebilir). "de/da, bile, sadece, yalnızca, mi" ise yanına geldiği öğeyi etkiler. Öğe sırası değişince bu sözlerin neyi kapsadığı da değişebilir.

- **Kayma:** *Sadece gece vardiyasında koruyucu gözlük takılıyor.* → *Gece vardiyasında sadece koruyucu gözlük takılıyor.* (hangi vardiya → hangi ekipman)
- **Kayma:** *Ahmet de toplantıya katıldı.* → *Ahmet toplantıya da katıldı.* (başkaları da katıldı → Ahmet başka yerlere de katıldı)
- **Güvenli:** Kapsam sözünü kaynakta kapsadığı öğenin hemen yanında tut. Öğe sırasını değiştirdiğin cümlede vurgunun aynı öğede kaldığını kontrol et.

### ANL-13 · Karşılaştırmanın yönü ve tabanı

- **Kayma:** *Kış aylarında PM2,5 değerleri yaz aylarına göre %41 daha yüksektir.* → *Yaz aylarında PM2,5 değerleri %41 daha düşüktür.* (Kış değeri yazınkinin 1,41 katıysa yaz değeri kışınkinin yaklaşık %29 altındadır, %41 değil. Yön değişince oran da değişir.)
- **Kayma:** *iki katına çıktı* → *%200 arttı* (iki katına çıkmak %100 artıştır)
- **Kayma:** *gündüz vardiyasına göre daha yüksek* → *daha yüksek* (karşılaştırma tabanı düştü)
- **Güvenli:** Karşılaştırmayı aynı yönde ve aynı tabanla yaz.
- **Bak:** "daha, en, -e göre, kıyasla, kat" sözleri ve yön fiilleri (arttı, azaldı, yükseldi, düştü) aynı mı?

### ANL-14 · Alan terimleri

Eş anlamlı görünen bazı sözler alanında farklı şeylerdir. Kullanıcının seçtiği terimi koru.

- **Tıp ve epidemiyoloji:** insidans ≠ prevalans · risk ≠ olasılık ≠ oran · anlamlı (istatistiksel) ≠ önemli · ilişki ≠ etki · sıklık ≠ yaygınlık (kaynaktaki hangisiyse)
- **İş sağlığı ve mevzuat:** iş kazası ≠ kaza · meslek hastalığı ≠ işle ilgili hastalık · çalışan ≠ işçi (6331 sayılı Kanun "çalışan" der, İş Kanunu "işçi") · işyeri hekimi ≠ hekim · risk değerlendirmesi ≠ risk analizi
- **İstatistik:** p, OR, RR, HR, %95 GA, n, ortalama ≠ ortanca
- **Hukuk:** "-ır" yükümlülüğü (ANL-07) · "madde, fıkra, bent" numaraları · kanun ve yönetmelik adları
- **Bak:** Kaynaktaki her terim yeni metinde aynı biçimde var mı? Betik kısaltmaları ve büyük harfli adları kendiliğinden, küçük harfli terimleri ise yalnızca `--terimler` ile verilirse denetler. Vermediğin terimleri sen kontrol edersin.

### ANL-15 · "Boş" sanılan ama bilgi taşıyan sözler

Bazı sözler klişeye benzer ama bir sınır çizer. Bunlar dolgu değildir.

- **Zaman sınırı:** *Son yıllarda iş kazası bildirimleri artmıştır.* → *İş kazası bildirimleri artmıştır.* (artışın zamanı kayboldu)
  Karşı örnek: *Günümüzde mesleki gürültü önemli bir sorundur.* cümlesindeki "Günümüzde" bir sınır çizmez, genel bir durumu süsler. Silinebilir (ACL-01). Fark şudur: Söz bir değişimin ya da olgunun zamanını mı sınırlıyor, yoksa yalnızca açılışı mı dolduruyor?
- **Yer sınırı:** *Türkiye'de* · *bu işletmede* · *çalışmamızda*
- **Kaynak:** *Bakanlık verilerine göre* · *Yılmaz ve arkadaşlarına göre* (silinirse iddia yazarın kendi iddiasına dönüşür)
- **Koşul:** *gerekli görülmesi hâlinde* · *aksi belirtilmedikçe*
- **Tanım:** *Bu raporda "çalışan" yalnızca geçici personeli kapsar.* (Silinirse sonraki bölümlerdeki her "çalışan" tüm personele dönüşür.)
- **Gönderge:** *Söz konusu ekipler* · *yukarıdaki tabloda* (Silinirse hangi grubun kastedildiği belirsizleşir. Gerekirse "bu ekipler" yap.)
- **Güvenli:** Bir sözü silmeden önce sor: Bu söz olmadan iddia daha geniş, daha kesin ya da başkasına ait mi oluyor? Öyleyse dolgu değildir.

### ANL-16 · Amaç, sonuç ve olayın durumu

"amacıyla, -mek için, hedefiyle" bir niyet bildirir. Eylemin başarıldığını söylemez. "Planlandı, kararlaştırıldı, onaylandı, uygulandı, tamamlandı" da ayrı olay durumlarıdır.

- **Kayma:** *Hataları önlemek amacıyla yeni bir kontrol listesi hazırlandı.* → *Yeni kontrol listesiyle hatalar önlendi.* (niyet → gerçekleşmiş sonuç)
- **Kayma:** *Çalışanın işe dönüşü planlandı.* → *Çalışan işe döndü.*
- **Kayma:** *Taslak kurula sunuldu.* → *Taslak kurulda kabul edildi.*
- **Güvenli:** *Hataları önlemek için yeni bir kontrol listesi hazırlandı.*
- **Bak:** Amaç sözü sonuca, plan ya da öneri gerçekleşmiş olaya dönüştü mü?

### ANL-17 · Koşul ve istisna

Bir koşulun dört parçası vardır: koşulun kendisi, sonucu, istisnası ve hiçbir şey söylenmezse geçerli olan durum. Koşul gerekli mi, yeterli mi, gerçekleşmemiş bir geçmişe mi ait, bunlar da korunur.

- **Kayma (gerekli → yeterli):** *Ancak onay gelirse kullanılabilir.* → *Onay gelirse kullanılabilir.* ("ancak" düşünce onay tek koşul olmaktan çıktı.)
- **Kayma (kutup):** *Aksi kararlaştırılmadıkça uygulama sürer.* → *Aksi kararlaştırılırsa uygulama sürer.*
- **Kayma (karşıolgusal):** *Bütçe ayrılsaydı cihaz alınabilirdi.* → *Bütçe ayrılırsa cihaz alınabilir.* (Gerçekleşmemiş geçmiş, açık bir olanağa dönüştü.)
- **Kayma (istisnanın kapsamı):** *Ziyaretçiler, refakatçi eşliğinde girmedikçe üretim alanına alınmaz; bakım ekibi hariçtir.* → *Bakım ekibi ve refakatli ziyaretçiler hariç kimse üretim alanına alınmaz.* (Yalnızca ziyaretçilere yönelik yasak, bütün çalışanları kapsayan bir yasağa dönüştü.)
- **Güvenli:** Koşul sözünü ("ancak, yalnızca ... ise, -madıkça, sürece, takdirde, hariç, dışında") kaynakta bağlı olduğu yükümlülüğün yanında tut.
- **Bak:** Hukuki ve kurumsal metinde her koşul ve istisna için şunu yaz: kime, hangi yükümlülüğe, hangi durumda. Yeni metinde aynısı mı?

### ANL-18 · Mantıksal bağ ve soru

"ve" iki şartın birlikte gerektiğini, "veya / ya da" birinin yettiğini söyler. "ve/veya" ikisini de kapsar. Soru bir iddia değildir.

- **Kayma:** *İlaç sabah ve akşam alınmalıdır.* → *İlaç sabah veya akşam alınmalıdır.*
- **Kayma:** *Raporlar PDF veya CSV biçiminde indirilebilir.* → *Raporlar PDF ve CSV biçiminde indirilmelidir.*
- **Kayma:** *Ahmet raporu imzaladı mı?* → *Ahmet raporu imzaladı.*
- **Bak:** "ve, veya, ya da, ve/veya, ne ... ne, hem ... hem" ve soru eklerinin sayısı ve bağlandığı öğeler aynı mı?

### ANL-19 · Roller: hâl ekleri, çatı, -lı/-sız

Türkçede kimin kime ne yaptığını ekler söyler. Tek bir ek değişince eylemi yapan, etkilenen ya da nitelik tersine dönebilir.

- **Kayma (rol):** *Doktorun aradığı çalışan geldi.* → *Doktoru arayan çalışan geldi.*
- **Kayma (ettirgen):** *Görevli kontrolleri yaptırdı.* → *Görevli kontrolleri yaptı.* (Sağlayan ile yapan karıştı.)
- **Kayma (karşılıklılık):** *Hekim yöneticiyle görüştü.* → *Hekim yöneticiyi görüştürdü.*
- **Kayma (belirtililik):** *Çalışan rapor hazırladı.* → *Çalışan raporu hazırladı.* (herhangi bir rapor → bilinen bir rapor)
- **Kayma (-lı/-sız):** *Kayıtlı çalışanlar sahaya girebilir.* → *Kayıtsız çalışanlar sahaya girebilir.*
- **Bak:** Edilgen-etken dönüşümünde, ilgi cümlesinde ve hâl eki değişen her öğede kim, kime, neyi sorularının cevabı aynı mı?

### ANL-20 · Niceleyicinin dağılımı

"her, -er/-şer, başına" bir dağılım bildirir. Dağılım toplama ya da ortak tek bir öğeye dönüşmez.

- **Kayma:** *Her çalışan bir hekimle görüştü.* → *Bütün çalışanlar aynı hekimle görüştü.*
- **Kayma:** *Her çalışana ikişer kart verildi.* → *Çalışanlara iki kart verildi.*
- **Kayma:** *Her vardiyada en az bir hekim bulunur.* → *Vardiyalarda en az bir hekim bulunur.* (Vardiya başına yükümlülük, toplamda bir hekime indi.)
- **Güvenli:** Dağılımı aynı sözle koru: *her biri, kişi başına, vardiya başına, ikişer.* "Bir" her zaman gereksiz bir tanımlık değildir. Belirsiz bir kişiyi kaynakta olmayan ortak bir kişiye dönüştürme.

### ANL-21 · Yazarın sesi ve söz sanatları

Deneme, köşe yazısı ve kişisel metinde bazı "kalıplar" yazarın bilinçli seçimidir. Bunları yapay zeka izi sanıp düzeltmek metnin söylediğini değiştirir.

- **Kayma (retorik soru):** *Kim yadsıyabilir ki bunu?* → *Bunu kimse yadsıyamaz.* (Yazar sormuyor ama okuru düşünmeye çağırıyor. Bildirim o çağrıyı siler.)
- **Kayma (ironi):** *Ne güzel. Ne verimli. Toplantı yine iki saat sürdü.* → *Toplantı verimli geçti ve iki saat sürdü.*
- **Kayma (bilinçli tekrar):** *Takvimim doldu. Günüm doldu. Sabrım doldu.* → *Takvimim, günüm ve sabrım doldu.*
- **Güvenli:** Metnin çoğu insan elinden çıkmışsa yalnızca açık yapay zeka izi taşıyan cümlelere dokun. Soru işaretlerinin sayısı, ironik pastişler ve tekrar dizileri yerinde kalır.
- **Yapay zekâ taslağı:** Hazır imge ve abartı yazar sesi değildir (SKILL.md, "Yapay zekâ taslağı"). Sadeleştirirken iddianın gücünü koru: *Tarihin en yalnız döneminden geçiyoruz.* → *Hiç bu kadar yalnız olmamıştık.* (güvenli); → *Biraz yalnızlaştık.* (kayma: üstünlük iddiası zayıfladı).
- **Bak:** Kaynaktaki her soru hâlâ soru mu? Bir sözü ironik kullanılan bir cümle hâlâ ironik mi?

### ANL-22 · Görüşün sahibi ve hukuki statüsü

Hukuk ve akademik metinde bir önermenin kime ait olduğu, önermenin kendisi kadar önemlidir. Şunlar ayrı statülerdir:
- yürürlükteki hukuk: *Kanun ... öngörür.*
- yargı kararı: *Yargıtay ... kabul etmiştir.*
- öğreti: *Öğretide ... savunulmaktadır.*
- yazarın görüşü: *Kanaatimizce ...*

- **Kayma:** *Kanaatimizce gebelik nidasyonla başlar.* → *Gebelik nidasyonla başlar.* (Yazarın görüşü, yerleşik hukuk gibi sunuldu.)
- **Kayma:** *Öğretide bu görüş savunulmaktadır.* → *Bu görüş genel kabul görmektedir.* (Bir görüş, genel kabule dönüştü.)
- **Kayma:** *Başsavcılık istemde bu görüşü ileri sürmüş, Daire benimsememiştir.* → *Yargıtay bu görüşü ileri sürmüştür.* (İstem, Dairenin kabulüne dönüştü.)
- **Kayma (karar türü):** *Daire kanun yararına bozma kararı vermiştir.* → *Daire kararı bozmuştur.*
- **Kayma (tek karar):** *12. CD bir kararında bunu kabul etmiştir.* → *Yargıtay bunu kabul etmektedir.* (Tek karar, yerleşik içtihada dönüştü.)
- **Kayma (tarama sınırı):** *Bu çalışmada incelenen kararlar arasında buna rastlanmamıştır.* → *Yargıtay bu konuda karar vermemiştir.*
- **Güvenli:** Görüş işaretlerini koru. Sık tekrar eden "kanaatimizce"yi "kanımızca" ya da "bize göre" ile çeşitlendirmek serbesttir. Silmek ya da bir öğreti cümlesine gömmek serbest değildir. "Ağırlıklı görüş", "genel kabul", "incelenen eserlerin çoğu" gibi nicel öğreti ifadeleri aynen kalır.
- **Bak:** Her cümlede iddianın sahibi (kanun, mahkeme, Başsavcılık, öğreti, yazar) ve karar türü kaynaktakiyle aynı mı?

### ANL-23 · Olan hukuk ile olması gereken hukuk

*De lege lata* (yürürlükteki hukuk) ile *de lege ferenda* (önerilen düzenleme) ayrı şeylerdir. Yürürlük durumu da (yürürlükte, değişik, mülga, tasarı) önermenin parçasıdır.

- **Kayma:** *Sürenin hesabı kanunda düzenlenmelidir.* → *Sürenin hesabı kanunda düzenlenir.* (öneri → yürürlükteki hukuk)
- **Kayma (ters yön):** *Kanun on haftayı esas alır.* → *Kanun on haftayı esas almalıdır.*
- **Kayma (zaman):** *765 sayılı Kanun bu fiili ayrıca cezalandırıyordu.* → *Kanun bu fiili ayrıca cezalandırır.* (Mülga hüküm, yürürlükteymiş gibi yazıldı.)
- **Kayma:** *Teklifte süre on iki hafta olarak önerilmişti.* → *Süre on iki haftadır.*
- **Güvenli:** Yürürlükteki hükmü geniş zamanla, değişen kısmı geçmiş zamanla, öneriyi "-malı/-meli, önerilir" ile yaz. Kaynaktaki dağılımı aynen koru.
- **Bak:** "-malı, -meli, gerekir, önerilir" sözleri ve hükümlerin yürürlük durumu kaynaktakiyle aynı mı?

---

## Kaynaklar

Erişim tarihi 5 Kasım 2026. Bu dosyadaki kuralların çoğu Aynen'in anlam koruma ilkesidir; dil bilgisi dayanakları öteki başvuru dosyalarının Kaynaklar bölümlerindedir.

- **[RYY]** T.C. Cumhurbaşkanlığı. *Resmî Yazışmalarda Uygulanacak Usul ve Esaslar Hakkında Yönetmelik* (Cumhurbaşkanı Kararı 2646, Resmî Gazete 10.06.2020, sayı 31151), md. 16/12 (metnin son bölümü). https://mevzuat.gov.tr/MevzuatMetin/21.5.2646.pdf
