import pygame
import math

# baleci stickman

# Pygame'ı başlat
pygame.init()

# Pencereyi oluştur
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Hareket Eden İnsan')

ekran_genisligi = 1500
ekran_yuksekligi = 800

# Renkleri tanımla
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# İnsan figürünün başlangıç konumunu ayarla
insan_x = 100
insan_y = 500

# İnsan figürü boyutlarını ayarla
kafa_radius = 20
govde_uzunlugu = 70
kol_uzunlugu = 70
bacak_uzunlugu = 90
diz_uzunlugu = bacak_uzunlugu / 2

# Gözlerin boyutlarını ve konumunu ayarla
goz_radius = 5
goz_mesafesi = 10  # Kafa merkezinden gözlere olan yatay mesafe

# Animasyon değişkenlerini ayarla
kol_animasyonu = 0
bacak_animasyonu = 0
diz_animasyonu = 0
animasyon_hizi = 5
kol_hareket_yonu = 1
bacak_hareket_yonu = 1
diz_hareket_yonu = 1

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
maksimum_ziplama_sayisi = 2

# Yürüme yönünü takip etmek için değişken
yurume_yonu = 'sag'  # Varsayılan yön sağdır

# Yüz ve gözlerin yönünü belirlemek için değişkenler
yuz_yonu = 'sag'
kol_yonu = 1
bacak_yonu = 1

sol_kol_animasyonu = 0
z_tusu_basildi = False
sag_kol_animasyonu = 0
x_tusu_basildi = False

