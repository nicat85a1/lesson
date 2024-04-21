import cv2
import numpy as np
import pygame

# Pygame başlat
pygame.init()

# Ekran ayarları
screen_width, screen_height = 1500, 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Renk tanımlamaları
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Karakter nesnesi
class Character(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect.center = pos

# İki karakter nesnesi oluştur
character1 = Character(BLACK)
character2 = Character(BLACK)
all_sprites = pygame.sprite.Group(character1, character2)

# OpenCV ile videoyu yükle
cap = cv2.VideoCapture('deneyup.mp4')

# Dairenin merkezini takip etmek için kullanılacak renk aralığı
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # BGR'dan HSV'ye renk dönüşümü
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Belirtilen renk aralığındaki nesneleri maskele
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maske üzerinde konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # İki en büyük konturu bul
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]

    for i, contour in enumerate(contours):
        # Kontur alanını hesapla
        area = cv2.contourArea(contour)
        if area > 500:
            # Dairenin merkezini bul
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # İlk karakter için ilk konturu, ikinci karakter için ikinci konturu kullan
            if i == 0:
                character1.update(center)
            elif i == 1:
                character2.update(center)

    # Pygame ekranını güncelle
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Pygame olaylarını kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            exit()

# Videoyu serbest bırak ve OpenCV pencerelerini kapat
cap.release()
cv2.destroyAllWindows()