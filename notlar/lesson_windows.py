sayi = int(input("Bir sayı girin: ")) # kullanıcıdan sayıyı aldım
karekok = int(sayi ** 0.5) # sayının 0.5 katından (^0.5) sayının karekökünü bulabiliriz.
asal = True # asal olup olmadığını tutan bir değişken / yani boolean veri tipi kullan.
for bölen in range(2,karekok+1) : # 2 den kareköke kadar sayılara böl
    if (sayi % bölen == 0) : # eğer % yani qalıq 0'a beraberdirse, yani tam bölünürse
        asal = False # asal olmadığını belirle
        break # döngüden çık
# döngü bittikten sonra asal değişkenine göre yazdır
if asal:
    print ("asal sayıdır")
else:
    print ("asal deyil")