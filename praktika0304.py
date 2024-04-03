# task 1

"""def upper_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def some_function():
    return input("Enter word: ")
print(upper_decorator(some_function)())"""

# task 2

"""def list_numbers(a=int(input("Enter number: ")), b=int(input("Enter number: "))):
    for i in range(a, b+1):
        yield i ** 3
a = list_numbers()
print(list(a))"""

# task 3

"""def cal_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_cal = result[0] - result[1]
        if result_cal < 0:
            return 0
        else:
            return result_cal
    return wrapper

def some_function():
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    return a,b
print(cal_decorator(some_function)())"""

# task 4

"""def cal_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_cal = result ** 2 * 2
        return result_cal
    return wrapper

def some_function():
    a = int(input("Enter number: "))
    return a
print(cal_decorator(some_function)())"""

# task 5

"""months = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"]
print(months)
season_find = input("Enter month: ")

if season_find in months:
    if season_find in ["dekabr", "yanvar", "fevral"]:
        print("Qış ayıdır")
    elif season_find in ["mart", "aprel", "may"]:
        print("Yaz ayıdır")
    elif season_find in ["iyun", "iyul", "avgust"]:
        print("Yay ayıdır")
    elif season_find in ["sentyabr", "oktyabr", "noyabr"]:
        print("Payız ayıdır")
else:
    print("Elə ay yoxdu")"""

# task 6

login = {"user777": "12345!."}
print(login)

choice = "Update(press 1), Delete(press 2), Exit(press 3): "
print(choice)

import keyboard

while True:
    if keyboard.is_pressed("1"):
    
        break
    elif keyboard.is_pressed("2"):
        login["user777"] = input("Enter new password: ")
        print(login)
        break
    elif keyboard.is_pressed("3"):
        login.clear()
        print(login,"Hesabınız silindi")
        break