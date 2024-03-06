import os
import re
import psutil
import shutil

# Bölümlerin isimlerini bir liste olarak tanımla
partitions = ["C:\\", "D:\\", "E:\\"]

# Toplam değerleri sıfırla
total_ssd = 0
used_ssd = 0
free_ssd = 0

# Her bir bölüm için disk kullanımını al ve toplama ekle
for partition in partitions:
    total, used, free = shutil.disk_usage(partition)
    total_ssd += total
    used_ssd += used
    free_ssd += free

print()
print("SSD Kullanımı:")

# Toplam değerleri GB cinsinden yazdır
print("Toplam SSD:", total_ssd // (2**30), "GB")
print("Kullanılan SSD:", used_ssd // (2**30), "GB")
print("Boş SSD:", free_ssd // (2**30), "GB")
print("SSD Kullanım Yüzdesi:", used_ssd / total_ssd * 100, "%")

# Sistem belleği kullanımı hakkında bir isimlendirilmiş demet döndür
memory = psutil.virtual_memory()
print()
print("Bellek Kullanımı:")

# Toplam RAM, kullanılabilir RAM, kullanılan RAM ve RAM kullanım yüzdesini yazdır
print("RAM Kullanım Yüzdesi:", memory.percent,"%")

# powercfg'nin tam yolunu belirtin (genellikle C:/Windows/System32/)
powercfg_path = 'C:/Windows/System32/'

# powercfg komutunu PATH'e ekleyin
os.environ['PATH'] = f"{powercfg_path};{os.environ['PATH']}"

# powercfg /batteryreport komutunu çalıştırın
os.system('powercfg /batteryreport')

dosya_adi = "C:/Users/user/Desktop/python/battery-report.html"

# Kapasite kelimesini arayalım
aranan_kelime = "CAPACITY"

# raporu oku
dosya = open(dosya_adi, "r")

# Satır numarasını tutmak için bir sayaç tanımlıyoruz
satir_no = 0

# Sayıları tutmak için boş bir liste tanımlıyoruz
sayilar = []

# Dosyadaki her satır için bir döngü başlatıyoruz
for satir in dosya:
    # Sayaç değişkenini bir artırıyoruz
    satir_no += 1
    # Satırda aranan kelime varsa
    if aranan_kelime in satir:
        # Satırı bölüyoruz
        parcalar = re.split(r"\b", satir)
        # Aranan kelime satırda varsa, indeksini buluyoruz
        if aranan_kelime in parcalar:
            indeks = parcalar.index(aranan_kelime)
            # Eğer parcalar listesinin boyutu yeterliyse, sayıyı alıyoruz
            if len(parcalar) >= indeks + 5:
                sayi = parcalar[indeks + 8] + parcalar[indeks + 10]
                # Sayıyı listeye ekliyoruz
                sayilar.append(sayi)
                # döngüden çıkıyoruz
            else:
                break
# Dosyayı kapıyoruz
dosya.close()

print()
print("pil durumu:")

# Sayıların listesini yazdırıyoruz
print(f"kapasite: {sayilar}")
# Bölen sayının sıfır olmadığını kontrol ediyoruz
if int(sayilar[1]) != 0:
    # İlk iki sayıyı birbirine bölüyoruz
    sonuc = int(sayilar[1]) / int(sayilar[0])
    sonuc = round(sonuc, 2)
    sonuc = sonuc * 100
    # Sonucu yazdırıyoruz
    print(f"Pil sağlığı: {sonuc} %")
else:
    # Bölen sayı sıfır ise hata mesajı veriyoruz
    print("Bölen sayı sıfır olamaz!")