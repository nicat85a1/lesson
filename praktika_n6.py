"""
# task 1
new_dict = {'name':['Orxan','Ali','Fuad','Maqa']}
sayac = 0
for i in range(len(new_dict['name'])):
    sayac += 1
    print(sayac,".",new_dict['name'][i])
    if i == 3:
        break
        """
"""
# task 3

inventory = {
     'gold' : 500,
     'pouch' : ['flint', 'twine', 'gemstone'],
     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
     }
print(inventory["gold"]+50)
"""
"""
# task 2

inventory = {
     'gold' : 500,
     'pouch' : ['flint', 'twine', 'gemstone'],
     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
     }
if input("Enter the item name: ") == "1":
    print((inventory.keys()))
elif input("Enter the item name: ") == "2":
    print((inventory.values()))
elif input("Enter the item name: ") == "3":
    print((inventory.items()))
    """
"""
# task 4

a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60,7:70}
print(a.values())
if int(input("Enter the item name: ")) in a.values():
    print("values de mövcuddur")
else:
    print("values de mövcud deyil")
    """
"""
# task 6

dictyarat = dict()

for i in range(1,16+1):
    dictyarat[i] = i**2
print(dictyarat)
"""

# task 7

euro = 1.85
usd = 1.70
azn = 1

balance = int(input("Enter the amount: "))

balanceazn = balance*azn
balanceeuro = balanceazn*euro
balanceusd = balanceazn*usd

exchege = input("Exchange: ")

if exchege == "1":
    print(balanceazn)
elif exchege == "2":
    print(balanceeuro)
elif exchege == "3":
    print(balanceusd)


# task 5
"""
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

key1 = input("Enter the key name: ")
value1 = input("Enter the value name: ")
inventory[key1] = value1
print(inventory)
"""