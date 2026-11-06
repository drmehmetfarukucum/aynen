# Yazım ve noktalama

Bu dosya, metni düzeltirken denetlenecek yazım ve noktalama kurallarını toplar. Kurallar TDK'nın çevrim içi yazım kuralları sayfalarına ve Güncel Türkçe Sözlük'e dayanır. Bir yazım düzeltmesi anlamı değiştirebiliyorsa `anlam-kaymasi.md` kazanır.

## Okuma anahtarı

- **Etiket:** `[TDK-NOK Virgül 10]` şu demektir: TDK'nın "Noktalama İşaretleri (Açıklamalar)" sayfası, Virgül bölümü, 10. madde. Etiketlerin bağlantıları en sondaki Kaynaklar bölümündedir.
- **Yanlış → Doğru:** Anlamı koruyan düzeltme. Her çift `scripts/anlam_denetimi.py` ile sınandı ve KESİN sonuç vermedi.
- **Doğru + betik uyarısı:** Anlamı koruyan ama betiğin uyarı verebileceği düzeltme: özel adın kesmesi, kısaltma noktası, alıntıdaki tırnak, yüzde işaretinin boşluğu. Betik bu değişikliği KONTROL olarak bildirebilir; kaynakla karşılaştırıp onayla.
- **Kayma:** Yazımın ya da noktalamanın anlamı bilerek değiştirdiği örnek. Bunlar uygulanmaz, tanınır.
- **[Aynen tercihi]:** TDK'nın değil, bu skill'in uygulama kararı.
- **[kaynak doğrulanamadı]:** Okunan TDK sayfalarında karşılığı bulunamayan kural.

## Dizin

1. Önce bunlara bak (YN-01–YN-08)
2. Noktalama (YN-09–YN-55)
3. Büyük harfler (YN-56–YN-67)
4. Sayılar (YN-68–YN-79)
5. Kısaltmalar (YN-80–YN-86)
6. Birleşik sözcükler (YN-87–YN-96)
7. de/da, ki, mi, ile, ek-fiil ve bağlaçlar (YN-97–YN-104)
8. Düzeltme işareti (YN-105–YN-108)
9. Yabancı sözcükler ve ekleri (YN-109–YN-113)
10. Sık yapılan yazım yanlışları
11. Yapay zekâ izleri: İngilizce tipografinin Türkçeye taşınması (YZ-01–YZ-09)
12. Anlam riski: Noktalamanın anlamı değiştirdiği yerler (YA-01–YA-10)

---

## 1. Önce bunlara bak

