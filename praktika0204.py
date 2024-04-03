"""
# Task 2

dict1 = {}

for i in range(3):
    dict1[input("Enter the key: ")] = input("Enter the value: ")
    
print(dict1)

"""
# task 1

import keyboard

def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if value == '':
            print("Mətni Boş buraxmaq olmaz")
        else:
            return value

verilen = get_valid_input("Enter verilen: ")

pressed_keys = {'3': False} # tekrarlayan kodları engelle

while not keyboard.is_pressed('4'):
    if keyboard.is_pressed('1'):
        list1 = []
        list1.append(verilen)
        print(list1)
        print("Convert to string again? yes / no")
        while True:
            if keyboard.is_pressed('y'):
                print(verilen)
                break
            elif keyboard.is_pressed('n'):
                print(list1)
                break
    elif keyboard.is_pressed('2'):
        dict1 = {}
        key = input("Choose Keys: ")
        dict1[key] = verilen
        print(dict1)
    elif keyboard.is_pressed('3') and not pressed_keys['3']:
        pressed_keys['3'] = True
        tuple1 = (verilen,)
        print(tuple1)

    if not keyboard.is_pressed('3'):
        pressed_keys['3'] = False

print("Exiting the program as '4' was pressed.")