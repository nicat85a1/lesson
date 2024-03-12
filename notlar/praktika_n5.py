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

reqem1 = int(input("Birinci ededi daxil edin: "))
reqem2 = int(input("Ikinci ededi daxil edin: "))
if (10 <= reqem1 <= 20 and reqem1 % 2 == 0) or (10 <= reqem2 <= 20 and reqem2 % 2 == 0):
    print("True")
else:
    print("False")

cüt = 0
for i in range(10, 20+1):
    if i % 2 == 0:
        cüt = cüt + 1
print("10 ilə 20 arasında", cüt, "cüt ədəd var.")