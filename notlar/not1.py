print ("python","py1","py2",15,"py8","19") # basit print
print ("python\npy1\npy2\n15\npy8\n19") # \n ile alt alta yazma
print ("03","09","2000", sep="/") # / ile ayırmak
print ("{} + {} = {}".format (2,3,2 + 3)) # süslü paranteze değer verme

"""
Yorumlar
"""

a = 3
b = 3.4
c = "Python"
d = [1,2,3,4,5,"python"]
e = (1,2,3,4,5,"python")
f = {"name":"Python","age":15}
g = True
h = False
print (type(a)) # int / integer / tam sayı
print (type(b)) # float / tam olmayan sayı
print (type(c)) # str / string / karakter dizisi
print (type(d)) # list / liste
print (type(e)) # tuple / kapsayıcı türlerden birinin farklı olduğunu gösterir ?
print (type(f)) # dict / dictionary / anahtar-değer çiftiyle tanımlanan veri yapısı
print (type(g)) # bool / boolean / doğru ya da yanlış olan değeri ifade eden temel veri tipi
print (type(h)) # bool

print(3+4) # matematik operatörleri / +
print(3-4) # -
print(3*4) # *
print(4/2) # /
print(10%3) # qalıq mod işlemi
print(4**2) # kuvvet
print(10//2.7) # // Tamsayı bölme / tam sayıdan sonrasını atar (# round fonksyonu ile yaklaştırma)
print(5>4) # > Büyük mü?
print(5<4) # < Küçük mü?
print(5==4) # == Eşittir mi?
print(5!=4) # != Eşit değil mi?
print(5<=4) # <= Küçük eşit mi?
print(5>=4) # >=  Büyük eşit mi?
print(5>4 and 6>5) # ve işlemi / her ikisi doğrumu?
print(not 5<4) # not işlemi / negatif değer almak için kullanılır
print(True or False) # veya işlemi / en az biri doğurumu
print(False and True) # veya işleminin tersini alma ?
print(5>4 or 6>5) # Veya işlemi / herhangi biri doğurumu
print(5>4 and 6<5 or 7>6) # Karmaşık koşul işlevi
print(5>4 and (6<5 or 7>6) ) # parantez ile gruplandırma
print(5>4 and not (6<5 or 7>6) ) # negasyon işlemi / not
print(5>4 and not (6<5 or 7>6) , 6<5 and 7>6) # komut ayrımı / comma
print(5>4 and not (6<5 or 7>6) , 6<5 and 7>6 , 6<5 and 7>6==True) # komutlar arasındaki boşluktan kaçmadıklarını kontrol etme / comma
print(5>4 and not (6<5 or 7>6) , 6<5 and 7>6 , 6<5 and 7>6==True) # Komut ayrımı ve boole durumları
# bölüm 1 bitti