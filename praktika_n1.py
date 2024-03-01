# task 1
"""
from datetime   # sadece saat

current_time=datetime.datetime.now()
month_time=current_time.time()
print(month_time)

from datetime import datetime

a = datetime.now() # tarix ve saat
print(a)

# task 2

# toplama
def topla(x, y):
    return x + y

# çıxma
def çıx(x, y):
    return x - y

# vurma
def vur(x, y):
    return x * y

# bölme
def böl(x, y):
    return x / y


print("işlemi seç.")
print("1.topla")
print("2.çıx")
print("3.vur")
print("4.böl")

while True:
    # kullanıcıdan işlemi al
    islemler = input("işlemi seç(1/2/3/4): ")

    # işlemi doğrula
    if islemler in ('1', '2', '3', '4'):
        try:
            b = float(input("1ci reqem: "))
            c = float(input("2ci reqem: "))
        except ValueError:
            print("sayı girin")
            continue

        if islemler == '1':
            print(b, "+", c, "=", topla(b, c))

        elif islemler == '2':
            print(b, "-", c, "=", çıx(b, c))

        elif islemler == '3':
            print(b, "*", c, "=", vur(b, c))

        elif islemler == '4':
            print(b, "/", c, "=", böl(b, c))

        hesplamaya_devam = input("davam? (yes/no): ")
        if hesplamaya_devam == "no":
          break
    else:
        print("seçim")

# task 3

user_name = str (input ("user name:"))
user_surname = str (input ("user surname:"))
print ("salam", user_name, user_surname, "xoş gəlmisiz")

# task 4

from datetime import date

d = date.today() # tarix
print(d)

# task 5

e = int (input ("e:"))

if e %2==0:
    print("cift ededdir")
else:
    print("tekdir")

# task 6
    
f = int (input ("f:"))
g = int (input ("g:"))
h = int (input ("h:"))

if f>g and f>h:
    print("en buyuk eded", f)
elif g>f and g>h:
    print("en buyuk eded", g)
else:
    h>f and h>g
    print("en buyuk eded", h)

"""
# task 7

isim = str (input ("isim:"))
parol = str (input ("parol:"))
if isim == "" and parol == "12345":
    print("login girmemisiz")
elif isim == "nesib" and parol == "":
    print("parol girmemisiz")
elif isim == "" and parol == "":
    print("login ve parol girmemisiz")
elif isim == "nesib" and parol == "12345":
    print("xosh geldiniz")
elif isim != "nesib" and parol == "12345":
    print("login yanlisdir")
elif isim == "nesib" and parol != "12345":
    print("parol yanlisdir")
elif isim != "nesib" and parol != "12345":
    print("login ve parol yanlisdir")
