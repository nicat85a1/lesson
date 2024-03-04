"""
# task 1

a = ["python","php","java"]

print(a[0])
print(a[len(a)-1])

# task 2

test_list = [6, 7, [], 3, [], [], 9]

test_list.pop(2),test_list.pop(4)
test_list.pop(-2)
print(test_list)

for x in test_list:
if type(x) == int
print(x)
"""
# task 3
b = ["python","php","java"]
print(b)
daxil = input("ad daxil edin:")
if daxil == "":
    print("ad daxil edilmedi")
elif len(daxil) > 15:
    print("ad 15 simvoldan cox ola bilmez")
    sil = input("ad silin:")
else: 
    pass

if sil == "":
    print("ad daxil edilmedi:")
elif len(sil) > 15:
    print("ad 15 simvoldan cox ola bilmez")

islemler = input("işlemi seç(1/2): ")
if islemler in ('1', '2'):
    if islemler == '1':
        b.append(daxil)
        print(b)
    elif islemler == '2':
        b.remove(sil)
        print(b)
print(b)       
"""
# task 4
c = ["python","java","django","Aphp"]
new_list = []
for x in c:
    if "a" not in x:    # or A
        new_list.append(x)
print(new_list)

# task 5

kelime = input("kelime gir: ")
print(kelime[len(kelime)-1])
d = ("a")
if d in kelime:
    print(True)
else:
    print(False)

# task 6

a = [1,2,3,4,5,6,7,8,9,1]
if a[0] == a[-1]:
    print(True)
else:
   print(False)

# task 7
    
a = [1,2,3,4,5,6,7,8,9,10]

for x in a:
    print(x ** 2)
"""