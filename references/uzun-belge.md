# Uzun belge modu

Tez, kitap bölümü ya da uzun rapor gibi 2.000 sözcükten uzun ya da birden çok dosyadan oluşan belgelerde bu iş akışını izle. SKILL.md'deki bütün kurallar burada da geçerlidir. Bu dosya yalnızca ölçeğin getirdiği adımları ekler.

Uzun bir belgede en büyük tehlike tek bir büyük hata değildir. Asıl tehlike, yüzlerce küçük değişikliğin içinde fark edilmeyen birkaç kaymadır. Bu yüzden amaç şudur: Her değişiklik görülebilir, gerekçesi yazılı ve geri alınabilir olmalı.

## 0. Başlamadan önce kullanıcıya söyle

Tahmini iş yükünü söyle:
- kaç parça çıkacağı
- her değişen parça için ayrı bir bağımsız denetçi çalışacağı
- asıl dosyaya dokunulmayacağı

Kullanıcı isterse önce bir iki bölümle başla ve sonucu birlikte değerlendirin.

## 1. Kopya üzerinde çalış

- Asıl dosyaları değiştirme. Düzeltilmiş dosyaları ayrı bir klasöre yaz (ör. `<belge>_duzeltilmis/`).
- Asıl dosyaya geçirmek kullanıcının onayıyla ve kullanıcının işidir.
- Kaynak ya da hukuk denetiminden geçmiş bir metinde bu kural özellikle önemlidir. Dipnotun bağlı olduğu cümle değişirse o denetim geçersiz olur.

## 2. Plan çıkar

```
python3 -I <skill-klasörü>/scripts/bolumle.py belge.md --koru "kaynak kontrolü;araştırma notu"
```

Betik her başlığın sözcük ve dipnot sayısını, korunan bölümleri ve 1.500 sözcüğü aşmayan çalışma parçalarını listeler. Belgeye dokunmaz.

**Korunan bölümler:**
- kaynakça
- projenin iç notları (kaynak kontrolü, araştırma notu, devir notu gibi)
- kullanıcının "dokunma" dediği bölümler

Bunlar yeniden yazılmaz. `--koru` ile verilen bölümler betikte de birebir denetlenir.

**Ön tarama:** Her dosyada şunu çalıştır:

```
python3 -I <skill-klasörü>/scripts/tarama.py belge.md --koru "kaynak kontrolü;araştırma notu"
```

Betik, `kaliplar.md`'deki kalıplardan sözcükle bulunabilenleri her paragrafta arar ve satır ile kalıp kimliğiyle listeler. Belgeye dokunmaz.
- **BELİRGİN** izler hemen her türde düzeltilir.
- **TÜRE BAĞLI** izlerde kalıbın Dokunma satırına bak. Akademik ve hukuki metinde çoğu olağan dildir.
- Üçlü sıralama, eş anlamlı döndürme, kalıp tekrarı ve ritim gibi yapısal kalıplar sözcükle aranamaz. Bunları metni okurken ara.

Tarama sonucunu iş yükü tahminiyle birlikte kullanıcıya söyle. Belirgin iz çıkmayan bir dosya büyük olasılıkla zaten temizdir; az değişiklik beklenir.

**Başvuru dosyalarını okuma:** `anlam-kaymasi.md`'yi tamamen oku; anlam her şeyden önce gelir. `kaliplar.md`'nin tamamını okumak gerekmez. Dizinini, taramada çıkan kalıpların maddelerini ve sözcükle aranamayan kalıpların (YPI-01, YPI-02, YPI-03, YPI-06) maddelerini oku.

## 3. Belge geneli listesi

`belge-geneli.md` adlı bir çalışma dosyasına şunları yaz:
- **Terimler ve tanımlar:** Projenin kılavuzunda bir terminoloji bölümü varsa onu esas al. Terimleri ayrıca `terimler.txt` dosyasına her satıra bir terim olacak biçimde yaz; betiğe `--terimler terimler.txt` ile verilir.
- **Kısaltmalar:** Kısaltmanın ilk geçtiği yer ve açılımı.
- **Kapsam sınırları ve istisnalar:** "Bu çalışmada X yalnızca Y'yi kapsar" türünden cümleler.
- **Yazarın görüş işaretleri:** "kanaatimizce, kanımızca, bize göre". Bunlar azaltılmaz ve silinmez (ANL-22).
- **Bölümler arası gönderimler:** "aşağıda (Üçüncü Bölüm, V.C)" gibi.

Her parçayı bu listeyle birlikte düzelt. Bağımsız denetçiye de bu listeyi ver.

