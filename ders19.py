"""

def num(x):
    if x == -1:
        return "hello"
    return num(x-1)
num(5)
print(num(5))

num = lambda x: x if x == -1 else num(x-1)
"""
"""
def tax_calculator(price, quantity):
    return price * quantity * 1.18

def product(name,price,quantity):
    tax = tax_calculator(price,quantity)

    product_dict = {
        "name":name,
        "price":price,
        "quantity":quantity,
        "tax":tax
    }
    return product_dict

print(product("apple",10,5))
"""
"""
def product(name,price,quantity):
    tax = lambda price,quantity: price * quantity * 1.18

    product_dict = {
        "name":name,
        "price":price,
        "quantity":quantity,
        "tax":tax(price,quantity)
    }
    return product_dict

print(product("apple",10,5))
"""

def budce(*args):
    for i in range(3):
        xerc=int(input("xerc: "))
        gelir=int(input("gelir: "))
        print("budceniz qaldi: ",gelir-xerc)
    return
budce() # inport