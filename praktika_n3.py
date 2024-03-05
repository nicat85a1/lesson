"""

from tkinter import *
root = Tk()
root.geometry("400x400")
root.mainloop()
"""
"""
customers = set()

print(type(customers))

for instance in range(0,1):
    name = input("Enter customer name: ")
    customers.add(name)
print(customers)

"""
"""

c = set(["python","python","java","django","Aphp"])
new_set = set()
for x in c:
    if "a" not in x:    # or A
        new_set.add(x)
print(new_set)

"""
"""

c = ["python","java","django","Aphp"]
new_list = []
for x in c:
    if "a" not in x:    # or A
        new_list.append(x)
print(new_list)

"""
"""
custemer = {}

print(type(custemer))

for instance in range(0,2):
    name = input("Enter customer name: ")
    surname = input("Enter customer surname: ")
    custemer["ad"] = name
    custemer["soyad"] = surname
    print(custemer)


custemers = {}

print(type(custemers))

for instance in range(0,2):
    name = input("Enter customer name: ")
    surname = input("Enter customer surname: ")
    custemers = { "ad": name, "soyad": surname}
    print(custemers)
"""

"""

custemers = [{'ad': 'Nicat', 'soyad': 'Huseynov'},{'ad': 'Nicats', 'soyad': 'Huseynovs'}]

print(custemers[1]["ad"])
print(custemers[1].items())
print(custemers[1].keys())
print(custemers[1].values())
print(custemers[1].get("ad"))
print(custemers[1].get("soyad"))

"""