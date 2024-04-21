import pygame
import sys

# Pygame'ı başlat
pygame.init()

# Ekran boyutlarını ayarla
width, height = 1500, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('İki Hareketli Daire')

# Renkleri tanımla
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# İlk daire özelliklerini ayarla
circle1_pos = [width // 2, height // 2]  # Dairenin başlangıç pozisyonu
circle1_radius = 20  # Dairenin yarıçapı
circle1_speed = 2  # Dairenin hızı
direction1 = 1  # Dairenin hareket yönü (1: sağa, -1: sola)

# İkinci daire özelliklerini ayarla
circle2_pos = [width // 4, height // 2]  # Dairenin başlangıç pozisyonu
circle2_radius = 20  # Dairenin yarıçapı
circle2_speed = 2  # Dairenin hızı
direction2 = 1  # Dairenin hareket yönü (1: yukarı, -1: aşağı)

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # İlk dairenin pozisyonunu güncelle
    circle1_pos[0] += circle1_speed * direction1  # X pozisyonunu güncelle
    if circle1_pos[0] > width - circle1_radius or circle1_pos[0] < circle1_radius:
        direction1 *= -1  # Yönü değiştir

    # İkinci dairenin pozisyonunu güncelle
    circle2_pos[1] += circle2_speed * direction2  # Y pozisyonunu güncelle
    if circle2_pos[1] > height - circle2_radius or circle2_pos[1] < circle2_radius:
        direction2 *= -1  # Yönü değiştir

    # Ekranı temizle
    screen.fill(WHITE)

    # Daireleri çiz
    pygame.draw.circle(screen, BLUE, circle1_pos, circle1_radius)
    pygame.draw.circle(screen, BLUE, circle2_pos, circle2_radius)

    # Ekranı güncelle
    pygame.display.flip()
    pygame.time.delay(10)

# Pygame'ı kapat
pygame.quit()
sys.exit()