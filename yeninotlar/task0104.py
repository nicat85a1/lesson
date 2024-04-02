
# task 1

"""from datetime import date

def calculate_age(now):
    today = date.today()
    return today.year - now.year - ((today.month, today.day) < (now.month, now.day))

age = calculate_age(date(2000, 9, 3))

print(f"Siz heyatda {age*365.25*24*60*60:.0f} saniye, {age*365.25*24*60:.0f} deqiqe, {age*365.25*24:.0f} saat, {age*365.25:.0f} gundur ki movcudsunuz ve sizin {age} yashiniz var")

# task 2"""

import datetime
from datetime import date

x = datetime.datetime.now()

def calculate_brith():
    name = input("Enter your name: ")
    today = date.today()
    brith = date(int(x.strftime("%Y")), month=int(input("Enter Brith month: ")), day=int(input("Enter Brith day: ")))
    calculate = brith - today
    if calculate.days < 0:
        print("Hormetli",{name}, "Sizin Ad gununuze",{365+calculate.days}, "gun" ,{24-int(x.strftime("%H"))}, "saat" ,{60-int(x.strftime("%M"))}, "deq" ,{60-int(x.strftime("%S"))}, "saniye qalib")
    else:
        print("Hormetli",{name}, "Sizin Ad gununuze",{calculate.days}, "gun" ,{24-int(x.strftime("%H"))}, "saat" ,{60-int(x.strftime("%M"))}, "deq" ,{60-int(x.strftime("%S"))}, "saniye qalib")

calculate_brith()


# task 3

import random

onedict = {
    "il": "year",
    "ay": "mounth",
    "gun": "day",
    "saat": "hour",
    "deqiqe": "minute",
    "saniye": "second"
}

print(random.choice(list(onedict.keys())))