# Oyun döngüsünü çalıştır
running = True
while running:
    # Olayları işle

    if insan_x > ekran_genisligi:
        insan_x = 0
    elif insan_x < 0:
        insan_x = ekran_genisligi

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
            if event.key == pygame.K_UP:
                if ziplama_sayisi < maksimum_ziplama_sayisi:
                    ziplama_durumu = True
                    ziplama_yuksekligi = -15
                    ziplama_sayisi += 1
            if event.key == pygame.K_z:
                sol_kol_animasyonu = 100
                z_tusu_basildi = True
            if event.key == pygame.K_x:
                sag_kol_animasyonu = 280
                x_tusu_basildi = True
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False
            if event.key == pygame.K_z:
                sol_kol_animasyonu = 0
                z_tusu_basildi = False
            if event.key == pygame.K_x:
                sag_kol_animasyonu = 0
                x_tusu_basildi = False

    # Tuş basılı durumunu kontrol et ve karakteri hareket ettir
    if keys_pressed[pygame.K_LEFT]:
        yurume_yonu = 'sol'
        yuz_yonu = 'sol'
        kol_yonu = -1
        bacak_yonu = -1
        insan_x -= 10
        kol_animasyonu += (animasyon_hizi * kol_hareket_yonu)
        bacak_animasyonu += (animasyon_hizi * bacak_hareket_yonu)
        diz_animasyonu += (animasyon_hizi * diz_hareket_yonu)
        if kol_animasyonu > 35 or kol_animasyonu < -35:
            kol_hareket_yonu *= -1
        if bacak_animasyonu > 25 or bacak_animasyonu < -25:
            bacak_hareket_yonu *= -1
        if diz_animasyonu > 15 or diz_animasyonu < -15:
            diz_hareket_yonu *= -1

    if keys_pressed[pygame.K_RIGHT]:
        yurume_yonu = 'sag'
        yuz_yonu = 'sag'
        kol_yonu = 1
        bacak_yonu = 1
        insan_x += 10
        kol_animasyonu += (animasyon_hizi * kol_hareket_yonu)
        bacak_animasyonu += (animasyon_hizi * bacak_hareket_yonu)
        diz_animasyonu += (animasyon_hizi * diz_hareket_yonu)
        if kol_animasyonu > 35 or kol_animasyonu < -35:
            kol_hareket_yonu *= -1
        if bacak_animasyonu > 25 or bacak_animasyonu < -25:
            bacak_hareket_yonu *= -1
        if diz_animasyonu > 15 or diz_animasyonu < -15:
            diz_hareket_yonu *= -1

    # Zıplama durumunu kontrol et
    if ziplama_durumu:
        insan_y += ziplama_yuksekligi
        ziplama_yuksekligi += 1
        if insan_y > orijinal_y:
            insan_y = orijinal_y
            ziplama_durumu = False
            ziplama_yuksekligi = 60
            ziplama_sayisi = 0

    # Ekranı temizle
    screen.fill(BLACK)

    # Kafa
    pygame.draw.circle(screen, WHITE, (insan_x, insan_y), kafa_radius)

    # Gözler (Yürüme yönüne göre)
    if yuz_yonu == 'sag':
        goz_sol_x = insan_x + goz_mesafesi
        goz_sag_x = insan_x + goz_mesafesi * 2
    else:
        goz_sol_x = insan_x - goz_mesafesi
        goz_sag_x = insan_x - goz_mesafesi * 2

    pygame.draw.circle(screen, BLUE, (goz_sol_x, insan_y - 5), goz_radius)
    pygame.draw.circle(screen, BLUE, (goz_sag_x, insan_y - 5), goz_radius)

    # Gövde
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius), (insan_x, insan_y + kafa_radius + govde_uzunlugu), 2)

    # Kollar (Yürüme yönüne göre)
    if z_tusu_basildi:
        # Z tuşuna basıldığında çalışacak kod
        sol_kol_acisi = math.radians(sol_kol_animasyonu * kol_yonu)
    else:
        # Z tuşuna basılmadığında çalışacak kod
        sol_kol_acisi = math.radians(kol_animasyonu * kol_yonu)
    if x_tusu_basildi:
        # Z tuşuna basıldığında çalışacak kod
        sag_kol_acisi = math.radians(sag_kol_animasyonu * kol_yonu)
    else:
        # Z tuşuna basılmadığında çalışacak kod
        sag_kol_acisi = math.radians(kol_animasyonu * kol_yonu)
    sol_kol_x = insan_x + kol_uzunlugu * math.sin(sol_kol_acisi)
    sag_kol_x = insan_x - kol_uzunlugu * math.sin(sag_kol_acisi)
    sol_kol_y = insan_y + kafa_radius + kol_uzunlugu * math.cos(sol_kol_acisi)
    sag_kol_y = insan_y + kafa_radius + kol_uzunlugu * math.cos(sag_kol_acisi)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius), (sol_kol_x, sol_kol_y), 2)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius), (sag_kol_x, sag_kol_y), 2)

    # Bacaklar (Yürüme yönüne göre)
    bacak_acisi = math.radians(bacak_animasyonu * bacak_yonu)
    diz_acisi = math.radians(diz_animasyonu * bacak_yonu)

    # Üst bacak
    sol_ust_bacak_x = insan_x + diz_uzunlugu * math.sin(bacak_acisi)
    sol_ust_bacak_y = insan_y + kafa_radius + govde_uzunlugu + diz_uzunlugu * math.cos(bacak_acisi)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius + govde_uzunlugu), (sol_ust_bacak_x, sol_ust_bacak_y), 2)
    # Alt bacak
    sol_alt_bacak_x = sol_ust_bacak_x + diz_uzunlugu * math.sin(diz_acisi)
    sol_alt_bacak_y = sol_ust_bacak_y + diz_uzunlugu * math.cos(diz_acisi)
    pygame.draw.line(screen, WHITE, (sol_ust_bacak_x, sol_ust_bacak_y), (sol_alt_bacak_x, sol_alt_bacak_y), 2)

    # Üst bacak
    sag_ust_bacak_x = insan_x - diz_uzunlugu * math.sin(bacak_acisi)
    sag_ust_bacak_y = insan_y + kafa_radius + govde_uzunlugu + diz_uzunlugu * math.cos(bacak_acisi)
    pygame.draw.line(screen, WHITE, (insan_x, insan_y + kafa_radius + govde_uzunlugu), (sag_ust_bacak_x, sag_ust_bacak_y), 2)
    # Alt bacak
    sag_alt_bacak_x = sag_ust_bacak_x - diz_uzunlugu * math.sin(diz_acisi)
    sag_alt_bacak_y = sag_ust_bacak_y + diz_uzunlugu * math.cos(diz_acisi)
    pygame.draw.line(screen, WHITE, (sag_ust_bacak_x, sag_ust_bacak_y), (sag_alt_bacak_x, sag_alt_bacak_y), 2)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS'i sınırla
    pygame.time.Clock().tick(60)

# Pygame'ı kapat
pygame.quit()