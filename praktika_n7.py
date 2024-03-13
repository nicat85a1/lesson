"""
# task 1

num = int(input("Say daxil edin: "))
toplam=0
for i in range(1,num+1):
    toplam+=i
print(toplam)
"""
"""
# task 2

man_accessories = ["bmw", "audi", "toyota"]

woman_accessories = ["moon","star","sun"]

gender = input("Cinsiyyetinizi daxil edin(man/woman): ")

age = int(input("Yashinizi daxil edin: "))

if gender == "man" and age >= 18:
    print(man_accessories)
elif gender == "woman" and age >= 18:
    print(woman_accessories)
else:
    print("alışveriş hüququnuz yoxdur")

"""
"""
clothing = {
    "man": ["Blazer", "Cardigan", "Shirt"],
    "woman": ["Dress","Gown","Leggings"],
    "child": ["Skirt","Heels","Blouse"]
}
gender = input("Cinsiyyetinizi daxil edin(man/woman): ")
age = int(input("Yashinizi daxil edin: "))

if age >= 18 and gender == "man":
    print(clothing["man"])
elif age >= 18 and gender == "woman":
    print(clothing["woman"])
elif age < 18 and (gender == "man" or gender == "woman"):
    print(clothing["child"])
    """
"""
megafun = input("eylence növünü daxil edin(Bovling/Tramplin,fun): ")
if megafun == "Bovling":
    age = int(input("Yashinizi daxil edin: "))
    if age < 8:
        print("yaşınız azdır")
    else:
        print("biletiniz hazırdı")
if megafun == "Tramplin":
    age = int(input("Yashinizi daxil edin: "))
    weight = int(input("Vesenizi daxil edin: "))
    if age < 8 and weight > 110:
        print("yaşınız azdır və ya çekiniz çoxdur")
    else:
        print("biletiniz hazırdı")
if megafun == "fun":
    fun_alt = input("alt kategoriya daxil edin(Əjdaha/Yelləncək/Sürətli karusel): ")
    if fun_alt == "Əjdaha" or fun_alt == "Yelləncək" or fun_alt == "Sürətli karusel":
        if fun_alt == "Əjdaha":
            age = int(input("Yashinizi daxil edin: "))
            weight = int(input("Vesenizi daxil edin: "))
            if age < 12 and weight > 110:
                print("yaşınız azdır və ya çekiniz çoxdur")
            else:
                print("biletiniz hazırdı")
        if fun_alt == "Yelləncək":
            age = int(input("Yashinizi daxil edin: "))
            weight = int(input("Vesenizi daxil edin: "))
            if age < 6 and weight > 110:
                print("yaşınız azdır və ya çekiniz çoxdur")
            else:
                print("biletiniz hazırdı")
        if fun_alt == "Sürətli karusel":
            age = int(input("Yashinizi daxil edin: "))
            weight = int(input("Vesenizi daxil edin: "))
            height = int(input("Boyunuzu daxil edin(sm): "))
            if age < 8 and weight > 110 and height > 190:
                print("yaşınız, çekiniz ve ya boyunuz uyğun deyil")
            else:
                print("biletiniz hazırdı")

"""

# task 4

cinema = {
    "man": {"family": ["inception"], "all": ["Mission Impossible","Extraction"]},
    "woman": {"family": ["inception","Barbie"], "all": ["Murder Mystery"]},
    "child": {'disney':['Transformers'],
            'marvel':['Kaptan Marvel',"Blue Beetle"]},
}

gender = input("Cinsiyyetinizi daxil edin(man/woman): ")
if gender == "man":
    age = int(input("yaşınızı daxil edin: "))
    if age < 18:
        print(cinema["child"])
        if input("disney/marvel") == "disney":
            print(cinema["child"]["disney"])
        elif input("disney/marvel") == "marvel":
            print(cinema["child"]["marvel"])
    elif age >= 18:
        family = input("teksiz yoxsa övladınızla gelmisiz?(tek/uşaqla) ")
        if family == "tek":
            print(cinema["man"]["all"])
        elif family == "uşaqla":
            print(cinema["man"]["family"])
elif gender == "woman":
    age = int(input("yaşınızı daxil edin: "))
    if age < 18:
        print(cinema["child"])
        if input("disney/marvel") == "disney":
            print(cinema["child"]["disney"])
        elif input("disney/marvel") == "marvel":
            print(cinema["child"]["marvel"])
    elif age >= 18:
        family = input("teksiz yoxsa övladınızla gelmisiz?(tek/uşaqla) ")
        if family == "tek":
            print(cinema["woman"]["all"])
        elif family == "uşaqla":
            print(cinema["woman"]["family"])