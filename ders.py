# task 1
"""
kütle = float(input("çeki daxil et: "))
boy = float(input("boy daxil et: "))

BKI = round(kütle / (boy / 100)**2, 1)

print("BKI:", BKI)

if BKI < 18.5:
    print("zeif")
elif BKI > 18.5 and BKI < 25:
    print("normal")
elif BKI > 25 and BKI < 30:
    print("kilolu")
elif BKI > 30:
    print("obez")
"""
# task 2

şifre = input("şifrenizi daxil edin: ")
if len(şifre) < 6:
    print("şifre 6 simvoldan azdir")
elif len(şifre) > 16:
    print("şifre 16 simvoldan çoxdur")

import re

x = re.findall("[a-z]", şifre)
z = re.findall("[A-Z]", şifre)
v = re.findall("[$#@]", şifre)
b = re.findall("[0-9]", şifre)

if not (x):
    print("a-z yoxdur")
if not (z):
    print("A-Z yoxdur")
if not (v):
    print("simvol yoxdur")
if not (b):
    print("0-9 yoxdur")

if x and z and v and b:
    print("şifre güclüdür")