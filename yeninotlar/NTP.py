"""
class dusman:
    kalan_can = 3
    def saldir(self):
        print("hucum")
        self.kalan_can -= 1
    def hayattami(self):
        if self.kalan_can <= 0:
            print("düşman öldü")
        else:
            print(str(self.kalan_can) + "cani kaldi")

dusman1 = dusman()
dusman2 = dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayattami()

dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayattami()
"""
"""
class dusman:
    def __init__(self,name = "dusman",kalan_can = 500,saldiri_gucu = 10,mermi_sayisi=20):
        self.isim = name
        self.kalancan = kalan_can
        self.saldirigucu = saldiri_gucu
        self.mermisayisi = mermi_sayisi
    def print(self):
        print("basiliyor")
        print("ism",self.isim,"kalancan",self.kalancan,"saldirigucu",self.saldirigucu,"mermisayisi",self.mermisayisi)
    
dusman1 = dusman("ali",2000,30,40)
dusman2 = dusman("veli",1000,20,30)
dusman3 = dusman()

print("dusman1 ----------------------")
dusman1.print()

print("dusman2 ----------------------")
dusman2.print()

print("dusman3 ----------------------")
dusman3.print()
"""
import random
class dusman:
    def __init__(self,name = "dusman",kalan_can = 500,saldiri_gucu = 10,mermi_sayisi=20):
        self.isim = name
        self.kalancan = kalan_can
        self.saldirigucu = saldiri_gucu
        self.mermisayisi = mermi_sayisi

    def saldir(self):
        print(self.isim,"saldiriyor")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi)+" mermi harcandi")
        self.mermisayisi -= harcanan_mermi

        return harcanan_mermi,self.saldirigucu
    
    def saldiri_gucu(self,harcanan_mermi,saldirigucu):
        print(self.isim,"vuruldum")
        self.kalancan -= (harcanan_mermi * saldirigucu)
    
    def mermi_bitti(self):
        if self.mermisayisi <= 0:
            print(self.isim,"mermisi bitti")
            return True
        return False
    
    def hayatta_mi(self):
        if self.kalancan <=0:
            print(self.isim,"hayatta degil")

    def print(self):
        print("basiliyor")
        print("ism",self.isim,"kalancan",self.kalancan,"saldirigucu",self.saldirigucu,"mermisayisi",self.mermisayisi)

dusmanlar = []

i = 0

while i < 10:
    rastgele_can = random.randrange(100,200)
    rastgele_saldirigucu = random.randrange(10,20)
    rastgele_mermisayisi = random.randrange(20,30)
    yenidusman = dusman("dusman"+str(i+1),rastgele_can,rastgele_saldirigucu,rastgele_mermisayisi)
    dusmanlar.append(yenidusman)

    i += 1

i = 0
while i < 3:
    random_dusman1 = random.randrange(0,10)
    random_dusman2 = random.randrange(0,10)

    donendeger = dusmanlar[random_dusman1].saldir()
    dusmanlar[random_dusman2].saldiri_gucu(donendeger[0],donendeger[1])

    print("raund bitti")

    i += 1