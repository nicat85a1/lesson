"""
a = "python  "
b = "programlama "
c = "dili"
e = [1,2,3,4,5,6,7]

d = a + b + c

print(d) # python  programlama dili
print(a * 4)  # python python python python
print(a[0]) # p
print(len(a)) # 8
print(len(e)) # 7
"""

"""
a = "python"
print(a[len(a)-1]) # son eleman / n
print(a[0:2]) # ilk iki karakter / py
print(a[:2]) # ilk 2 harf / 2 e kadar / py
print(a[2:]) # sonraki / 2 den sonra / thon
print(a[-3:-1]) # sonrakilerden once önceki 3 harf / ho
print(a[0:6:2]) # her ikisi değil 2 adımla / pto
"""
"""
a = {"elma": 12,"armut": 15,"karpuz": 20}
print(a["elma"] ) # elma için değeri getir / 12
"""
"""
print(a["çilek"]) # yoksa hata ver / KeyError
"""
"""
yaş = input ("Yaşınızı girin")
print("Yaşınız", yaş) # Yaşınız 30
"""
"""
a = int (input ("a:")) # int eklemezsen input string olarak alır ve hata verir.
b = int (input ("b:")) # int float da olabilir (tam olmayan sayı)
c = int (input ("c:"))
print("Toplam", a+b+c)
"""
"""
yaş = int (input ("Yaşınızı girin")) # koşullar
if yaş < 18 :
    print("Yaşınız 18'den küçük")
else :
    print("Yaşınız 18'den büyük") # if çalışmazsa
"""
"""
yaş = int (input ("Yaşınızı girin"))
if yaş == 18 :
    print("Yaşınız 18")
elif yaş == 19 :
    print("Yaşınız 19") # birden fazla koşul varsa elif gönderiliriz
elif yaş == 20 :
    print("Yaşınız 20")
else:
    print("uygun degil")
"""
"""
i = 0

while i < 10 :
    print("i",i) # döngüler
    i = i + 2 # i+=2 # i*=2 ve s. da kullanabilirsin
"""
"""
i = 0
while (i < 10) :
    if i == 5 :
        break
    print("i",i) # döngü sonlandırmak için kullanabiliriz (5de)
    i = i + 1
"""
"""
i = 0
while (i < 10) :
    if i == 3 or i == 5 :
        i = i + 1 # örneğin bu satır olmaz ise döngü bitmez. (sonsuzdöngü/hatalı kod önleme).
        continue
    print("i",i)
    i = i + 1
"""
"""
a = [1,2,3,4,5,6] # ve ya b = "python"
for eleman in a :
    print(eleman) # for döngüsü
"""
"""
for sayi in range(20,30) : # 20-29
    print(sayi)  # range() fonskiyonu
"""
"""
for sayi2 in range(20,30,2) : # 20-28
    print(sayi2)
    """
# bölüm 2 bitti

a = [1,2,3,4,5,6] # ve ya b = "python"
for eleman in a :
    print(eleman) # for döngüsü