- **YN-01 · Anlam önce.** Bir yazım ya da noktalama düzeltmesi anlamı değiştirebiliyorsa yapma ya da kullanıcıya sor (Bölüm 12). Doğru yazılmış metinde değişiklik üretme.
- **YN-02 · Alıntıya dokunma.** Tırnak içindeki söz, olduğu gibi aktarılmış sözdür [TDK-NOK Tırnak 1]. İçindeki yazım yanlışı da alıntının parçasıdır. Betik alıntıdaki değişikliği KESİN sayar.
- **YN-03 · Biçimli içeriğe dokunma.** Kod, bağlantı, e-posta adresi, dosya yolu, formül, tablo verisi ve kaynakça girdisi düzeltilmez. Bunlarda nokta, virgül ve tırnak sözdiziminin parçasıdır. Sosyal medya etiketleri (#IsGuvenligi) ve kullanıcı adları (@ad) platformun işlevsel parçasıdır; yazımını TDK'ye uydurma, sayısını azaltma. Metin içi kaynak gösterimi (*Arıkan vd., 2024*; *Yılmaz ve ark.*), dipnot işareti ve sayfa numarası olduğu gibi kalır. [Aynen tercihi] Resmî yazının Sayı, Konu, İlgi, Ek ve Dağıtım bölümlerinin biçimi yönetmelikle belirlenir [RYY md. 11, 13, 15, 18, 19]; bunları düzyazı gibi düzeltme.
- **YN-04 · Adın kendi yazımı.** Latin harfli dillerdeki özel adlar özgün biçimleriyle yazılır [TDK-YOA 1]. Kanunda bitişik geçen ya da bitişik tescil edilmiş kuruluş adları bitişik yazılır [TDK-BIT 21]. Kurala uymuyor gibi görünen biçim adın kendisi olabilir. Değiştirme.
- **YN-05 · Değeri kesin olmayan sayı.** Bir sayının hangi ayırıcı düzeniyle yazıldığı belli değilse biçimine dokunma (YN-71, YZ-06). Kullanıcıya sor.
- **YN-06 · Sayısal tarih.** *03/04/2026* hem 3 Nisan hem 4 Mart olabilir. Sayısal tarihin sırasını ve ayırıcısını değiştirme, ay adına çevirme (YA-09).
- **YN-07 · Niteleyici sayının yanında kalır.** "yaklaşık, en az, en fazla, -den fazla, -e yakın" gibi sözler bağlı oldukları sayıdan ayrılmaz (ANL-01, ANL-03).
- **YN-08 · Tutarlı tercih.** TDK sayfaları bir konuda kural koymuyorsa metnin tutarlı tercihini koru. Düz ya da kıvrık tırnak, kesme işaretinin biçimi, liste maddelerinin sonuna nokta konup konmaması ve sayı ile derece simgesi arasındaki boşluk bunlardandır (TDK'nin örneği boşlukludur: *-2 °C* [TDK-NOK Kısa Çizgi 9]). [Aynen tercihi]

---

## 2. Noktalama

- **YN-09 · Boşluk.** Nokta, virgül, noktalı virgül, iki nokta, üç nokta, soru, ünlem, tırnak, ayraç ve kesme önceki sözcüğe bitişik yazılır. Kesme dışındaki işaretlerden sonra bir boşluk bırakılır [TDK-NOK giriş].
  - Yanlış → Doğru: *Ekip hazır , eğitim yarın başlıyor .* → *Ekip hazır, eğitim yarın başlıyor.*

### Nokta

- **YN-10** Cümlenin sonuna konur [TDK-NOK Nokta 1]. Resim, çizelge ve tablo açıklaması cümle değilse sonuna nokta konmaz [TDK-BH F].
- **YN-11** Sıra bildiren rakamdan sonra konur: *3. kat, XXI. yüzyıl* [TDK-NOK Nokta 3]. Art arda sıralanan rakamlarda yalnızca sonuncudan sonra konur [TDK-NOK Nokta 4].
  - Yanlış → Doğru: *2., 4. ve 7. maddeler değişti.* → *2, 4 ve 7. maddeler değişti.*
- **YN-12** Tarihte gün, ay ve yılı; saatte saat ile dakikayı ayırır: *5.11.2026, 14.30* [TDK-NOK Nokta 6, 7]. Ay adı yazıyla yazılırsa ay adının önüne ve ardına nokta konmaz: *5 Kasım 2026* [TDK-NOK Nokta 6 UYARI].
- **YN-13** Dört ve daha çok basamaklı sayılarda sondan üçlü grupları ayırır: *4.250* [TDK-NOK Nokta 9]. Ayrıntı YN-71.
- **YN-14** Bazı kısaltmaların sonuna konur: *Dr., Prof., vb.* [TDK-NOK Nokta 2]. Ayrıntı YN-82.

### Virgül

- **YN-15** Eş görevli sözcükleri ve sıralı cümleleri ayırır [TDK-NOK Virgül 1, 2].
- **YN-16** Uzun cümlede yüklemden uzak düşen özneyi belirtir [TDK-NOK Virgül 3].
- **YN-17** Ara söz ve ara cümlenin başına ve sonuna konur [TDK-NOK Virgül 4].
- **YN-18** Hitaptan sonra konur. Sonraki cümleye bağlı "evet, hayır, peki, tamam, olur, elbette" gibi sözlerden sonra da konur [TDK-NOK Virgül 9, 11].
- **YN-19** Bir sözcüğün sonrakiyle bağı olmadığını göstermek ve anlam karışıklığını önlemek için konur. Özne olan "bu, şu, o" zamirlerinden sonra konur [TDK-NOK Virgül 10, 14]. Bu virgül anlam taşır (YA-01).
- **YN-20** Tırnak içine alınmamış aktarma cümlesinden sonra konur: *Yarın gelirim, dedi.* [TDK-NOK Virgül 6]
- **YN-21** Sayıda kesri ayırır: *2,5* [TDK-NOK Virgül 12].
- **YN-22** Art arda gelen zarf-fiillerden sonra konur. Tek zarf-fiilden sonra konmaz [TDK-NOK Virgül 13 ve UYARI].
- **YN-23 · Virgülün konmadığı yerler** [TDK-NOK Virgül UYARI'ları]:
  - "ve, veya, yahut, ya ... ya" bağlaçlarının önü ve ardı
  - tekrarlı bağlaçlar: hem ... hem, ne ... ne, gerek ... gerek, ister ... ister
  - pekiştirme ve bağlama görevindeki "da/de"nin ardı
  - "-ınca" anlamıyla zarf-fiil görevindeki "mı/mi"nin ardı
  - şart ekinin ardı
  - Yanlış → Doğru: *Rapor hazır, ve yarın gönderilecek.* → *Rapor hazır ve yarın gönderilecek.*
  - Yanlış → Doğru: *Hem bakım ekibi, hem kalite ekibi katılacak.* → *Hem bakım ekibi hem kalite ekibi katılacak.*
  - Yanlış → Doğru: *Onay gelirse, süreç başlar.* → *Onay gelirse süreç başlar.*

### Noktalı virgül

- **YN-24** Cümle içinde virgüllerle ayrılmış tür ya da takımları birbirinden ayırır [TDK-NOK Noktalı Virgül 1]. Gruplama bilgisi taşır (YA-03).
- **YN-25** Ögeleri arasında virgül bulunan sıralı cümleleri ayırır [TDK-NOK Noktalı Virgül 2]. İkiden çok eş değer ögesinde virgül bulunan cümlede özneden sonra da konabilir [TDK-NOK Noktalı Virgül 3]. Bu kullanım isteğe bağlıdır. Varsa koru.
- **Not:** Grup ayırmayan bir noktalı virgülü noktaya çevirmek güvenlidir. Virgüle çevirmek grupları silebilir. [Aynen tercihi]

### İki nokta

- **YN-26** Örnek ya da açıklama verilecek cümlenin sonuna konur [TDK-NOK İki Nokta 1, 2]. Ardından gelen cümle büyük harfle başlar. Cümle ya da özel ad olmayan örnekler sıralanıyorsa küçük harfle başlar [TDK-BH A ve UYARI]. Ayrıntı YZ-07.
- **YN-27** Karşılıklı konuşmada konuşanı belirten sözden sonra konur [TDK-NOK İki Nokta 4]. Saat ile dakika iki noktayla değil noktayla ayrılır (YN-12, YZ-09).

### Üç nokta

- **YN-28** Tamamlanmamış cümlenin sonuna, açık yazılmak istenmeyen sözün yerine, alıntıda alınmayan bölümün yerine ve sözü okura bırakmak için konur [TDK-NOK Üç Nokta 1–4]. Alıntıda atlanan bölümü gösteren üç nokta ayraç içine alınabilir: *(…)* [TDK-NOK Yay Ayraç 5].
- **YN-29** Üç nokta yerine iki ya da daha çok nokta kullanılmaz. Soru ve ünlem işaretinden sonra iki nokta yeterlidir: *?.. !..* [TDK-NOK Üç Nokta UYARI'ları].
  - Yanlış → Doğru: *Sonuçlar hâlâ gelmedi....* → *Sonuçlar hâlâ gelmedi…*

### Soru işareti

- **YN-30** Soru eki ya da soru sözü taşıyan cümlenin sonuna konur. Soru eki taşımadığı hâlde soru soran cümlenin sonuna da konur: *Teslim tarihi?* [TDK-NOK Soru 1, 2]. Bu işaret silinirse soru bildirime döner (YA-04).
- **YN-31** Bilinmeyen ya da kuşkulu bilgi için ayraç içinde kullanılır: *1987 (?)* [TDK-NOK Soru 3; Yay Ayraç 7]. Silinirse kuşku kalkar (YA-04).
- **YN-32** "mı/mi" ile kurulan yan cümle, temel cümlenin zarf tümleciyse sona soru işareti konmaz. Sıralı soru cümlelerinde işaret en sona konur [TDK-NOK Soru UYARI'ları].
  - Yanlış → Doğru: *Alarm çaldı mı binayı boşaltıyoruz?* → *Alarm çaldı mı binayı boşaltıyoruz.*
  - Yanlış → Doğru: *Rapor bu hafta mı? Gelecek hafta mı?* → *Rapor bu hafta mı, gelecek hafta mı?*

### Ünlem

- **YN-33** Sevinç, acı, korku, şaşma gibi duyguları anlatan cümlenin sonuna konur. Seslenme, hitap ve uyarı sözlerinden sonra da konur [TDK-NOK Ünlem 1, 2]. Ayrıntı YZ-08.
- **YN-34** Alay, kinaye ya da küçümseme katmak için sözden hemen sonra ayraç içinde kullanılır: *(!)* [TDK-NOK Ünlem 3; Yay Ayraç 6]. Dokunma (YA-05).

### Kısa çizgi ( - )

- **YN-35** Satır sonunda bölünen sözcükte kullanılır. Kök, gövde, ek ve heceleri göstermede de kullanılır [TDK-NOK Kısa Çizgi 1, 3–6].
- **YN-36** "arası, ve, ile, ila, -den ... -e" anlamı verir: *İzmir-Ankara seferi, 2024-2026 dönemi, 09.00-17.00* [TDK-NOK Kısa Çizgi 7]. Cümle içinde yinelenen sayı adlarının arasına konmaz: *üç beş kişi* [TDK-NOK Kısa Çizgi UYARI].
- **YN-37** Ara söz iki kısa çizgi arasına alınabilir. Çizgi ara söze bitişik yazılır: *Ekip -iki kişi eksik olsa da- sahaya çıktı.* [TDK-NOK Kısa Çizgi 2]. İki çizgi arasındaki açıklama cümlesi küçük harfle başlar [TDK-BH A UYARI].
- **YN-38** Matematikte eksiyi ve sıfırın altındaki değerleri gösterir: *-4 °C* [TDK-NOK Kısa Çizgi 8, 9]. Bu çizgi sayının parçasıdır. Silinirse değer değişir (YA-10).

### Uzun çizgi ( — )

- **YN-39** TDK'ya göre uzun çizgi, satır başına alınan konuşmaları gösterir. Buna konuşma çizgisi denir. Oyunlarda konuşanın adından sonra da konabilir. Konuşma tırnak içinde verilmişse kullanılmaz [TDK-NOK Uzun Çizgi]. Cümle içindeki ara söz için TDK sayfası uzun çizgiyi değil virgülü, kısa çizgiyi ya da ayracı gösterir (YN-17, YN-37, YN-43). Ayrıntı YZ-01.

### Tırnak ve tek tırnak

- **YN-40** Başkasından ya da bir yazıdan olduğu gibi aktarılan söz tırnak içine alınır. Alıntının sonundaki nokta, soru ya da ünlem tırnağın içinde kalır [TDK-NOK Tırnak 1 ve UYARI].
  - Yanlış → Doğru: *Ece “Toplantı yarın mı”? diye sordu.* → *Ece “Toplantı yarın mı?” diye sordu.*
- **YN-41** Özel olarak vurgulanan söz tırnak içine alınır [TDK-NOK Tırnak 2]. Eser, yazı ve bölüm adları cümle içinde tırnakla ya da eğik yazıyla gösterilir [TDK-NOK Tırnak 3 ve UYARI]. Künyede makale adı tırnak içinde yazılır [TDK-NOK Tırnak 4].
- **YN-42** Tırnak içindeki söze gelen ek kesmeyle ayrılmaz [TDK-NOK Tırnak UYARI]. Tırnak içinde yeniden tırnak gerekiyorsa tek tırnak kullanılır [TDK-NOK Tek Tırnak].
  - Yanlış → Doğru: *“Güvenli Vardiya”'yı okudunuz mu?* → *“Güvenli Vardiya”yı okudunuz mu?*

### Ayraç ve köşeli ayraç

- **YN-43** Cümlenin anlamını tamamlayan ama cümlenin dışında kalan ek bilgi ayraç içine alınır. Ayraç içindeki söz yargı bildiriyorsa büyük harfle başlar ve sonuna uygun işaret konur [TDK-NOK Yay Ayraç 1; TDK-BH A].
- **YN-44** Özel ada gelen ek ayraçtan önce yazılır [TDK-NOK Yay Ayraç 2; TDK-KES 1].
  - Yanlış → Doğru: *Selin (ekip lideri)'nin önerisi kabul edildi.* → *Selin'in (ekip lideri) önerisi kabul edildi.*
- **YN-45** Madde gösteren rakam ve harflerden sonra kapama ayracı konabilir: *1) a)* [TDK-NOK Yay Ayraç 8].
- **YN-46** Ayraç içinde ayraç gerekiyorsa dıştaki köşeli ayraç olur. Alıntıya aktaranın eklediği sözler köşeli ayraç içine alınır [TDK-NOK Köşeli Ayraç 1, 2]. Köşeli ayraç kalkarsa aktaranın sözü alıntının sahibine mal edilir (ANL-22).

### Kesme işareti

- **YN-47** Özel adlara gelen iyelik, hâl ve bildirme ekleri kesmeyle ayrılır: *Kocaeli'de, Selin'in, Ankara'dır* [TDK-KES 1].
- **YN-48** Kurum, kuruluş, kurul ve iş yeri adlarına gelen ekler kesmeyle ayrılmaz [TDK-KES UYARI].
  - Doğru: *Dilekçe Mavikaya Hastanesine gönderildi.* (*Hastanesi'ne* değil.) Betik bu değişikliği KONTROL olarak bildirebilir; kaynakla karşılaştırıp onayla.
  - Belli bir kanun ya da yönetmelik kastedilip büyük harfle yazılan "Kanun, Yönetmelik" ek alınca kesme alır: *Yönetmelik'in 4'üncü maddesi* [TDK-KES 1].
  - Ek alan söz bir kurum adı mı, yoksa bir ürün, marka ya da kişi adı mı, belli değilse kesmeye dokunma; metnin tutarlı tercihini koru ve gerekirse kullanıcıya sor. TDK sayfası marka adları için ayrı bir örnek vermez [kaynak doğrulanamadı]. Adın kendisi değişmez (YN-04); kesme adın değil ekin yazımıdır.
- **YN-49** Özel ada gelen yapım ekleri ve çokluk eki ile bunlardan sonra gelen ekler kesmeyle ayrılmaz [TDK-KES UYARI].
  - Doğru: *Formun Türkçesi hazır.* (*Türkçe'si* değil.) Betik bu değişikliği KONTROL olarak bildirebilir; kaynakla karşılaştırıp onayla.
- **YN-50** Kişi adından sonra gelen saygı ve ünvan sözlerine gelen ek kesmeyle ayrılır: *Deniz Bey'e, Ece Hanım'dan* [TDK-KES 2].
- **YN-51** Kısaltmalara ve sayılara gelen ekler kesmeyle ayrılır: *KDV'ye, 2026'da, 3'üncü, %40'ı* [TDK-KES 3, 4]. Ek, sayının okunuşuna uyar; okunuş sert ünsüzle bitiyorsa ek de sertleşir: TDK örneği *1985'te* (bin dokuz yüz seksen beşte) [TDK-KES 4]. Noktayla biten kısaltmaya kesme konmaz (YN-84).
  - Yanlış → Doğru: *Sözleşme 2023'de imzalandı.* → *Sözleşme 2023'te imzalandı.*
- **YN-52** Belirli bir tarih bildiren ay ve gün adlarına gelen ekler kesmeyle ayrılır: *20 Kasım'a kadar* [TDK-KES 5].
- **YN-53** Bağlaç olan "da/de" kesmeyle ayrılmaz [TDK-DE UYARI]. Özel ad yerine kullanılan "o" zamiri küçük harfle ve kesmesiz yazılır [TDK-KES UYARI].
- **Not:** TDK'nın kesme sayfası ’ biçimini gösterir. Klavyedeki düz ' da yaygındır. Metin tutarlıysa biçime dokunma (YN-08).

### Eğik çizgi

- **YN-54** Adreste daire numarasını kapı numarasından, semti şehirden ayırır. Tarihte gün, ay ve yılı ayırabilir. Dil bilgisinde eklerin biçimlerini gösterir: *-a/-e* [TDK-NOK Eğik Çizgi 2–4]. Yan yana yazılan dizeleri ayırır [TDK-NOK Eğik Çizgi 1].
- **YN-55** Matematikte bölmeyi gösterir. Birimler arası oranda araya boşluk konmadan yazılır: *km/sa* [TDK-NOK Eğik Çizgi 6, 7]. "ve/veya" bir mantık bağıdır. Eğik çizgiyi atlamak ya da bağlardan birini silmek anlamı değiştirir (YA-10, ANL-18).

---

## 3. Büyük harfler

- **YN-56 · Cümle başı.** Cümle büyük harfle başlar. Cümle içinde tırnak ya da ayraç içine alınan cümle de büyük harfle başlar ve sonuna uygun işaret konur [TDK-BH A].
- **YN-57 · İki noktadan sonra.** Cümle gelirse büyük harfle başlar. Cümle ya da özel ad olmayan örnekler sıralanıyorsa küçük harfle başlar [TDK-BH A ve UYARI]. Ayrıntı YZ-07.
- **YN-58 · Rakamla başlayan cümle.** Rakamdan sonraki sözcük özel ad değilse küçük harfle başlar [TDK-BH A UYARI]. Bir zorunluluk yoksa cümle rakamla başlamaz [TDK-SAY 12]. Bunu düzeltmek cümleyi yeniden kurmayı gerektiriyorsa ve kullanıcı tam TDK uyumu istemediyse dokunma. [Aynen tercihi]
- **YN-59 · Kişi adları ve ünvanlar.** Kişi adları, soyadları ve takma adlar büyük harfle başlar [TDK-BH C1]. Kişi adından önce ya da sonra gelen ünvan, saygı sözü ve rütbe büyük harfle başlar: *Dr. Selin Arıkan, Deniz Bey* [TDK-BH C2]. Akrabalık sözleri küçük harfle başlar: *Ece teyze* [TDK-BH C2 UYARI].
- **YN-60 · Makam ve hitap.** Cümle içinde özel adın yerine kullanılan makam ya da ünvan sözü büyük harfle başlar [TDK-BH C3]. Saygı sözünden sonra gelen makam sözü ve mektupla resmî yazışmadaki hitaplar büyük harfle başlar: *Sayın Müdür,* [TDK-BH C4].
- **YN-61 · Millet, dil, devlet, din.** Bu adlar ve özel addan türeyen bütün sözcükler büyük harfle başlar: *Türkçe, Japonca, Sivaslı* [TDK-BH C6–C9, C25]. Kendi anlamı dışında yeni bir anlam kazanmış özel ad küçük harfle başlar. Para birimleri küçük harfle başlar: *lira, dolar, avro* [TDK-BH C25 UYARI'ları].
- **YN-62 · Yer adları.** Yer adları büyük harfle başlar. Tür bildiren ikinci ad özel adın parçasıysa o da büyük harfle başlar: *Eğirdir Gölü*. Özel ada dâhil olmayan "il, ilçe, köy" gibi sözler küçük harfle başlar: *Bolu ili* [TDK-BH C13, C14]. Mahalle, meydan, bulvar, cadde ve sokak sözleri adın içinde büyük harfle başlar [TDK-BH C15]. Yapı adlarının bütün sözcükleri büyük harfle başlar [TDK-BH C16].
- **YN-63 · doğu, batı, dünya, güneş, ay.** "doğu, batı" düşünce, yaşam biçimi ya da siyaset bildirince büyük, yön bildirince küçük harfle başlar [TDK-BH C12 ve UYARI]. "dünya, güneş, ay" gezegen anlamı dışında küçük harfle başlar [TDK-BH C11 UYARI].
- **YN-64 · Kurum ve mevzuat.** Kurum, kuruluş ve kurul adlarının her sözcüğü büyük harfle başlar [TDK-BH C18]. Kanun, tüzük, yönetmelik, yönerge ve genelge adlarının her sözcüğü büyük harfle başlar [TDK-BH C19]. "kurum, kurul, bakanlık, üniversite, kanun, yönetmelik" gibi sözler, asılları kastedildiğinde tek başına da büyük harfle başlar: *Kurul kararını açıkladı.* [TDK-BH C20]. Bu büyük harf bir göndergedir (YA-08).
- **YN-65 · Eser adları.** Kitap, dergi, gazete ve sanat eserlerinin adlarındaki her sözcük büyük harfle başlar. Özel ada dâhil olmayan "gazete, dergi" sözleri küçük harfle başlar [TDK-BH C21 ve UYARI]. Her sözcüğü büyük yazılan eser, kurum ve kuruluş adlarında "ve, ile, ya, veya, yahut, ki, da, de" ve "mı/mi" küçük yazılır [TDK-BH C21 UYARI].
- **YN-66 · Gün ve dönem adları.** Bayram ve anma günü adları, kurultay ve çalıştay gibi toplantıların adları, tarihî olay, çağ ve dönem adları büyük harfle başlar [TDK-BH C22–C24]. Ay ve gün adları belirli bir tarih bildiriyorsa büyük, bildirmiyorsa küçük harfle başlar [TDK-BH Ç].
  - Yanlış → Doğru: *Eğitimler genellikle Eylül ayında başlar.* → *Eğitimler genellikle eylül ayında başlar.*
  - Yanlış → Doğru: *Son başvuru 20 kasım.* → *Son başvuru 20 Kasım.*
- **YN-67 · Başlık, açıklama, levha.** Kitap, bildiri ve makalede ana başlığın bütün harfleri büyük yazılır. Alt başlıkta sözcüklerin ilk harfleri büyük yazılır [TDK-BH E]. Resim, çizelge ve tablo açıklamaları büyük harfle başlar [TDK-BH F]. Tabela ve levha yazılarındaki sözcükler büyük harfle başlar [TDK-BH D]. Başlık düzeni için YZ-03'e bak.

---

## 4. Sayılar

- **YN-68 · Rakam ya da yazı.** Sayılar yazıyla da yazılabilir. Saat, para tutarı, ölçü ve istatistik verilerinde rakam kullanılır [TDK-SAY 1]. Gerekmedikçe rakamı yazıya ya da yazıyı rakama çevirme. [Aynen tercihi]
- **YN-69 · Ayrı yazım.** Birden çok sözcükten oluşan sayılar ayrı yazılır: *iki yüz, on beş* [TDK-SAY 2]. Okumayı kolaylaştırmak için "bin, milyon, milyar" harfle yazılabilir: *3 milyon 200 bin* [TDK-SAY 1]. Senet ve çek gibi ticari belgelerde tutar bitişik yazılır [TDK-SAY 3]. Bu belgelere dokunma.
  - Yanlış → Doğru: *Ekipte onbeş kişi var.* → *Ekipte on beş kişi var.*
- **YN-70 · Ondalık ayırıcı.** Kesir virgülle ayrılır: *2,5* [TDK-SAY 8].
- **YN-71 · Binlik ayırıcı.** Dört ve daha çok basamaklı sayılar sondan üçlü gruplara ayrılır, araya nokta konur: *4.250, 1.250.000* [TDK-SAY 7].
  - TDK örneklerinde yıllar (*1985*), kanun sayıları (*2876 sayılı*) ve posta kodları (*06680*) noktasız yazılır [TDK-KES 4; TDK-BH C20; TDK-NOK Eğik Çizgi 2]. Bunlara nokta ekleme.
  - Bölüm ve madde numarası (*3.2. Bulgular*), sürüm numarası, saat (*14.30*), tarih ve kod ondalık sayı değildir. Ayırıcılarına dokunma.
  - Ayırıcı düzeni belli değilse dokunma (YN-05, YZ-06, YA-07).
- **YN-72 · Yüzde ve binde.** İşaret sayının önüne, boşluk bırakılmadan yazılır: *%25, ‰5* [TDK-SAY 4]. Ek, kesmeyle ve sayının okunuşuna göre gelir: *%25'i, %40'ı* [TDK-KES 4]. Ayrıntı YZ-05.
- **YN-73 · Sıra sayısı.** Rakamla yazılırken ya rakamdan sonra nokta ya da kesme ve ek gelir. İkisi birlikte kullanılmaz [TDK-SAY 9 ve UYARI]. Ek, sayının okunuşuna göre gelir: *1'inci, 2'nci, 6'ncı, 9'uncu, 10'uncu*.
  - Yanlış → Doğru: *Toplantı 3.'üncü katta.* → *Toplantı 3'üncü katta.*
- **YN-74 · Üleştirme sayısı.** Rakamla değil yazıyla yazılır: *ikişer* (2'şer değil) [TDK-SAY 10]. Dağılım bilgisi bu ektedir (ANL-20).
  - Yanlış → Doğru: *Her çalışana 2'şer maske verildi.* → *Her çalışana ikişer maske verildi.*
- **YN-75 · Bayağı kesir.** Ek, alttaki sayının okunuşuna göre gelir: *3/4'ü* (üç bölü dördü) [TDK-SAY 11].
- **YN-76 · Romen rakamı.** Tarihî olaylarda, yüzyıllarda, hükümdar adlarında, cilt numaralarında ve madde sıralamada kullanılır [TDK-SAY 6].
- **YN-77 · Tarih.** Gün, ay ve yıl nokta ya da eğik çizgiyle ayrılır. Ay adı yazıyla da yazılabilir [TDK-NOK Nokta 6 ve UYARI; Eğik Çizgi 3]. Sayısal tarihin biçimine dokunma (YN-06).
- **YN-78 · Saat.** Saat ile dakika nokta ile ayrılır: *14.30* [TDK-NOK Nokta 7]. Saat metin içinde yazıyla da yazılabilir [TDK-SAY 1]. Ek kesmeyle gelir: *14.30'da*.
- **YN-79 · Cümle başı.** Bir zorunluluk yoksa cümle rakamla başlamaz [TDK-SAY 12]. YN-58'deki sınır burada da geçerlidir.

---

## 5. Kısaltmalar

- **YN-80** Kuruluş, ülke, kitap, dergi ve yön adlarının kısaltması, her sözcüğün ilk harfi büyük yazılarak yapılır. Büyük harfli kısaltmalarda nokta kullanılmaz. Gelenekleşmiş *T.C.* ve *T.* bunun dışındadır [TDK-KIS 1].
  - Doğru: *KDV oranı değişmedi.* (*K.D.V.* değil.) Betik bu değişikliği KONTROL olarak bildirebilir; kaynakla karşılaştırıp onayla.
- **YN-81** Ölçü birimlerinin uluslararası kısaltmaları kullanılır: *m, cm, kg, mg, l* [TDK-KIS 2]. Element simgeleri uluslararası biçimleriyle yazılır. Metin içinde ek, simgeye değil elementin adına getirilir [TDK-SIM 1, 2].
- **YN-82** Öteki kısaltmalarda kısaltılan söz özel ad, ünvan ya da rütbeyse ilk harf büyük, cins adsa küçük yazılır: *Dr., Prof., Sok., çev., haz.* [TDK-KIS 3].
- **YN-83** Büyük harfli kısaltmaya gelen ek, son harfin okunuşuna göre gelir: *KDV'ye, İSG'nin, KKD'yi*. Sözcük gibi okunan kısaltmada ek, kısaltmanın okunuşuna göre gelir: *KOMSAD'a* (kurgusal bir ad). Küçük harfli kısaltmada ek, sözcüğün okunuşuna göre gelir: *kg'dan, cm'yi* [TDK-KIS].
  - Yanlış → Doğru: *Bu fatura KDV'ya tabi.* → *Bu fatura KDV'ye tabi.*
  - Yanlış → Doğru: *Paket 5 kg'den ağır.* → *Paket 5 kg'dan ağır.*
- **YN-84** Noktayla biten kısaltmaya ve üs işaretli birime gelen ek kesmeyle ayrılmaz. Ek noktadan ya da üs işaretinden hemen sonra, okunuşa göre yazılır: *vb.lerinden, m²ye* [TDK-KIS].
- **YN-85** Sert ünsüzle biten kısaltma ek aldığında son ses yumuşatılmaz. "birlik" sözüyle biten kısaltmalar bunun dışındadır [TDK-KIS].
- **YN-86** Kısaltmayı açma, açık yazılmış adı kısaltmaya çevirme. Kısaltma çoğu zaman bir terimdir (ANL-14). [Aynen tercihi]

---

## 6. Birleşik sözcükler

Kural birçok istisna taşır. Karar verirken önce Güncel Türkçe Sözlük'e bak [GTS].

- **YN-87 · etmek, olmak.** Birleşirken ses düşmesine, değişmesine ya da türemesine uğrayanlar bitişik yazılır: *affetmek, hissetmek, kaybolmak* [TDK-BIT 2]. Ses olayı yoksa ayrı yazılır: *fark etmek, kabul etmek, terk etmek, yok olmak* [TDK-AYR 1].
- **YN-88 · Anlam değişmesi.** Sözcüklerden ikisi ya da ikincisi anlam değiştirmişse bitişik yazılır: bitki, hayvan, renk adları gibi [TDK-BIT 3]. Anlam değişmesi yoksa ayrı yazılır: *iş birliği, iş bölümü, hafta sonu, gece yarısı* [TDK-AYR 2].
- **YN-89 · dış, iç, sıra.** Bu sözlerle kurulanlar ayrı yazılır: *yasa dışı, olağan dışı, yurt içi, hafta içi, yanı sıra* [TDK-AYR 8].
- **YN-90 · alt, üst.** Somut yer bildiriyorsa ayrı yazılır: *yer altı, deri altı* [TDK-AYR 9]. Somut yer bildirmiyorsa bitişik yazılır: *bilinçaltı, olağanüstü, akşamüstü* [TDK-BIT 9].
- **YN-91 · Başa gelen sıfatlar.** "alt, üst, ana, ön, art, arka, yan, karşı, iç, dış, orta, büyük, küçük, tek, çok, çift" gibi sözlerin başa geldiği birleşikler ayrı yazılır: *ön yargı, ön söz, alt kurul, arka plan, yan etki, karşı görüş* [TDK-AYR 10]. Sözlükte bitişik geçen istisnalar vardır: *altyapı, öngörü* [GTS].
- **YN-92 · bilim, bilgi.** Bu sözlerle kurulanlar ayrı yazılır: *dil bilimi, dil bilgisi* [TDK-AYR 2e].
- **YN-93 · Belirsizlik sözleri.** *birçok, birkaç, birtakım, herhangi, hiçbir* bitişik yazılır [TDK-BIT 14ç]. *her şey, pek çok* ayrı yazılır [GTS].
- **YN-94 · ev, hane, name, zade, -zede.** Bu sözlerle kurulanlar bitişik yazılır: *yayınevi, huzurevi, dershane, depremzede* [TDK-BIT 15–17].
- **YN-95 · Yönler ve ikilemeler.** Ara yönler bitişik yazılır: *güneydoğu* [TDK-BIT 13]. Yer adındaki yön sözleri ve "orta, iç, yakın, uzak" ayrı yazılır: *İç Anadolu* [TDK-AYR 6]. İkilemeler ayrı yazılır: *yavaş yavaş, yan yana, iç içe, bire bir* [TDK-IKL].
- **YN-96 · Anlam ayıran yazım.** Bitişik ve ayrı biçim farklı sözcükler olabilir: *yer altı* (yüzeyin altı) ile *yeraltı* (gizli ve yasa dışı) ayrıdır [GTS]. *birtakım* "bazı" demektir [GTS]. *bir takım* "bir ekip, bir set" anlamına gelir. Bitiştirmeden ya da ayırmadan önce anlamı doğrula.

---

## 7. de/da, ki, mi, ile, ek-fiil ve bağlaçlar

- **YN-97 · Bağlaç da/de.** Ayrı yazılır. Önceki sözcüğün son ünlüsüne göre "da" ya da "de" olur. Hiçbir zaman "ta/te" olmaz. Kesmeyle ayrılmaz. "ya da" ayrı yazılır [TDK-DE].
  - Yanlış → Doğru: *Kalite ekibi'de toplantıya katıldı.* → *Kalite ekibi de toplantıya katıldı.*
  - Yanlış → Doğru: *Gidip te bakmadı.* → *Gidip de bakmadı.*
  - Yanlış → Doğru: *Telefonla yada e-postayla bildirin.* → *Telefonla ya da e-postayla bildirin.*
- **YN-98 · Bulunma eki.** "-da/-de/-ta/-te" sözcüğe bitişik yazılır [TDK-BUL]. Ayrı ya da bitişik yazmak özneyi değiştirebilir (YA-02).
  - Pratik sınama: Bağlaç çıkarılınca yalnızca "de" anlamı düşer, cümlenin geri kalanı aynı kalır. Ek çıkarılınca cümle bozulur ya da anlamı değişir. [kaynak doğrulanamadı: TDK sayfalarında yok]
- **YN-99 · ki.** Bağlaç olan "ki" ayrı yazılır: *demek ki, kaldı ki, yeter ki*. Kalıplaşmış şu sözler bitişik yazılır: *belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki*. Şüphe ve pekiştirme bildiren "ki" de ayrı yazılır [TDK-KI]. TDK'nin yazım sayfası bu yedi sözü sayar; Güncel Türkçe Sözlük *illaki*'yi de bitişik bir madde olarak verir ve anlamı için *illa*'ya gönderir [GTS]. *illa ki* yazılışını *illaki* yap.
  - Yanlış → Doğru: *Demekki süre doldu.* → *Demek ki süre doldu.*
  - Yanlış → Doğru: *Oysa ki ekip hazırdı.* → *Oysaki ekip hazırdı.*
- **YN-100 · -ki eki.** Sıfat yapan "-ki" eki bitişik yazılır: *evdeki, yarınki, toplantıdaki*. [kaynak doğrulanamadı: TDK'nın çevrim içi yazım sayfalarında bu kural yok]
- **YN-101 · Soru eki.** "mı/mi/mu/mü" ayrı yazılır ve ünlü uyumuna uyar. Ardından gelen ekler soru ekine bitişir. Soru dışındaki görevlerde de ayrı yazılır. Birleşik fiilde iki sözcüğün arasına girebilir: *Kabul mü etti?* [TDK-MI]
  - Yanlış → Doğru: *Rapor hazırmı?* → *Rapor hazır mı?*
  - Yanlış → Doğru: *Toplantıya gelecekmisiniz?* → *Toplantıya gelecek misiniz?*
- **YN-102 · ile.** Ayrı ya da bitişik yazılabilir. Bitişik yazılınca ünsüzden sonra "-la/-le", ünlüden sonra "-yla/-yle" olur ve büyük ünlü uyumuna uyar [TDK-ILE]. Özel ada ve sayıya kesmeyle eklenir: *Selin'le, 5'le* [TDK-KES 1, 4].
  - Yanlış → Doğru: *Proje çevreyla uyumlu.* → *Proje çevreyle uyumlu.*
- **YN-103 · Ek-fiil.** "idi, imiş, ise" ayrı ya da bitişik yazılabilir. Bitişik yazılınca ünlü uyumuna uyar, ünlüden sonra "y" girer: *hazırdı, yorgunmuş, hastaysa*. "iken" bitişince "-ken" olur ve ünlüsü hep incedir: *çalışırken, evdeyken* [TDK-EKF].
  - Yanlış → Doğru: *Toplantıdaykan aradı.* → *Toplantıdayken aradı.*
- **YN-104 · Gelecek ve istek ekleri.** "-acak, -an, -ayım, -alım, -a" gibi eklerin önündeki ünlü, söyleyişe bakılmadan "a/e" ile yazılır: *başlayacak, gelmeyecek* [TDK-FC].
  - Yanlış → Doğru: *Eğitim yarın başlıyacak.* → *Eğitim yarın başlayacak.*
- **Bağlaç ve virgül:** "ve, veya, yahut" ile tekrarlı bağlaçların önüne ve ardına virgül konmaz (YN-23).

---

## 8. Düzeltme işareti (â, î, û)

- **YN-105 · Anlam ayırmak için.** Yazılışı aynı, anlamı ve okunuşu ayrı sözcüklerde uzun okunan ünlünün üzerine konur [TDK-DUZ 1]:
  - *hâl* (durum) / *hal* (sebze ve meyve satılan yer)
  - *hâlâ* (henüz) / *hala* (babanın kız kardeşi)
  - *âdet* (gelenek) / *adet* (sayı)
  - *âlem* (dünya) / *alem* (bayrak)
  - *kâr* (kazanç) / *kar* (yağış) [GTS]
  - *hâkim* (egemen) / *hakim* (bilge) [GTS]
- **YN-106 · İnce ünsüzden sonra.** Arapça ve Farsçadan gelen sözlerde ince "g, k" ünsüzlerinden sonra gelen "a" ve "u" üzerine konur: *kâğıt, dükkân, hikâye, rüzgâr, zekâ, mahkûm*. Kişi ve yer adlarında ince "l"den sonra da konur [TDK-DUZ 2; GTS].
- **YN-107 · Nispet eki.** Nispet ekini belirtme ve iyelik ekinden ayırmak için konur: *askerî* (askerlikle ilgili) / *askeri* (onun askeri), *resmî* / *resmi*, *dinî* / *dini* [TDK-DUZ 3]. *millî* "milletle ilgili", *milli* "mil içeren" demektir [GTS]. İşaret, Türkçe ek gelince de kalır: *millîleşmek, resmîlik* [TDK-DUZ 3].
- **YN-108 · Uygulama.** "katil" ve "kadir" sözlerinin işaretsiz yazılışı yaygınlaşmıştır [TDK-DUZ UYARI]. Anlam ayıran işaretleri (YN-105, YN-107) her düzeyde düzelt. Öbürlerinde metin tutarlı olarak işaretsiz yazıyorsa ve kullanıcı tam TDK uyumu istemediyse dokunma. [Aynen tercihi]
  - Yanlış → Doğru: *Başvurular hala bekliyor.* → *Başvurular hâlâ bekliyor.*
  - Yanlış → Doğru: *Milli bayram programı açıklandı.* → *Millî bayram programı açıklandı.*

---

## 9. Yabancı sözcükler ve ekleri

- **YN-109 · Yabancı özel adlar.** Latin harfli dillerdeki özel adlar özgün biçimleriyle yazılır. Okunuş ayraç içinde gösterilebilir [TDK-YOA 1]. Dilimize eskiden yerleşmiş bazı adlar Türkçe söylenişleriyle yazılır: *Londra, Brüksel, Münih* [TDK-YOA 2]. Ait olduğu dilde ayrı yazılan yer adı Türkçede de ayrı yazılır [TDK-YOA 4]. Yunanca ve Rusça adlar Türk harfleriyle yazılır [TDK-YOA].
- **YN-110 · Batı kökenli alıntılar.** Başta ya da içte yan yana gelen ünsüzlerin arasına ünlü konmaz: *grup, plan, program, proje, kredi, film, form* [TDK-ALN 1–3]. Bazılarında türemiş ünlü yazılır: *istasyon, istatistik, kulüp* [TDK-ALN 1]. "g" korunur: *diyalog, katalog, program*. *fotoğraf* bunun dışındadır [TDK-ALN 4].
- **YN-111 · Özgün biçimle yazılanlar.** Bazı bilim, sanat ve uzmanlık terimleri ile Latin harfli dillerden alınmış kalıp sözler özgün biçimleriyle yazılır [TDK-ALN]. Bunlar terimdir. Türkçe biçime çevirme (ANL-14).
- **YN-112 · Yabancı ada gelen ek.** Ek kesmeyle ayrılır [TDK-KES 1]. Ekin okunuşa göre geldiği bilinen bir uygulamadır. [kaynak doğrulanamadı: TDK'nın çevrim içi sayfalarında yabancı özel adlar için açık kural yok; okunuşa göre ek kuralı yalnızca kısaltmalar için yazılmış (TDK-KIS)] Emin değilsen eke dokunma.
- **YN-113 · Türkçe karşılık.** Sözlük bazı alıntı sözlerde Türkçe karşılığa gönderir: *doküman* → *belge* [GTS]. Bu bir yazım yanlışı değildir. Değiştirmek üslup kararıdır. Söz bir terimse değiştirme (ANL-14).

---

## 10. Sık yapılan yazım yanlışları

Tablodaki doğru biçimler, çekimli fiiller dışında, Güncel Türkçe Sözlük'te bu yazılışla madde başıdır. Yanlış biçimler sözlükte madde başı olarak yoktur [GTS]. Sözlük aramaları düzeltme işaretine duyarsızdır. Bu yüzden işaretli biçimleri ayrıca kural sayfasıyla doğrula (Bölüm 8).

| Yanlış | Doğru | Not |
|---|---|---|
| herşey | her şey | |
| hiç bir | hiçbir | [TDK-BIT 14ç] |
| bir çok, bir kaç | birçok, birkaç | [TDK-BIT 14ç] |
| pekçok | pek çok | |
| yanlız, yalnış | yalnız, yanlış | |
| herkez | herkes | |
| işbirliği | iş birliği | [TDK-AYR 2d] |
| önyargı, önsöz, önkoşul | ön yargı, ön söz, ön koşul | [TDK-AYR 10] |
| olağandışı, yasadışı | olağan dışı, yasa dışı | [TDK-AYR 8] |
| yurtiçi, yurtdışı | yurt içi, yurt dışı | [TDK-AYR 8] |
| haftasonu | hafta sonu | [TDK-AYR 2i] |
| ardarda, yanısıra | art arda, yanı sıra | |
| veritabanı, çevrimiçi | veri tabanı, çevrim içi | |
| geribildirim, arkaplan | geri bildirim, arka plan | |
| dilbilgisi | dil bilgisi | [TDK-AYR 2e] |
| anadili | ana dili | *ana dil* başka bir terimdir: birbirinden ayrışmış dillerin ortak kaynağı sayılan dil. |
| eşzamanlı | eş zamanlı | |
| farketmek | fark etmek | [TDK-AYR 1] |
| alt yapı, ön görü | altyapı, öngörü | Bitişik yazılan istisnalar. |
| yada | ya da | [TDK-DE] |
| oysa ki | oysaki | [TDK-KI] |
| itibariyle | itibarıyla | |
| başlıyacak, gelmiyecek | başlayacak, gelmeyecek | [TDK-FC] |
| orjinal, süpriz, egsoz | orijinal, sürpriz, egzoz | |
| laboratuar, antreman | laboratuvar, antrenman | |
| döküman, metod | doküman, metot | |
| klavuz, traş | kılavuz, tıraş | |
| malesef, entellektüel | maalesef, entelektüel | |

**İki doğru biçim, iki anlam.** Bunlar yazım yanlışı sanılır ama ayrı sözcüklerdir. Bağlama göre seç, emin değilsen dokunma [GTS]:

| Biçim | Anlam | Öbür biçim | Anlam |
|---|---|---|---|
| mütevazı | alçak gönüllü | mütevazi | birbirine paralel |
| tabii | doğal; elbette | tabi | bağımlı |
| dâhil | içinde, ile birlikte | dahil | bir işe karışma |
| yer altı | yüzeyin altı | yeraltı | gizli ve yasa dışı |
| birtakım | bazı | bir takım | bir ekip, bir set ("bir" ile "takım"ın serbest öbeği) |
| hâlâ, kâr, hâkim, millî | Bölüm 8 | hala, kar, hakim, milli | Bölüm 8 |

---

## 11. Yapay zekâ izleri: İngilizce tipografinin Türkçeye taşınması

Bu izler, İngilizce yazım ve dizgi alışkanlıklarının Türkçe metne taşınmasıdır. Bir ön baskı, İngilizce çıktı üreten on iki modelin çoğunda uzun çizginin, biçimlendirme kapatıldığında bile sürdüğünü bildiriyor [FREEBURG]. Türkçe metinlerde bu izlerin sıklığını ölçen bir çalışmaya ulaşılamadı [kaynak doğrulanamadı]. Bu yüzden her izi tek başına kanıt sayma. Yalnızca TDK kuralına aykırı olanı düzelt.

### YZ-01 · Cümle içinde uzun çizgi (—)

- **İz:** Ara söz, açıklama ya da ani dönüş için cümle içinde uzun çizgi. Bazen kısa çizgi (–) ya da boşluklu çizgi olarak yazılır.
- **TDK:** Uzun çizgi yalnızca konuşma çizgisidir [TDK-NOK Uzun Çizgi]. Ara söz virgülle [Virgül 4], kısa çizgiyle [Kısa Çizgi 2] ya da ayraçla [Yay Ayraç 1] ayrılır. Açıklama ve örnek iki noktayla verilir [İki Nokta 1, 2]. Aralık kısa çizgiyle gösterilir [Kısa Çizgi 7].
- **Yap:**
  - Ara sözü iki yandan ayıran çizgileri virgüle çevir. Virgül cümledeki başka virgüllerle karışıyorsa ayraç kullan.
  - Açıklama ya da örnek getiren tek çizgiyi iki noktaya çevir. Bunu yalnızca çizgi gerçekten açıklama getiriyorsa yap. İki nokta bir açıklama ilişkisi kurar (ANL-06).
  - Öbür tek çizgileri virgüle ya da noktaya çevir. Varsa karşıtlık bağlacını koru.
  - Aralık bildiren çizgiyi kısa çizgiye çevir: *2024-2026*.
- **Dokunma:** Kurmacada satır başındaki konuşma çizgisi. Oyun metninde konuşanın adından sonraki çizgi. Kullanıcının kendi metninde bütün belge boyunca tutarlı kullandığı ara söz çizgisi: Türk yayıncılığında da görülen bir tercih olabilir, emin değilsen sor (NOK-01). [Aynen tercihi]
- Yanlış → Doğru: *Yeni vardiya planı — ilk kez — gece ekibini de kapsıyor.* → *Yeni vardiya planı, ilk kez, gece ekibini de kapsıyor.*
- Yanlış → Doğru: *Üç birim — bakım, kalite ve depo — rapor gönderdi.* → *Üç birim (bakım, kalite ve depo) rapor gönderdi.*
- Yanlış → Doğru: *Toplantının tek gündemi var — bütçe.* → *Toplantının tek gündemi var: bütçe.*
- **Kayma:** *Ekip sahaya çıktı — yağmur başladı.* → *Ekip sahaya çıktı: Yağmur başladı.* (İki olay yan yana duruyordu. İki nokta, ikincisini birincinin açıklaması gibi gösterir.)

### YZ-02 · "ve"den önce virgül (Oxford virgülü)

- **İz:** Sıralamanın son ögesinden önce "ve" ya da "veya"nın önüne konan virgül.
- **TDK:** "ve, veya, yahut, ya ... ya" bağlaçlarının önüne de ardına da virgül konmaz [TDK-NOK Virgül UYARI].
- **Yap:** Bağlacın önündeki virgülü sil. Sıralamadaki öbür virgüller kalır.
- **Dokunma:** Virgül sıralamaya değil, bağlaçtan hemen önce biten bir ara söze aitse kalır. Ara söz iki virgülle ayrılır [TDK-NOK Virgül 4]; kapanış virgülü silinirse ara sözün sınırı kaybolur. [Aynen tercihi] Doğru: *Toplantıya müdür, yani Ece Hanım, ve iki uzman katıldı.*
- **Kayma:** *Toplantıya müdür, yani Ece Hanım, ve iki uzman katıldı.* → *Toplantıya müdür, yani Ece Hanım ve iki uzman katıldı.* ("yani" artık iki uzmanı da kapsıyor gibi okunabilir. Betik bu kaymaya uyarı vermedi.)
- Yanlış → Doğru: *Formu Ece, Can, ve Deniz imzaladı.* → *Formu Ece, Can ve Deniz imzaladı.*
- Yanlış → Doğru: *Raporu PDF, veya CSV olarak indirin.* → *Raporu PDF veya CSV olarak indirin.*

### YZ-03 · Başlıklarda her sözcüğün büyük harfle başlaması

- **İz:** İngilizce başlık yazımı. Başlıktan cümle içine ve madde etiketlerine de taşınır. "Ve, İle, De" gibi bağlaçlar da büyük yazılır.
- **TDK:** Kitap, bildiri ve makalede alt başlıktaki sözcüklerin ilk harfleri büyük yazılır [TDK-BH E]. Bu türlerde her sözcüğü büyük harfle başlatmak TDK'ya uygundur. Her sözcüğü büyük yazılan eser ve kurum adlarında "ve, ile, ya, veya, yahut, ki, da, de" ve "mı/mi" küçük yazılır [TDK-BH C21 UYARI]. Aynı ilkeyi başlıklara da uygula. [Aynen tercihi] Cümle içinde yalnızca özel adlar büyük harfle başlar [TDK-BH C].
- **Yap:**
  - Başlık düzenine dokunma. Metindeki başlıklar tek bir düzen izliyorsa koru. [Aynen tercihi]
  - Başlıktaki büyük harfli bağlacı ve soru ekini küçült.
  - Cümle içinde özel ad olmayan sözcüklerin büyük harfini küçült. Önce sözcüğün belirli bir kurumu, birimi, programı ya da belgeyi adlandırıp adlandırmadığına bak. Adlandırıyorsa özel addır, dokunma (YA-08). Betik bu değişikliği KONTROL olarak bildirir.
- **Register:** E-posta, mesaj ve blog başlıkları için TDK sayfalarında kural yok. Kullanıcı istemedikçe bu başlıklara dokunma. Katalogdaki karşılığı: `kaliplar.md` → NOK-02.
- Yanlış → Doğru: *Riskler Ve Önlemler* → *Riskler ve Önlemler*
- Yanlış → Doğru: *Bu dönemde Müşteri Deneyimi ve Veri Güvenliği öne çıkıyor.* → *Bu dönemde müşteri deneyimi ve veri güvenliği öne çıkıyor.*

### YZ-04 · “ ” ve ‘ ’ karışıklığı

- **İz:** Vurguyu tek tırnakla göstermek (‘akıllı’). Açılış ve kapanış tırnağını karıştırmak. İç içe tırnakta dıştakini tek, içtekini çift yazmak. Tırnaktan sonra gelen eki kesmeyle ayırmak.
- **TDK:** Aktarılan ve vurgulanan söz tırnak içine alınır [TDK-NOK Tırnak 1, 2]. Tek tırnak yalnızca tırnak içinde yeniden tırnak gerektiğinde kullanılır [TDK-NOK Tek Tırnak]. Tırnaktan sonraki ek kesmeyle ayrılmaz [TDK-NOK Tırnak UYARI].
- **Yap:** İç içe tırnak değilse tek tırnağı çift tırnağa çevir. İç içe tırnakta dıştaki çift, içteki tek olsun. Açılış ve kapanışı eşle. Düz tırnak (") TDK sayfalarında ele alınmaz. Metin tutarlıysa dokunma (YN-08). Kodda ve satır içi kodda hiçbir tırnağa dokunma.
- Yanlış → Doğru: *Şirket ‘akıllı’ bir çözüm sunuyor.* → *Şirket “akıllı” bir çözüm sunuyor.*
- Doğru: *Ece “Plan ‘taslak’ olarak kalsın” dedi.* (Dışta tek, içte çift tırnak değil.) Betik bu değişikliği KONTROL olarak bildirebilir; kaynakla karşılaştırıp onayla.
- **Dikkat:** Tırnağı silmek aktarma ve mesafe bilgisini siler (YA-06).

### YZ-05 · Yüzde işaretinin sona konması

- **İz:** *25%* ya da *% 25*.
- **TDK:** Yüzde ve binde işareti sayının önüne, boşluk bırakılmadan yazılır [TDK-SAY 4]. Ek kesmeyle ve sayının okunuşuna göre gelir [TDK-KES 4].
- **Yap:** İşareti sayının önüne al, boşluğu sil. Ek varsa sayının okunuşuna göre yaz: *%40'ı* (yüzde kırkı).
- Yanlış → Doğru: *Hastaların 25%'i taburcu edildi.* → *Hastaların %25'i taburcu edildi.*
- Doğru: *Katılım %60 oldu.* (*% 60* değil.) Betik bu değişikliği KONTROL olarak bildirebilir; kaynakla karşılaştırıp onayla.
- **Kayma:** *Oran 5 puan arttı.* → *Oran %5 arttı.* (Yüzde puan ile yüzde aynı şey değildir. %40'lık bir oran 5 puan artınca %45, %5 artınca %42 olur. ANL-13. Betik bu çifti KESİN olarak yakalar.)

### YZ-06 · Ondalık nokta ve binlik virgül

- **İz:** İngilizce sayı düzeni. İngilizcede ondalık ayırıcı nokta, binlik ayırıcı virgüldür. Türkçede tersidir.
- **TDK:** Kesir virgülle ayrılır [TDK-SAY 8]. Dört ve daha çok basamaklı sayılar sondan üçlü gruplara ayrılır, araya nokta konur [TDK-SAY 7].
- **Yap:** Yalnızca değer kesinse çevir. Değer şu durumlarda kesindir:
  - Ayırıcı noktaysa, ardından üç basamak gelmiyorsa ve sayı saat değilse sayı ondalıktır: *3.5, 0.8, 12.75*.
  - Sayı kesirli olamayacak bir şeyi sayıyorsa (kişi, adet) virgülden sonraki üç basamak binliktir: *1,250 kişi*.
  - Öbür durumlarda değer belirsizdir: *2,500 mg* ya da *1.250 kg*. Dokunma, kullanıcıya sor (YN-05). Betik bu çiftleri "ayırıcı belirsiz" diye KONTROL'e koyar, KESİN saymaz (YA-07).
- **Dokunma:** Saat (*14.30* TDK'ye göre saattir [TDK-NOK Nokta 7]), bölüm ve madde numarası, sürüm numarası, tarih, kod, tablo verisi, yıl ve kanun sayısı (YN-71). Bir standardın, bağlantı tipinin ya da ürün modelinin adının parçası olmuş ölçü de adın kendisidir (YN-04): Katalogdaki yazılışı koru, kullanıcı istemedikçe çevirme. [Aynen tercihi]
- Yanlış → Doğru: *Ortalama bekleme 3.5 saat.* → *Ortalama bekleme 3,5 saat.*
- Yanlış → Doğru: *Ankete 1,250 kişi katıldı.* → *Ankete 1.250 kişi katıldı.*

### YZ-07 · İki noktadan sonra büyük ya da küçük harf

- **İz:** İki noktadan sonra gelen tam cümleyi küçük harfle, sözcük sıralamasını büyük harfle başlatmak.
- **TDK:** İki noktadan sonra gelen cümle büyük harfle başlar. Cümle ya da özel ad olmayan örnekler sıralanıyorsa küçük harfle başlar [TDK-BH A ve UYARI].
- **Yap:** Ardından gelen şey cümle mi, sıralama mı, ona bak. Özel adların büyük harfi kalır: *Katılımcılar: Ece, Can ve Deniz.* Bilgiyi her seferinde "Sonuç açık:", "Gerçek şu:" gibi bir ilanla açmak ayrı bir kalıptır: `kaliplar.md` → NOK-04.
- Yanlış → Doğru: *Sonuç açık: bu yöntem işe yarıyor.* → *Sonuç açık: Bu yöntem işe yarıyor.*
- Yanlış → Doğru: *Üç adım var: Planlama, uygulama ve değerlendirme.* → *Üç adım var: planlama, uygulama ve değerlendirme.*

### YZ-08 · Ünlem bolluğu

- **İz:** Bildirim cümlelerinin ünlemle bitmesi. Art arda ünlem.
- **TDK:** Ünlem, duygu bildiren cümlenin ve seslenme, hitap ve uyarı sözlerinin sonuna konur [TDK-NOK Ünlem 1, 2]. Öbür cümlelerin sonuna nokta konur [TDK-NOK Nokta 1]. Art arda ünlem TDK sayfalarında geçmez.
- **Yap:** Duygu, uyarı ya da çağrı taşımayan bildirim cümlesindeki ünlemi noktaya çevir. Art arda ünlemi teke indir. [Aynen tercihi] Duygu, uyarı ve seslenme ünlemini koru. Ayraç içindeki alay ünlemine dokunma (YA-05).
- **Register:** Reklam, davet, kutlama ve kişisel mesajda ünlem olağandır. Yazarın sesiyse dokunma (ANL-21). Güvenlik uyarısında ünlem işlevseldir: *Dikkat! Zemin ıslak.*
- Yanlış → Doğru: *Rapor ekte yer alıyor! Bilgilerinize sunarım!* → *Rapor ekte yer alıyor. Bilgilerinize sunarım.*
- Yanlış → Doğru: *Kayıtlar açıldı!!* → *Kayıtlar açıldı!*

### YZ-09 · Saatte iki nokta, tarihte İngilizce sıra

- **İz:** *14:30* ya da *Kasım 20, 2026*.
- **TDK:** Saat ile dakika nokta ile ayrılır [TDK-NOK Nokta 7]. TDK örneklerinde ay adlı tarih gün, ay, yıl sırasıyla yazılır: *5 Kasım 2026* [TDK-NOK Nokta 6 UYARI; TDK-BH Ç].
- **Yap:** Saatteki iki noktayı noktaya çevir; değer aynı kalır. Kod, tablo ve yazılım arayüzü metninde dokunma. Ay adı yazılmışsa değer kesindir, sırayı Türkçeye çevirebilirsin. Sayısal tarihe dokunma (YN-06).
- Yanlış → Doğru: *Toplantı 14:30'da başlıyor.* → *Toplantı 14.30'da başlıyor.*
- Yanlış → Doğru: *Son gün Kasım 20, 2026.* → *Son gün 20 Kasım 2026.*

---

## 12. Anlam riski: Noktalamanın anlamı değiştirdiği yerler

Aşağıdaki örneklerin hepsi **Kayma**dır. Noktalama ya da yazım tek başına anlamı değiştirir. Düzeltme yaparken bu işaretleri ekleme, silme ya da yerinden oynatma.

Betik bu kaymaların çoğunu görmez. Sınamada yalnızca şunları yakaladı: YA-04'teki "(?)", YA-07, YA-08, YA-09 ve YA-10'daki "ve/veya" KONTROL; YA-10'daki eksi işareti KESİN. YA-01, YA-02 ("Merkez de" için yalnızca büyük harf uyarısı), YA-03, YA-05, YA-06 ve öbür soru işareti kaymaları için betik "Sorun bulunmadı" dedi. Bunları sen okursun.

### YA-01 · Virgül öznenin ve sıfatın sınırını çizer

[TDK-NOK Virgül 10, 14] · ANL-11, ANL-19
- **Kayma:** *Genç, hekimi aradı.* → *Genç hekimi aradı.* (Arayan genç biriydi, aranan hekimdi. Virgül gidince aranan "genç hekim" olur, arayan belirsizleşir.)
- **Kayma:** *Bu, kalibrasyon cihazının raporu.* → *Bu kalibrasyon cihazının raporu.* (Virgüllü cümlede "bu" eldeki belgeyi gösteren öznedir. Virgül gidince "bu" cihazın sıfatı olarak da okunabilir: Hangi cihazdan söz edildiği değişir.)
- **Bak:** Özne ya da sıfat sınırındaki virgülü silme. Yeni bir virgül eklemek de sınırı değiştirir.

### YA-02 · de/da ayrı mı, bitişik mi

[TDK-DE; TDK-BUL] · ANL-11, ANL-12
- **Kayma:** *Merkezde onay verdi.* → *Merkez de onay verdi.* (İlkinde biri merkezde onay verdi. İkincisinde onay veren merkezdir ve başkalarının da onay verdiği anlaşılır.)
- **Bak:** "de"yi ayırırken ya da bitiştirirken öznenin ve odağın değişip değişmediğine bak.

### YA-03 · Noktalı virgül grupları ayırır

[TDK-NOK Noktalı Virgül 1] · ANL-03, ANL-20
- **Kayma:** *Eğitime üç ekip katılacak: Ece, Can; Deniz, Selin; Ozan, Ali.* → *Eğitime üç ekip katılacak: Ece, Can, Deniz, Selin, Ozan, Ali.* (Kimin hangi ekipte olduğu bilgisi düştü.)
- **Bak:** Virgüllü takımları ayıran noktalı virgülü virgüle çevirme.

### YA-04 · Soru işareti soruyu bildirimden ayırır

[TDK-NOK Soru 2, 3 ve UYARI; TDK-MI] · ANL-18, ANL-01, ANL-17
- **Kayma:** *Ödeme yapıldı?* → *Ödeme yapıldı.* (Soru eki yok. Soruyu yalnızca işaret taşıyordu. Silinince soru, olgu bildirimine döndü.)
- **Kayma:** *Tesis 1987 (?) yılında kuruldu.* → *Tesis 1987 yılında kuruldu.* (Kuşkulu tarih kesinleşti.)
- **Kayma:** *Alarm çaldı mı binayı boşaltıyoruz.* → *Alarm çaldı mı? Binayı boşaltıyoruz.* (Koşul bildiren yan cümle bir soruya, temel cümle de koşulsuz bir eyleme dönüştü.)
- **Bak:** Kaynaktaki her soru hâlâ soru mu? Her "(?)" yerinde mi? "mı" ile kurulan koşul cümlesine soru işareti eklenmiş mi?

### YA-05 · Ayraç içindeki ünlem alay bildirir

[TDK-NOK Ünlem 3; Yay Ayraç 6] · ANL-21
- **Kayma:** *Rapor çok titiz (!) hazırlanmış.* → *Rapor çok titiz hazırlanmış.* (Alay düştü. Eleştiri övgüye döndü.)

### YA-06 · Tırnak aktarmayı ve mesafeyi gösterir

[TDK-NOK Tırnak 1, 2] · ANL-15, ANL-21, ANL-22
- **Kayma:** *Firma “gönüllü” fazla mesai uyguluyor.* → *Firma gönüllü fazla mesai uyguluyor.* (Yazar "gönüllü" sözüne mesafe koymuştu. Tırnak gidince fazla mesai gerçekten gönüllüymüş gibi okunur.)
- **Kayma:** *Müdür “Bütçe yeterli” dedi, ama ek ödenek istendi.* → *Müdür “Bütçe yeterli, ama ek ödenek istendi” dedi.* (Kapanış tırnağı kayınca ikinci bilgi de müdüre mal edildi.)
- **Bak:** Tırnağın sınırları kaynaktakiyle aynı mı? Tırnak silinince söz başkasınınken yazarın sözüne mi döndü?

### YA-07 · Sayı ayırıcısı değeri bin kat değiştirebilir

[TDK-SAY 7, 8] · ANL dizininde sayının değeri için ayrı kod yok. Değer betiğin KESİN denetimindedir. Ayırıcı belirsizse betik yalnızca KONTROL verir.
- **Kayma:** *Numunede 1,250 mg kurşun ölçüldü.* → *Numunede 1.250 mg kurşun ölçüldü.* (Türkçe okumada ilki bir virgül iki yüz elli miligram, ikincisi bin iki yüz elli miligramdır. Değer bin kat büyüdü.)
- **Bak:** YN-05 ve YZ-06. Değer kesin değilse dokunma, kullanıcıya sor.

### YA-08 · Büyük harf belirli bir şeyi gösterir

[TDK-BH C12, C20] · ANL-14, ANL-15
- **Kayma:** *Öneriyi Kurul reddetti.* → *Öneriyi kurul reddetti.* (Metinde adı geçen belirli bir kurul, herhangi bir kurula dönüştü.)
- **Kayma:** *Firma Doğu pazarına açılıyor.* → *Firma doğu pazarına açılıyor.* (Kültürel ve siyasal anlamdaki Doğu, bir bölgenin doğusuna dönüştü.)
- **Bak:** Büyük harfi küçültmeden önce sözcüğün bir göndergesi olup olmadığına bak (YZ-03).

### YA-09 · Sayısal tarih iki türlü okunur

[TDK-NOK Nokta 6; Eğik Çizgi 3] · ANL-08
- **Kayma:** *Son başvuru 03/04/2026.* → *Son başvuru 3 Nisan 2026.* (Kaynak ay/gün düzeniyle yazıldıysa son gün 4 Mart'tı.)
- **Bak:** YN-06. Sayısal tarihe dokunma.

### YA-10 · Çizgi ve eğik çizgi değerin ve bağın parçasıdır

[TDK-NOK Kısa Çizgi 9] · ANL-18
- **Kayma:** *Aşı -18 °C'de saklanır.* → *Aşı 18 °C'de saklanır.* (Eksi işareti düştü. Betik bunu KESİN olarak yakalar.)
- **Kayma:** *Belgeler PDF ve/veya CSV olarak yüklenebilir.* → *Belgeler PDF ve CSV olarak yüklenebilir.* (Birinin yettiği durum, ikisinin birden gerektiği bir duruma dönüşebilir.)

---

## Kaynaklar

Bütün TDK sayfalarına 5 Kasım 2026'da erişildi. Sayfaların tam metni sitenin yazı arayüzünden okundu: https://tdk.gov.tr/wp-json/wp/v2/posts?categories=27 ("Yazım Kuralları" kategorisi, 36 sayfa). "Yazı no." sitenin sayfa kimliği, "güncelleme" sayfanın son değiştirilme tarihidir. Sayfa numarası verilmedi, çünkü bunlar çevrim içi sayfalardır.

| Etiket | Başlık | Kurum | Bağlantı | Yazı no. · güncelleme |
|---|---|---|---|---|
| TDK-NOK | Noktalama İşaretleri (Açıklamalar) | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/noktalama-isaretleri-aciklamalar/ | 493 · 12.09.2023 |
| TDK-KES | Kesme İşareti ( ’ ) | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/kesme-isareti/ | 10648 · 10.03.2025 |
| TDK-BH | Büyük Harflerin Kullanıldığı Yerler | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/buyuk-harflerin-kullanildigi-yerler/ | 489 · 08.01.2026 |
| TDK-SAY | Sayıların Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/sayilarin-yazilisi/ | 488 · 16.07.2021 |
| TDK-KIS | Kısaltmalar | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/kisaltmalar/ | 494 · 12.09.2023 |
| TDK-SIM | Simgeler | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/simgeler/ | 539 · 16.07.2021 |
| TDK-BIT | Bitişik Yazılan Birleşik Kelimeler | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/bitisik-yazilan-birlesik-kelimeler/ | 490 · 12.09.2023 |
| TDK-AYR | Ayrı Yazılan Birleşik Kelimeler | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/ayri-yazilan-birlesik-kelimeler/ | 538 · 12.09.2023 |
| TDK-IKL | İkilemelerin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/ikilemelerin-yazilisi/ | 526 · 16.07.2021 |
| TDK-DE | Bağlaç Olan da, de'nin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/baglac-olan-da-denin-yazilisi/ | 530 · 16.07.2021 |
| TDK-BUL | Bulunma Durumu Eki -da / -de / -ta / -te'nin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/bulunma-durumu-eki-da-de-ta-tenin-yazilisi/ | 533 · 16.07.2021 |
| TDK-KI | Bağlaç Olan ki'nin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/baglac-olan-kinin-yazilisi/ | 531 · 16.07.2021 |
| TDK-MI | Soru Eki mı, mi, mu, mü'nün Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/soru-eki-mi-mi-mu-munun-yazilisi/ | 529 · 16.07.2021 |
| TDK-ILE | İle'nin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/ilenin-yazilisi/ | 532 · 16.07.2021 |
| TDK-EKF | Ek-fiilin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/ek-fiilin-yazilisi/ | 536 · 12.09.2023 |
| TDK-FC | Fiil Çekimi ile İlgili Yazılışlar | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/fiil-cekimi-ile-ilgili-yazilislar/ | 534 · 16.07.2021 |
| TDK-DUZ | Düzeltme İşareti | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/duzeltme-isareti/ | 483 · 16.07.2021 |
| TDK-ALN | Alıntı Kelimelerin Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/alinti-kelimelerin-yazilisi/ | 500 · 16.07.2021 |
| TDK-YOA | Yabancı Özel Adların Yazılışı | Türk Dil Kurumu | https://tdk.gov.tr/icerik/yazim-kurallari/yabanci-ozel-adlarin-yazilisi/ | 492 · 16.07.2021 |
| GTS | Güncel Türkçe Sözlük (madde sorguları) | Türk Dil Kurumu | https://sozluk.gov.tr/ (sorgu biçimi: https://sozluk.gov.tr/gts?ara=SÖZCÜK) | - |
| RYY | Resmî Yazışmalarda Uygulanacak Usul ve Esaslar Hakkında Yönetmelik (Cumhurbaşkanı Kararı 2646, Resmî Gazete 10.06.2020, sayı 31151); md. 11 (sayı), 13 (konu), 15 (ilgi), 16/12 (metnin son bölümü), 18 (ek), 19 (dağıtım) | T.C. Cumhurbaşkanlığı | https://mevzuat.gov.tr/MevzuatMetin/21.5.2646.pdf | - |
| FREEBURG | E. M. Freeburg, "The Last Fingerprint: How Markdown Training Shapes LLM Prose", arXiv:2603.27006 [cs.CL], 27 Mart 2026. Hakem denetiminden geçmemiş ön baskı. Yalnızca özeti okundu. | - | https://arxiv.org/abs/2603.27006 | - |

**Erişilemeyen kaynaklar:** Göksel ve Kerslake, Korkmaz, Banguoğlu, Ergin ve Gencan'ın dil bilgisi kitaplarına bu çalışmada erişilmedi. Türkçe yapay zekâ metinlerinin noktalamasını inceleyen hakemli bir çalışma bulunamadı.
