# Faktoriyel hesabı
def faktoriyel(sayi):
    """Bu fonsiyon verilen bir pozitif tam sayı
        için faktoriyel değeri hesaplar:
        6! = 1 * 2 * 4 * 5 * 6 = 120
    """
    # Sayı sıfırdan büyük mü kontrol et
    if sayi >= 0:
        # Eğer sayı sıfırdan büyük ise

        # Sayı sıfıra eşit mi kontrol et
        if sayi == 0:
            # Eğer sayı sıfıra eşit ise 1 değeri geri döndür
            return 1
            # Bu aşamada fonksiyon durur

        # sonuc adlı değişkene 1 değeri ata
        sonuc = 1
        # 1'den sayi+1'e kadar bir döngü oluştur: 1, 2, 3, ... , sayi
        for i in range(1, sayi + 1):
            # sonuc değerini i ile çarpıp, sonuc değişkenine ata
            sonuc *= i
        # sonuc'u döndür
        return sonuc
    else:
        # Eğer sayı sıfırdan küçük ise hata mesajı göster
        print("Negatif sayılar kullanılamaz")


# Dereceden, radiana dönüşüm
def derece2rad(aci):
    """Derece cinsinden verilen çıyı, radian'a dönüştürür
        pi => 180
    """
    # Verilen açıyı pi ile çarpıp, 180 değerine bölüp, döndür
    return aci * 3.141592 / 180


# Radiandan, dereceye dönüşüm
def rad2derece(aci):
    """Radian cinsinden verilen çıyı, derece'ye dönüştürür
            180 => pi
        """
    # Verilen açıyı 180 ile çarpıp, pi değerine bölüp, döndür
    return aci * 180 / 3.141592


# Sinüs hesabı
def sin(aci):
    """Derece cinsinden verilen açının sinüs değerini hesaplar
    https://en.wikipedia.org/wiki/Trigonometric_functions#Power_series_expansion
    """
    # Derece cinsinden verile acçıyı, radiana çevir
    aci = derece2rad(aci)
    # sonuc değişkenine 0 ata
    sonuc = 0
    # 0 ile 24 arasında bir döngü oluştur. 0, 1, 2, ..., 22, 23, 24
    for i in range(25):
        # i. tek sayısı hesapla: 1, 3, 5, 7 ... , 45, 47, 49
        tek_sayi = 2 * i + 1
        # i çift ise 1, tek ise -1 oluştur. 1, -1, 1, ..., 1, -1 , 1
        isaret = pow(-1, i)
        # Wikipedia sayfasındaki sinüs hesabındaki serinin i. elemanını hesapla
        deger = isaret * pow(aci, tek_sayi) / faktoriyel(tek_sayi)
        # Hesaplanan i. elemanı sonuc ile topla
        sonuc += deger

    # Sonucu döndür
    return sonuc


# Sinuüs 45'i hesapla. 1 / sqrt(2) olmalı
print(sin(45))
# 1 / sqrt(2)'yi göster. Denetlemek için
print(1 / pow(2, 0.5))
