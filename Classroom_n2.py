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
    print("i",i)
    i = i + 2

# task 12 +
say = 6
sıra = 0
for i in range(say):
  sıra += 1
  print(sıra,"Java")

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
"""
# task 9

combination = [1, 2, 3]
print(combination) # :p

# Nested Loops / for loops w3schools / tekrarlı permutasyon
rakamlar = [1, 2, 3]
for saygac1 in rakamlar:
    for saygac2 in rakamlar:
        for saygac3 in rakamlar:
            print([saygac1, saygac2, saygac3])

# Nested Loops / for loops w3schools / permutasyon
rakamlar1 = [1, 2, 3]
permutasyonlar = []

for saygac4 in rakamlar1:
    for saygac5 in rakamlar1:
        for saygac6 in rakamlar1:
            if saygac4 != saygac5 and saygac4 != saygac6 and saygac5 != saygac6:
                permutasyonlar.append([saygac4, saygac5, saygac6])
print(permutasyonlar)

# Backtracking ile permutasyon

rakamlar = [1, 2, 3]
print(rakamlar)
for i in range(3):
    rakamlar[1], rakamlar[2] = rakamlar[2], rakamlar[1]
    print(rakamlar)
    if rakamlar[0] == 3 and rakamlar[2] == 1:
        break
    rakamlar[0], rakamlar[2] = rakamlar[2], rakamlar[0]
    print(rakamlar)
    """