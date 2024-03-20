"""
# task 1
def cem(nums):
    total = 0
    for num in nums:
        total += num
    return total
nums = [1,2,3,4,5,6,7,8,9,10]
print(cem(nums))

# task 2
def tekrar(liste):
    liste2 = []
    for i in liste:
        if i not in liste2:
            liste2.append(i)
    print(liste2)
tekrar([1,2,2,4,4,6,6,8,8,10])

# task 3
def hesapla(eded1,eded2):
    a = eded1+eded2
    b = eded1-eded2
    c = eded1*eded2
    d = eded1/eded2
    return a,b,c,d
f = hesapla(10,5)
print(f)

# task 7

def max():
    a=int(input("eded daxil edin:"))
    b=int(input("eded daxil edin:"))
    c=int(input("eded daxil edin:"))
    if a>b and a>c:
        print(a,"en boyuk")
    elif b>a and b>c:
        print(b,"en boyuk")
    elif c>a and c>b:
        print(c,"en boyuk")
max()

# task 8

import random

texmin = random.randint(1,20)

while True:
    kullanici = int(input("Texmini tap edin: "))
    if texmin == kullanici:
        print("Tebrikler")
        break
    else:
        if texmin > kullanici:
            print("yuxari")
        elif texmin < kullanici:
            print("asagi")
# task 4

def args(*kids):
  print(kids[0] + kids[1])

args(5,10)

# task 5

def kwargs(**kwargs):
  print("Your name is" " " + kwargs["names"])

kwargs(names = "Nicat")

# task 7

def max(n1,n2,n3):
    print(max(n1,n2,n3))
max(5,10,15)

# task 8

def calculate(x,y):
    def sum(a):
        return a+x
    def mul(b):
        return b*y
    def div(c):
        return c/y
    def sub(d):
        return d-x
    return sum,mul,div,sub
sum,mul,div,sub = calculate(10,2)
print(sum(10))
print(mul(10))
print(div(10))
print(sub(10))
"""
import random

texmin = random.randint(1,20)

while True:
    kullanici = int(input("Texmini tap edin: "))
    if texmin == kullanici:
        print("Tebrikler")
        break
    else:
        if texmin > kullanici:
            print("yuxari")
        elif texmin < kullanici:
            print("asagi")