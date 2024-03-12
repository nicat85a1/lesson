"""
# Nested Loops / for loops w3schools / tekrarlı permutasyon

rakamlar = [1, 2, 3]
for saygac1 in rakamlar:
    for saygac2 in rakamlar:
        for saygac3 in rakamlar:
            print([saygac1, saygac2, saygac3])
"""

# Recursion

rakamlar = [1, 2, 3, 4]
def forinfor(döngü, mevcut_döngü=0, mevcut_sonuç=[]):
    if mevcut_döngü < döngü:
        for saygac in rakamlar:
            forinfor(döngü, mevcut_döngü + 1, mevcut_sonuç + [saygac])
    else:
        print(mevcut_sonuç)
forinfor(len(rakamlar))