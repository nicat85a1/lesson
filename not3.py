"""
def selamla():
    print("Selam")
    print("naber ?")

selamla() # def fonksyonu selam naber?
selamla()
selamla()
"""
"""
def selamla(isim):
    print("Merhaba", isim)

selamla("Ali")
selamla("Veli") # Merhaba Ali Merhaba Veli
"""
"""
def selamla(isim = "isimsiz"):
    print("Merhaba", isim)

selamla("Ali")
selamla("Veli")
selamla() # Merhaba Ali Merhaba Veli Merhaba isimsiz
"""
"""
def toplama (a,b,c):
    print("Toplam:",a+b+c)

toplama(10,20,30)
toplama(100,200,300) # Toplam: 60 Toplam: 600
"""
"""
def toplama (a,b,c):
    print("Toplam:",a+b+c)
a = toplama(3,4,5)
print("a:",a) # hatalı kod a: None olur. output/çıktı olmadığı için / sadece değer yazdırır.
"""
"""
def toplama (a,b,c):
    return a+b+c # output için return kullan
toplam = toplama(3,4,5)
print(toplam)
"""
"""
liste = [1,2,3,4,5,6]
a = "araba"
print(a.startswith("a")) # True a ile başlıyo
print(a.startswith("b")) # False
print(a.endswith("ba")) # True
print(a.replace("a","o")) # orobo
liste.append("Python") # print(liste.append("Python")) yazarsan None olur.
print(liste) # [1, 2, 3, 4, 5, 6, 'Python']
"""
"""
liste = [1,2,3,4,5,6]
liste.pop() # 6 yı siler. pop(0) olursa 1 i siler.
print(liste)
"""
# bölüm 3 bitti