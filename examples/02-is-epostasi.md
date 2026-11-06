# Örnek 2: İş e-postası (proje gecikmesi)

**Register:** iş yazışması (ekip içi) · **Seviye:** orta · **Kişi:** birinci tekil yazar, olgular edilgen

İş e-postasında en kolay kayan bilgi, bir önerinin karar gibi okunmasıdır. Bu örnekte sohbet kalıntıları ve bürokratik kalıplar temizlenir. Öneri, karar yetkisi, "henüz" ve yaklaşık yüzde aynı kalır.

## Önce

> Konu: Depo Yönetim Sistemi Projesinin Güncel Durumu Hakkında Bilgilendirme
>
> Merhaba ekip,
>
> Umarım bu e-posta hepinizi iyi bulur! Depo yönetim sistemi projemizin güncel durumu hakkında sizleri bilgilendirmek istiyorum.
>
> Mevcut durumda projenin yaklaşık %70'lik kısmı tamamlanmış durumdadır. Ancak, tedarikçi firmadan gelmesi beklenen barkod okuyucuların teslimatında yaşanan gecikme nedeniyle saha testlerine henüz başlanamamıştır. Bu durum, canlıya geçiş için 1 Aralık olarak planlanan tarihi doğrudan etkilemektedir.
>
> Bu doğrultuda, canlıya geçiş tarihinin 15 Aralık'a ertelenmesinin daha uygun olacağını düşünüyorum. Şunu belirtmek isterim ki, bu yalnızca bir öneridir ve nihai karar yönlendirme komitesine aittir.
>
> Bunun yanı sıra, test senaryolarının hazırlanmasına yönelik çalışmalar da paralel olarak yürütülmektedir. Bu gecikme yalnızca bir zaman kaybı değil, aynı zamanda test sürecini daha sağlam kurmak için bir fırsattır.
>
> Herhangi bir sorunuz olursa lütfen çekinmeden bana ulaşın. Umarım yardımcı olur!
>
> Saygılarımla,
>
> Deniz

## Sonra

> Konu: Depo yönetim sistemi projesinin güncel durumu
>
> Merhaba ekip,
>
> Umarım hepiniz iyisinizdir. Depo yönetim sistemi projemizin son durumunu paylaşmak istiyorum.
>
> Şu ana kadar projenin yaklaşık %70'i tamamlandı. Ancak tedarikçi firmadan beklenen barkod okuyucuların teslimatı geciktiği için saha testlerine henüz başlanamadı. Bu durum, canlıya geçiş için planlanan 1 Aralık tarihini doğrudan etkiliyor.
>
> Bu doğrultuda, canlıya geçişin 15 Aralık'a ertelenmesinin daha uygun olacağını düşünüyorum. Bu yalnızca bir öneri; nihai karar yönlendirme komitesine ait.
>
> Test senaryolarının hazırlanması da paralel olarak sürüyor. Bu gecikme hem bir zaman kaybı hem de test sürecini daha sağlam kurmak için bir fırsat.
>
> Herhangi bir sorunuz olursa lütfen çekinmeden bana ulaşın.
>
> Saygılarımla,
>
> Deniz

---
Denetim (metne dahil değil): seviye orta · betik 0 KESİN, 4 KONTROL satırı ve 5 hedefli soru tek tek incelendi · iki yönlü önerme kontrolü yapıldı. Silinen: "Umarım yardımcı olur!" (sohbet kapanışı). Son okuma sizde.

## Düzeltilen kalıplar

| ID | Ne değişti |
|---|---|
| NOK-02 | Konu satırında her sözcük büyük harfle başlıyordu. Metin içinde küçük harfle yazıldığı için "depo yönetim sistemi" bir özel ad değil. "Hakkında Bilgilendirme" de atıldı. |
| CEV-01 | "Umarım bu e-posta hepinizi iyi bulur!" → "Umarım hepiniz iyisinizdir." |
| KLS-09 · DLB-05 | "Mevcut durumda ... %70'lik kısmı tamamlanmış durumdadır" → "Şu ana kadar ... %70'i tamamlandı" |
| DLB-04 | "teslimatında yaşanan gecikme nedeniyle" → "teslimatı geciktiği için"; "hazırlanmasına yönelik çalışmalar ... yürütülmektedir" → "hazırlanması ... sürüyor" |
| DLB-01 | "etkilemektedir" → "etkiliyor"; "başlanamamıştır" → "başlanamadı" |
| KLS-08 | "Şunu belirtmek isterim ki" silindi. |
| YPI-07 | "Bunun yanı sıra" silindi. Ekleme işini "da" görüyor. |
| YPI-05 | "yalnızca bir zaman kaybı değil, aynı zamanda ... bir fırsattır" → "hem bir zaman kaybı hem de ... bir fırsat" |
| ACL-03 | "Umarım yardımcı olur!" silindi. |

