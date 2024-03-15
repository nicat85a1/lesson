"""
# task 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    try:
        print(list1.pop(0))
    except IndexError:
        break

# task 2

list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

index = 0
while index < len(list2):
    if list2[index] in ['a', 'e', 'i', 'g', 'j']:
        index += 1
        continue
    print(list2[index])
    index += 1

# task 3

eded = int(input("eded daxil edin: "))

while True:
    i = 0
    while i <= eded:
        print(i)
        i+=1
    break

# task 4

password = "123456"

şans = 3
for i in range(3):
    kullanici = input("password daxil edin: ")
    if kullanici == password:
        print("parol doğrudur")
        break
    else:
        print(şans-1, "şansınız qaldı")
        şans -= 1
        """
"""
# task 5

sual1 = "3+4 toplamını girin"
sual1c = "A) 3 B) 4 C) 7 D) 8"
sual2 = "sade ededler nedir?"
sual2c = "A) sadece özüne ve 1'e bölünen ededler B) fsdf C) fsdd D) sfsd"
sual3 = "ededin sade eded olub olmadigini tapmaq üçün ne edirik?"
sual3c = "A) B) C) D) ededi 2 den kökaltına qeder bütün ededlere bölürük"
sual4 = "p = np nedir?"
sual4c = "A) B) belirli problemler için polinom mertebesinde bir sürede çalışacak bir algoritma varmı? C) D)"
sual5 = "yuxarıda neçe sual verilib?"
sual5c = "A)3 B)5 C)4 D)2"

dogru_cavab = 0
yanlis_cavab = 0

print(sual1)
print(sual1c)
cavab = input("cavabı seçin: ")
if cavab == "C":
    print("sizin cavabınız doğru")
    dogru_cavab += 1
else:
    print("sizin cavabınız yanlış")
    yanlis_cavab += 1
print()
print(sual2)
print(sual2c)
cavab = input("cavabı seçin: ")
if cavab == "A":
    print("sizin cavabınız doğru")
    dogru_cavab += 1
else:
    print("sizin cavabınız yanlış")
    yanlis_cavab += 1
print()
print(sual3)
print(sual3c)
cavab = input("cavabı seçin: ")
if cavab == "D":
    print("sizin cavabınız doğru")
    dogru_cavab += 1
else:
    print("sizin cavabınız yanlış")
    yanlis_cavab += 1
print()
print(sual4)
print(sual4c)
cavab = input("cavabı seçin: ")
if cavab == "B":
    print("sizin cavabınız doğru")
    dogru_cavab += 1
else:
    print("sizin cavabınız yanlış")
    yanlis_cavab += 1
print()
print(sual5)
print(sual5c)
cavab = input("cavabı seçin: ")
if cavab == "C":
    print("sizin cavabınız doğru")
    dogru_cavab += 1
else:
    print("sizin cavabınız yanlış")
    yanlis_cavab += 1

if yanlis_cavab == 4:
    dogru_cavab -= 1
print("sonucunuz: ", dogru_cavab)
print("yanlis cavab", yanlis_cavab)
"""