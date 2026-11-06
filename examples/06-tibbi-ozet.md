# Örnek 6: Tıbbi özet (iş sağlığı)

**Register:** akademik/tıbbi · **Seviye:** hafif · **Kişi:** edilgen/nesnel

Tıbbi metinde anlamı en çok temkin, olumsuzluk ve ilişki/neden ayrımı taşır. Bu örnek önce güvenli düzeltmeyi, sonra akıcı görünen ama anlamı kaydıran bir yeniden yazımı gösterir.

## Önce

> Günümüzde vardiyalı çalışma, iş sağlığında önemi giderek büyüyen kritik bir mesele hâline gelmiştir. Bu bağlamda, söz konusu çalışmada bir lojistik deposunda çalışan 412 işçide gece vardiyası ile bel ağrısı arasındaki ilişki incelenmektedir. Veriler, 2025 yılının Mart-Haziran döneminde yüz yüze görüşme yöntemiyle toplanmış olup lojistik regresyon analizi kullanılarak değerlendirilmiştir. Elde edilen bulgular, gece vardiyasında çalışanlarda bel ağrısı sıklığının gündüz vardiyasına göre daha yüksek olduğunu göstermektedir (OR 1,84; %95 GA 1,21–2,79; p=0,004). Bununla birlikte, yaş grupları arasında istatistiksel olarak anlamlı bir fark bulunmamıştır. Bu bulgular, gece çalışmasının bel ağrısı ile ilişkili olabileceğini düşündürmektedir. Sonuç olarak, vardiya planlamasında ergonomik risklerin göz önünde bulundurulması büyük önem taşımaktadır.

## Sonra

> Vardiyalı çalışma, iş sağlığında önemi giderek büyüyen kritik bir mesele hâline gelmiştir. Bu çalışmada bir lojistik deposunda çalışan 412 işçide gece vardiyası ile bel ağrısı arasındaki ilişki incelenmektedir. Veriler 2025 yılının Mart-Haziran döneminde yüz yüze görüşmeyle toplanmış, lojistik regresyon analiziyle değerlendirilmiştir. Bulgular, gece vardiyasında çalışanlarda bel ağrısı sıklığının gündüz vardiyasına göre daha yüksek olduğunu göstermektedir (OR 1,84; %95 GA 1,21–2,79; p=0,004). Bununla birlikte, yaş grupları arasında istatistiksel olarak anlamlı bir fark bulunmamıştır. Bu bulgular, gece çalışmasının bel ağrısıyla ilişkili olabileceğini düşündürmektedir. Vardiya planlamasında ergonomik risklerin göz önünde bulundurulması çok önemlidir.

---
Denetim (metne dahil değil): seviye hafif · betik 0 KESİN, KONTROL satırları tek tek incelendi · iki yönlü önerme kontrolü yapıldı. Son okuma sizde.

## Düzeltilen kalıplar

Kimlikler `references/kaliplar.md`'deki kalıplardır.

| ID | Ne değişti |
|---|---|
| ACL-01 | Açılıştaki "Günümüzde" silindi. Zamanı sınırlamıyordu. |
| KLS-01 | "Bu bağlamda," silindi. Belirli bir bağ kurmuyordu. |
| KLS-02 | "söz konusu çalışmada" → "Bu çalışmada" |
| DLB-02 | "toplanmış olup" → "toplanmış," (tek cümle, iki yüklem; "-tir" ikisini de kapsar) |
| KLS-09 | "Elde edilen bulgular" → "Bulgular"; "görüşme yöntemiyle" → "görüşmeyle"; "analizi kullanılarak" → "analiziyle" (yöntemin ve testin adı kaldı) |
| ACL-04 | Son cümlenin başındaki "Sonuç olarak," silindi. |
| KLS-03 | "büyük önem taşımaktadır" → "çok önemlidir" (derece korundu) |

## Bilinçli olarak korunanlar

- **412, 2025, Mart-Haziran, OR 1,84, %95 GA 1,21–2,79, p=0,004:** aynen.
- **"işçi":** Kaynaktaki terim. "Çalışan" ile değiştirilmedi (ANL-14).
- **"ilişki" ve "ilişkili olabileceğini düşündürmektedir":** İlişki bir nedene, temkin de kesinliğe dönüşmedi (ANL-01, ANL-05).
- **"anlamlı bir fark bulunmamıştır":** "Yaşın etkisi yoktur" yazılmadı (ANL-04).
- **"gündüz vardiyasına göre daha yüksek":** Karşılaştırmanın tabanı korundu (ANL-13).
- **"incelenmektedir", "Bununla birlikte":** Hafif seviyede yüklemin zamanı ve bağlaçlar yerinde kalır.
- **"önemi giderek büyüyen kritik bir mesele hâline gelmiştir":** Derece sözü ("giderek") ve değerlendirme yerinde kaldı (ANL-02). Tıpta "kritik" bir terim de olabildiği için hafif seviyede değiştirilmedi (KLS-05).

## Güvenli olmayan yeniden yazım

Aşağıdaki metin akıcıdır ve yapay zeka izlerinin çoğunu temizler, ama yedi yerde anlamı değiştirir:

> Vardiyalı çalışma iş sağlığının önemli konularından biri. Bir lojistik deposundaki 421 çalışanla yaptığımız bu çalışmada gece vardiyasının bel ağrısına etkisini inceledik. Gece çalışanlarda bel ağrısı daha sık görüldü (OR 1.84; p=0,004). Yaşın ise bir etkisi yoktu. Kısacası gece çalışması bel ağrısını artırıyor, bu yüzden vardiyalar ergonomik risklere göre planlanmalı.

1. **412 → 421** ve **1,84 → 1.84**: değer ve biçim bozuldu, %95 GA düştü. Betik bunları KESİN olarak yakalar.
2. **işçi → çalışan:** terim değişti (ANL-14).
3. **"yaptığımız ... inceledik":** Kaynakta olmayan "biz" eklendi ve edilgen anlatım birinci kişiye döndü (ANL-11, register).
4. **"ilişki" → "etkisi", "ilişkili olabileceği" → "artırıyor":** ilişki nedenselliğe, temkin kesinliğe dönüştü (ANL-01, ANL-05).
5. **"gündüz vardiyasına göre" düştü:** Karşılaştırmanın tabanı kayboldu (ANL-13).
6. **"anlamlı fark bulunmamıştır" → "bir etkisi yoktu":** Kanıt yokluğu, etkinin yokluğuna dönüştü (ANL-04).
7. **"göz önünde bulundurulması büyük önem taşımaktadır" → "bu yüzden ... planlanmalı":** Öneri zorunluluğa dönüştü ve bulgulara bir "bu yüzden" bağıyla bağlandı (ANL-06, ANL-07).