## 4. İlerleme dosyası

Önerme listelerini `onermeler-<dosya>.md` dosyasına yaz. Önerme listesini yalnızca değiştirdiğin paragraflar için yaz. Değişmeyen cümleleri betik kaynakla birebir karşılaştırır, düşen cümleyi de bildirir. `ilerleme.md` adlı bir dosyada her parça için tek satır tut: parça, durum, betik sonucu, denetçi sonucu, not.

Durum şunlardan biridir: bekliyor, düzeltildi, denetlendi, kullanıcı onayladı.

Bağlam dolarsa ya da iş yeni bir oturumda sürerse bu dosyadan ve `belge-geneli.md`'den devam edilir. Bir parçayı yarım bırakma: Ya bitir ya da başlamadan dur.

## 5. Parça parça düzelt

Varsayılan seviye hafiftir. Her parça için:

1. **Yeniden yaz.** Paragraf paragraf, küçük düzenlemelerle çalış. Bütün parçayı tek seferde yeniden üretme. Tek seferde yeniden üretmek fark edilmeyen kayma riskini en çok artıran yoldur.
   - Ön taramanın işaretlediği paragraflardan başla, ama öteki paragrafları da oku: Yapısal kalıplar ve sözcük listesinde olmayan izler taramada görünmez.
   - Dipnot işaretleri desteklediği iddianın hemen yanında kalır. Dipnotlu bir cümleyi yalnızca her dipnotun hangi iddiayı desteklediği açıksa böl ya da birleştir. Dipnot birden çok yan cümleyi destekliyor olabilirse cümleye dokunma ve bunu belirsiz yerler listesine yaz.
2. **Betik.** Kaynak ve yeni dosyanın bütünüyle çalıştır:

   ```
   python3 -I <skill-klasörü>/scripts/anlam_denetimi.py kaynak.md yeni.md --koru "..." --terimler terimler.txt
   ```

   KESİN satırlarının hepsini düzelt, KONTROL satırlarının her birine hüküm ver (SKILL.md 4a). HEDEFLİ SORULAR bölümündeki her soruyu kaynak ve yeni cümle için ayrı ayrı yanıtla, cevapları `onermeler-<dosya>.md` dosyasına yaz (SKILL.md 4b).
3. **İki yönlü önerme kontrolü** (SKILL.md 4b): değişen paragraflarda.
4. **Bağımsız denetçi.** Değişen her parçada çalıştır. Hiç değişmeyen parçada gerekmez. Denetçiye şunları ver:
   - parçanın kaynak ve yeni hâli
   - `belge-geneli.md`
   - `references/dogrulama.md`
   - betiğin hedefli sorularının listesi (senin cevapların olmadan)

   Denetçinin her bulgusunu düzelt ve betiği yeniden çalıştır.
5. `ilerleme.md`'yi güncelle.

## 6. Dosya bitince

İç jargon ve kelime kelime çevrilmiş isim zinciri önerilerini (CEV-06) her parçada ayrı ayrı sunma. Bütün dosya için tek bir öneri listesinde topla: tekrar edenleri birleştir, her öneriyi bir kez yaz. Kullanıcı listeden seçtiklerini toplu olarak onaylasın.


Betiği `--fark` ile çalıştır ve fark tablosunu `degisiklikler-<dosya>.md` olarak kaydet. Tabloda değişen her cümle önce ve sonra hâliyle yer alır. Kullanıcı değişiklikleri buradan tek tek gözden geçirir, istemediğini geri alır.

## 7. Bütün belge bitince

- `belge-geneli.md`'deki her terim, kısaltma ve tanım bütün dosyalarda aynı mı?
- Bölümler arası gönderimler duruyor mu?
- Toplam sözcük sayısı ve dipnot sayısı aynı mı? Betiğin ilk satırı sözcük sayısını, `bolumle.py` dipnot sayısını verir.

## 8. Teslim

Denetim notunu ve öteki notları düzeltilmiş dosyanın içine yazma. Bunlar özete girer. Kullanıcıya `teslim.md` dosyasında ve sohbette kısa bir özet ver:
- kaç parça işlendiği ve kaç cümlenin değiştiği
- kaç KONTROL satırının incelendiği
- denetçilerin bulduğu ve düzeltilen sorunlar
- anlamından emin olunamadığı için dokunulmayan yerler (yazarın karar vermesi gereken belirsizlikler)
- değişiklik tablolarının yeri

Asıl dosyaya geçirmek için kullanıcının onayını bekle. Hiçbir aşama sıfır hata garantisi vermez. Son okuma yazarındır.