## Bilinçli olarak korunanlar

- **"yaklaşık %70":** "yaklaşık" sayının yanında kaldı (ANL-01).
- **"henüz başlanamadı":** "henüz" testlerin başlayacağını sezdiriyor (ANL-08). "-ama-" bir yapamamayı bildiriyor, "başlanmadı" yazılmadı. Cümle edilgen kaldı, kaynakta olmayan bir "biz" eklenmedi (ANL-11).
- **"teslimatı geciktiği için":** Sebep bağı aynı iki olay arasında kaldı (ANL-06).
- **"Bu durum ... doğrudan etkiliyor":** Gönderge "bu gecikme" diye daraltılmadı (ANL-15). "doğrudan" derece sözüdür (ANL-02).
- **"Bu doğrultuda":** Tek kullanım ve belirli bir bağ kuruyor: Öneriyi önceki paragraftaki duruma bağlıyor. Silinmedi, "bu yüzden" diye bir sebep bağına da çevrilmedi (KLS-01 Dokunma, ANL-06).
- **"daha uygun olacağını düşünüyorum" ve "Bu yalnızca bir öneri; nihai karar yönlendirme komitesine ait":** Öneri öneri olarak kaldı, karar yetkisi komitede (ANL-07, ANL-16, ANL-11). E-postada "-dır"ı düşürmek resmiyeti bozmuyor (ANL-10).
- **1 Aralık, 15 Aralık:** aynen.
- **"da paralel olarak sürüyor":** "da" test senaryolarına bağlı. "paralel olarak" biçim bildiriyor. Süren görünüş kaldı (ANL-12, DLB-02 Dokunma, ANL-08).
- **"hem ... hem de ... bir fırsat":** Değerlendirme silinmedi, iki yanı da duruyor (YPI-05, ANL-02).
- **"Herhangi bir sorunuz olursa lütfen çekinmeden bana ulaşın":** Gerçek bir davet. Koşul ve rica kaldı; "yazın" ya da "ulaşabilirsiniz" yapılmadı (ACL-03 Dokunma, ANL-07, ANL-17).

## Anlamı kaydıracak seçimler

1. **Yaklaşıklık düştü.**
   - Kaynak: *Mevcut durumda projenin yaklaşık %70'lik kısmı tamamlanmış durumdadır.*
   - Kötü: *Projenin %70'i bitti.*

   "yaklaşık" düştü. Tahmini bir oran kesin bir ölçüm gibi okunuyor (ANL-01). Betik bunu KESİN olarak yakalar.

2. **"Henüz" ve yapamama düştü, "biz" eklendi.**
   - Kaynak: *... saha testlerine henüz başlanamamıştır.*
   - Kötü: *... saha testlerine başlamadık.*

   "henüz" düşünce testlerin başlayacağı bilgisi kayboldu (ANL-08). Yapamama, yapmamaya döndü: Gecikme bir tercih gibi okunuyor. Kaynakta olmayan "biz" eklendi (ANL-11). Betik bunları KONTROL olarak gösterir.

3. **Öneri karara döndü.**
   - Kaynak: *Bu doğrultuda, canlıya geçiş tarihinin 15 Aralık'a ertelenmesinin daha uygun olacağını düşünüyorum. ... bu yalnızca bir öneridir ve nihai karar yönlendirme komitesine aittir.*
   - Kötü: *Bu yüzden canlıya geçişi 15 Aralık'a erteliyoruz.*

   Öneri bir karara döndü (ANL-07, ANL-16). Karar yetkisi komiteden yazara ve ekibe geçti (ANL-11). "Bu doğrultuda" bir sebep bağına çevrildi (ANL-06). Akıcı ve kısa, ama komiteyi devre dışı bırakan bir e-posta. Betik düşen öneri cümlesini ve yeni "biz"i KONTROL olarak gösterir.
