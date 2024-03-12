# Recursion

rakamlar = [1, 2, 3, 4]

def forinfor(döngü, mevcut_döngü=0, mevcut_sonuç=[]):
    if mevcut_döngü < döngü:
        for saygac in rakamlar:
            forinfor(döngü, mevcut_döngü + 1, mevcut_sonuç + [saygac])
    else:
        print(mevcut_sonuç)

forinfor(len(rakamlar))