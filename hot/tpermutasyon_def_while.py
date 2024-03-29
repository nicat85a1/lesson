"""
# Recursion tekrarlı permutasyon

rakamlar = [1, 2, 3, 4]
def forinfor(döngü, mevcut_döngü=0, mevcut_sonuç=[]):
    if mevcut_döngü < döngü:
        for saygac in rakamlar:
            forinfor(döngü, mevcut_döngü + 1, mevcut_sonuç + [saygac])
    else:
        print(mevcut_sonuç)
forinfor(len(rakamlar))

# while tekrarlı permutasyon

rakamlar = [1, 2, 3, 4]
döngü_sayısı = len(rakamlar)
indeksler = [0] * döngü_sayısı
while indeksler[0] < döngü_sayısı:
    sonuç = [rakamlar[indeks] for indeks in indeksler]
    print(sonuç)
    indeksler[-1] += 1
    for i in range(döngü_sayısı - 1, 0, -1):
        if indeksler[i] == döngü_sayısı:
            indeksler[i] = 0
            indeksler[i-1] += 1
"""