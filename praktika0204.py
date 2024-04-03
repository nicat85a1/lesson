"""
# Task 2

dict1 = {}

for i in range(3):
    dict1[input("Enter the key: ")] = input("Enter the value: ")
    
print(dict1)

"""
# task 1
"""
def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if value == '':
            print("Mətni Boş buraxmaq olmaz")
        else:
            return value

verilen = get_valid_input("Enter verilen: ")

import keyboard

while True:
    if keyboard.is_pressed("1"):
        list1 = []
        list1.append(verilen)
        print(list1)
        print("Convert to string again? yes / no")
        while True:
            if keyboard.is_pressed("y"):
                print(verilen)
                break
            elif keyboard.is_pressed("n"):
                print(list1)
                break
        break
    elif keyboard.is_pressed("2"):
        dict1 = {}
        dict1[input("Choose Keys: ")] = verilen
        print(dict1)
        break
    elif keyboard.is_pressed("3"):
        tuple1 = ()
        tuple1 = (verilen,)
        print(tuple1)
        break
    elif keyboard.is_pressed("4"):
        break
"""

def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if value == '':
            print("Mətni Boş buraxmaq olmaz")
        else:
            return value

verilen = get_valid_input("Enter verilen: ")

import keyboard

#while True:

while True:
    if keyboard.is_pressed("1"):
        list1 = []
        list1.append(verilen)
        print(list1)
        print("Convert to string again? yes / no")
        while True:
            if keyboard.is_pressed("y"):
                print(verilen)
                break
            elif keyboard.is_pressed("n"):
                print(list1)
                break
        break
    elif keyboard.is_pressed("2"):
        dict1 = {}
        dict1[input("Choose Keys: ")] = verilen
        print(dict1)
        break
    elif keyboard.is_pressed("3"):
        tuple_ = ()
        tuple_ = (verilen,)
        print(tuple_)
        break
    elif keyboard.is_pressed("4"):
        break