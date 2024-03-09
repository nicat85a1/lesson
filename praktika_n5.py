"""
# task 4

sayi = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(sayi)):
    karekok = int(sayi[i] ** 0.5)
    asal = True
    for bölen in range(2,karekok+1) :
        if (sayi[i] % bölen == 0) :
            asal = False
            break
    if asal:
        print (sayi[i],"asal sayıdır")
    else:
        print (sayi[i],"asal deyil")

# task 2

listorta = [1,2,3,4,5,6,7,8,9,10]
toplam=0
for sayi in listorta:
   toplam+=sayi
print(toplam//len(listorta))

# task 3

sayilar = (1,2,3,4,5,6,7,8,9,10)
for i in range(7+1):
    sayi=sayilar[i+1]*sayilar[i-1]
print(sayi)


# task 5

sayi = int(input("Bir sayı giriniz: "))
if sayi > 0:
    print("Girilen sayı musbetdir")
elif sayi < 0:
    print("Girilen sayı menfidir")
else:
    print("Girilen sayı sifirdir")
    """

# task 1

reqem1 = int(input("1. reqemi daxil edin: "))
reqem2 = int(input("2. reqemi daxil edin: "))