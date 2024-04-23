"""# task1
try:
    num1 = int(input("enter num 1: "))
    num2 = int(input("enter num 2: "))
    cavab = num1 / num2
    file = open("C:/Users/user/Desktop/praktika.txt","w")
    file.write(str(cavab))
    file.close()
except ZeroDivisionError:
    print("0 dan yuxarı reqem girin")"""

# task2

file = open("C:/Users/user/Desktop/praktika2.txt","w")
file.write("10 11 12 13 14 15 16 17 18 19 20")
file = open("C:/Users/user/Desktop/praktika2.txt","r")
x = file.read()
x = x.split()
for i in x:
    if int(i) % 2 == 0:
        file2 = open("C:/Users/user/Desktop/praktika3.txt","a+")
        file2.write(str(i)+" ")
        file2.close()
    else:
        try:
            cavab = int(i) / 0
        except ZeroDivisionError:
            print(f"{i} 2 ye bölünmür")

print("-------------------------------------------------------------------------------------------------")

file = open("C:/Users/user/Desktop/praktika2.txt","w")
file.write("10 11 12 13 14 15 16 17 18 19 20")
file = open("C:/Users/user/Desktop/praktika2.txt","r")
x = file.read()
x = x.split()
for i in x:
    try:
        if int(i) % 2 == 0:
            file2 = open("C:/Users/user/Desktop/praktika3.txt","a+")
            file2.write(str(i)+" ")
            file2.close()
        else:
            raise ValueError #(f"{i} 2 ye bölünmür")
    except: # ValueError as e
        print(f"{i} 2 ye bölünmür")

# task3

"""Məhsullar = {
    "iphone": "1400",
    "samsung": "400",
    "xiaomi": "200"
}

with open("C:/Users/user/Desktop/praktika4.txt", "w") as file:
    for key, value in Məhsullar.items():
        file.write(f"{key}: {value}\n")
file = open("C:/Users/user/Desktop/praktika4.txt","r")
x = file.read()
x = x.split()
total = 0
for _ in range(3):
    choise_shop = input("Məhsulun adini daxil edin: ")+":"
    if choise_shop in x:
        if choise_shop == "iphone:":
            print(f"Məhsulun qiymeti: {x[1]}")
            total += int(x[1])
            try:
                if total >= 1500:
                    print(f"Sizin toplam məbləğiniz: {total}")
                    if total / 0 == 0:
                        print()
            except:
                print("icazə verilən məbləği keçdiniz, yenidən seçəm edin və ya sifarişi sonlandırın")
                total -= int(x[1])
        elif choise_shop == "samsung:":
            print(f"Məhsulun qiymeti: {x[3]}")
            total += int(x[3])
            try:
                if total >= 1500:
                    print(f"Sizin toplam məbləğiniz: {total}")
                    if total / 0 == 0:
                        print()
            except:
                print("icazə verilən məbləği keçdiniz, yenidən seçəm edin və ya sifarişi sonlandırın")
                total -= int(x[1])
        elif choise_shop == "xiaomi:":
            print(f"Məhsulun qiymeti: {x[5]}")
            total += int(x[5])
            print(total)
            try:
                if total >= 1500:
                    print(f"Sizin toplam məbləğiniz: {total}")
                    if total / 0 == 0:
                        print()
            except:
                print("icazə verilən məbləği keçdiniz, yenidən seçəm edin və ya sifarişi sonlandırın")
                total -= int(x[1])
print("Yekun ödəniş: ",total)"""