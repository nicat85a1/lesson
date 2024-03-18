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

# task 5

suallar = {
    "3+4 toplamını girin": "C",
    "sade ededler nedir?": "A",
    "ededin sade eded olub olmadigini tapmaq üçün ne edirik?": "D",
    "p = np nedir?": "B",
    "yuxarıda neçe sual verilib?": "C"
}

variantlar = {
    "3+4 toplamını girin": "A) 3 B) 4 C) 7 D) 8",
    "sade ededler nedir?": "A) sadece özüne ve 1'e bölünen ededler B) fsdf C) fsdd D) sfsd",
    "ededin sade eded olub olmadigini tapmaq üçün ne edirik?": "A) B) C) D) ededi 2 den kökaltına qeder bütün ededlere bölürük",
    "p = np nedir?": "A) B) belirli problemler için polinom mertebesinde bir sürede çalışacak bir algoritma varmı? C) D)",
    "yuxarıda neçe sual verilib?": "A)3 B)5 C)4 D)2"
}

dogru_cavab = 0
yanlis_cavab = 0

for sual, cavab in suallar.items():
    print(sual)
    print(variantlar[sual])
    cavabi = input("cavabı seçin: ")
    if cavabi == cavab:
        print("sizin cavabınız doğrudur")
        dogru_cavab += 1
    else:
        print("sizin cavabınız yanlışdir")
        yanlis_cavab += 1
    print()

if yanlis_cavab == 4: # suallarin sayi artsa bu sert islemeyecek
    dogru_cavab -= 1
    print("1 düzgün cavabınız silindi")

print("Doğru cavab: ", dogru_cavab)
print("Yanlis cavab: ", yanlis_cavab)