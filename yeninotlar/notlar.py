# print(*range(10))
"""
# hatalı kod

i = 0

while i < 10:
    if i == 2:
        continue
    i+=1
    print(i) # sonsuz döngü
"""
"""
def topla(liste):
      if (len(liste)) == 0:
            return 0
      else:
            return liste[0] + (topla(liste[1:]))
 # 1. return 1 + topla (2,3,4)
 # 2. return 2 + topla (3,4)
 # 3. return 3 + topla (4)
 # 4. return 4 + topla ()
 # 5. return 0
 # 1 + (2 +(3 + (4 + ())

print(topla([1,2,3,4]))
"""
"""
a=10
def harf():
    global a # globaldaki veriyi değiştir
    a=2
    print(a)
harf()
print(a)
"""
"""
def harf():
    a=2
    b=5
    return a # return b
print(harf())
"""
"""
import modul1

modul1.selamla()
"""
"""
try:
    dosya = open("deneme.txt","r")
except:
    print("hata")
finally:
    dosya.close()
"""
"""
dosya = open("deneme.txt","r")

dosya.read() # hepsini alır

dosya.readline() # satırı alır

dosya.readlines() # satırı liste olarak hepsini alır
"""
# önerilen

"""
with open("deneme.txt","r") as dosya:
    print(dosya.read())
"""