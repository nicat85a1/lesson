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
"""file = open("C:/Users/user/Desktop/praktika2.txt","w")
file.write("10 11 12 13 14 15 16 17 18 19 20")
file = open("C:/Users/user/Desktop/praktika2.txt","r")
x = file.read()
x = x.split()
for i in x:
    if int(i) % 2 == 0:
        file2 = open("C:/Users/user/Desktop/praktika3.txt","a+")
        file2.write(str(i)+" ")
        file2.close()
    try:
        cavab = int(i) / 0
    except ZeroDivisionError:
        print("0 dan yuxarı reqemler yazilmadi")"""


# task3

