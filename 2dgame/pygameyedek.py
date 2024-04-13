"""import pygame
import math

# Pygame'ı başlat
pygame.init()

# Ekran boyutlarını ayarla
ekran_genisligi = 1500
ekran_yuksekligi = 800
screen = pygame.display.set_mode((ekran_genisligi, ekran_yuksekligi))"""

"""# Gökkuşağı renklerini, yüksekliklerini ve genişliklerini tanımla
gokkusagi_renkleri_ve_boyutlari = [
    ((148, 0, 211), 110, ekran_genisligi * 0.4),  # Mor
    ((75, 0, 130), 110, ekran_genisligi * 0.5),   # Çivit
    ((0, 0, 255), 110, ekran_genisligi * 0.6),     # Mavi
    ((0, 255, 0), 110, ekran_genisligi * 0.7),     # Yeşil
    ((255, 255, 0), 110, ekran_genisligi * 0.8),   # Sarı
    ((255, 127, 0), 110, ekran_genisligi * 0.9),   # Turuncu
    ((255, 0, 0), 110, ekran_genisligi)      # Kırmızı
]

# Gökkuşağı çizim fonksiyonu
def ciz_gokkusagi():
    yukseklik_toplami = sum(yukseklik for _, yukseklik, _ in gokkusagi_renkleri_ve_boyutlari)
    baslangic_y = (screen.get_height() - yukseklik_toplami) // 2
    for renk, yukseklik, genislik in gokkusagi_renkleri_ve_boyutlari:
        pygame.draw.rect(screen, renk, ((ekran_genisligi - genislik) // 2, baslangic_y, genislik, yukseklik))
        baslangic_y += yukseklik"""

"""def renkleri_donustur():
    global gokkusagi_renkleri_ve_boyutlari
    renkler = [renk for renk, _, _ in gokkusagi_renkleri_ve_boyutlari]
    renkler.insert(0, renkler.pop())  # Listenin sonundaki rengi al ve başa ekle
    for i, (_, yukseklik, genislik) in enumerate(gokkusagi_renkleri_ve_boyutlari):
        gokkusagi_renkleri_ve_boyutlari[i] = (renkler[i], yukseklik, genislik)"""
        #renkleri_donustur()
    #ciz_gokkusagi()

import pygame
import math

# Pygame'ı başlat
pygame.init()

# Pencereyi oluştur
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Hareket Eden İnsan')

# Renkleri tanımla
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# İnsan figürünün başlangıç konumunu ayarla
insan_x = 100
insan_y = 500

# İnsan figürü boyutlarını ayarla
kafa_radius = 20
govde_uzunlugu = 70
kol_uzunlugu = 70
bacak_uzunlugu = 90

# Animasyon değişkenlerini ayarla
kol_animasyonu = 0
bacak_animasyonu = 0
animasyon_hizi = 5
kol_hareket_yonu = 1  # 1 ileri, -1 geri
bacak_hareket_yonu = 1  # 1 ileri, -1 geri

# Zıplama değişkenlerini ayarla
ziplama_durumu = False
ziplama_yuksekligi = 60
orijinal_y = insan_y

# Tuşların basılı durumunu takip etmek için sözlük
keys_pressed = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False
}

# Çift zıplama değişkenlerini ayarla
ziplama_sayisi = 0
maksimum_ziplama_sayisi = 2  # Maksimum zıplama sayısı

# Oyun döngüsünü çalıştır
running = True
while running:
    # Olayları işle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
            # Zıplama tuşuna basıldığında zıplama durumunu etkinleştir
            if event.key == pygame.K_UP:
                if ziplama_sayisi < maksimum_ziplama_sayisi:
                    ziplama_durumu = True
                    ziplama_yuksekligi = -15  # Zıplama hızı
                    ziplama_sayisi += 1
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    # Zıplama durumunu kontrol et
    if ziplama_durumu:
        insan_y += ziplama_yuksekligi  # Y pozisyonunu güncelle
        ziplama_yuksekligi += 1  # Yerçekimi etkisi
        if insan_y > orijinal_y:
            insan_y = orijinal_y
            ziplama_durumu = False
            ziplama_yuksekligi = 60
            ziplama_sayisi = 0  # Zıplama sayısını sıfırla

    # Tuş basılı durumunu kontrol et ve karakteri hareket ettir
    if keys_pressed[pygame.K_LEFT]:
        insan_x -= 10
        kol_animasyonu += (animasyon_hizi * kol_hareket_yonu)
        bacak_animasyonu += (animasyon_hizi * bacak_hareket_yonu)
        if kol_animasyonu > 35 or kol_animasyonu < -35:
            kol_hareket_yonu *= -1
        if bacak_animasyonu > 25 or bacak_animasyonu < -25:
            bacak_hareket_yonu *= -1

    if keys_pressed[pygame.K_RIGHT]:
        insan_x += 10
        kol_animasyonu += (animasyon_hizi * kol_hareket_yonu)
        bacak_animasyonu += (animasyon_hizi * bacak_hareket_yonu)
        if kol_animasyonu > 35 or kol_animasyonu < -35:
            kol_hareket_yonu *= -1
        if bacak_animasyonu > 25 or bacak_animasyonu < -25:
            bacak_hareket_yonu *= -1

    # Ekranı temizle
    screen.fill(BLACK)

    # Kafa
    pygame.draw.circle(screen, WHITE, (insan_x, insan_y), kafa_radius)

    # Gövde
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius), (insan_x, insan_y + kafa_radius + govde_uzunlugu), 2)

    # Kollar (Yürüme animasyonu)
    kol_acisi = math.radians(kol_animasyonu)
    sol_kol_x = insan_x + kol_uzunlugu * math.sin(kol_acisi)
    sag_kol_x = insan_x - kol_uzunlugu * math.sin(kol_acisi)
    sol_kol_y = insan_y + kafa_radius + kol_uzunlugu * math.cos(kol_acisi)
    sag_kol_y = insan_y + kafa_radius + kol_uzunlugu * math.cos(kol_acisi)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius), (sol_kol_x, sol_kol_y), 2)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius), (sag_kol_x, sag_kol_y), 2)

    # Bacaklar (Yürüme animasyonu)
    bacak_acisi = math.radians(bacak_animasyonu)
    sol_bacak_x = insan_x + bacak_uzunlugu * math.sin(bacak_acisi)
    sag_bacak_x = insan_x - bacak_uzunlugu * math.sin(bacak_acisi)
    sol_bacak_y = insan_y + kafa_radius + govde_uzunlugu + bacak_uzunlugu * math.cos(bacak_acisi)
    sag_bacak_y = insan_y + kafa_radius + govde_uzunlugu + bacak_uzunlugu * math.cos(bacak_acisi)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius + govde_uzunlugu), (sol_bacak_x, sol_bacak_y), 2)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius + govde_uzunlugu), (sag_bacak_x, sag_bacak_y), 2)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS'i sınırla
    pygame.time.Clock().tick(60)

# Pygame'ı kapat
pygame.quit()