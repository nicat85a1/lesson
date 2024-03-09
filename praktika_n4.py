"""
# task 1 +

listcem= [2, 3, 4, 5]
toplam=0
for sayi in listcem:
   toplam+=sayi
print(toplam)

hasil=1
for sayi in listcem:
   hasil*=sayi
print(hasil)

# task 2 +

listsira = [2,4,5,9]
listsira.reverse()
print(listsira)

# task 3 +

list1 = ["sa","sa","sa"]
list2 = ["lam","lam","lam"]
listzip = zip(list1,list2)
bosluk = tuple((a + b,) for a, b in listzip)
print(bosluk)

# task 4 +

a = [5,7,["aplle","gilas","heyva"]]
a[2][2]="gül"
print(a)

# task 5 +

listindexx = [1,2,3,4,5]
listindexx[2]=2
print(listindexx)

# tas 6 +

listorta = [1,2,3,4,5,6,7,8,9,10]
toplam=0
for sayi in listorta:
   toplam+=sayi
print(toplam/len(listorta))

# task 7 +

reqem1 = int(input("reqem1: "))
reqem2 = int(input("reqem2: "))

cüt = []
tək = []

for reqem in range(reqem1, reqem2 + 1):
    if reqem % 2 == 0:
        cüt.append(reqem)
    else:
        tək.append(reqem)

print(f"Cüt: {cüt}")
print(f"Tək: {tək}")
print(f"Cüt rəqəmlərin sayı: {len(cüt)}")

# task 8 +

listtekrar = [1,2,2,4,4,6,6,8,8,10]
print(set(listtekrar))

# task 11 +

i = 0

while i < 10 :
    print("i",i) # döngüler
    i = i + 2 # i+=2 # i*=2 ve s. da kullanabilirsin
"""

"""
# task 10
a = {'a': ['Fuad', 'Ali', 'Orxan']}
secim = input("(1) Elave et (2) Sil:")
if secim == "1":
    ad = input("Ad:")
    if ad == "":
        print("Ad bos ola bilmez")
    elif ad in a["a"]:
        print("Bu ad artiq movcuddur",a)
    else:
        a["a"].append(ad)
        print("Ad elave olundu",a)
elif secim == "2":
    ad = input("Ad:")
    if ad == "":
        print("Ad bos ola bilmez")
    elif ad not in a["a"]:
        print("Bu ad movcud deyil",a)
    else:
        a["a"].remove(ad)
        print("Ad silindi",a)
"""
# task 9
"""
rakamlar = [1, 2, 3]

# Kombinasyon bulmak için bir fonksiyon
def kombinasyon_bul(rakamlar):
    for i in range(len(rakamlar)):
        for j in range(i+1, len(rakamlar)):
            for k in range(j+1, len(rakamlar)):
                print(rakamlar[i], rakamlar[j], rakamlar[k])

kombinasyon_bul(rakamlar)

###

rakamlar = [1, 2, 3]

# permütasyon bulmak için bir fonksiyon
def permütasyon_bul(rakamlar):
    for i in rakamlar:
        for j in rakamlar:
            for k in rakamlar:
                if i != j and j != k and i != k:
                    print(i, j, k)
print(permütasyon_bul(rakamlar))

###

rakamlar = [1, 2, 3]   # 3^3

# Tekrarlı permütasyon bulmak için bir fonksiyon
def tekrarli_permütasyon_bul(rakamlar):
    for i in rakamlar:
        for j in rakamlar:
            for k in rakamlar:
                print(i, j, k)

tekrarli_permütasyon_bul(rakamlar)
"""

# backtracking

def permutasyon_yazdir(liste, baslangic, son):
    # liste: permutasyonlarını yazdırmak istediğimiz liste
    # baslangic: permutasyonun başladığı indeks
    # son: permutasyonun bittiği indeks
    if baslangic == son: # permutasyon tamamlandıysa
        print(liste) # liste yazdır
    else:
        for i in range(baslangic, son + 1): # her bir eleman için
            liste[baslangic], liste[i] = liste[i], liste[baslangic] # elemanı başa getir
            permutasyon_yazdir(liste, baslangic + 1, son) # geri kalan elemanların permutasyonlarını bul
            liste[baslangic], liste[i] = liste[i], liste[baslangic] # elemanı eski yerine geri koy

rakamlar = [1, 2, 3]
permutasyon_yazdir(rakamlar, 0, len(rakamlar) - 1)