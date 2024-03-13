"""
### Pərakəndə:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
products = []

for i in range(2):
    product = {}  # "Dictionaries" yaradıram
    product["name"] = input("Məhsulun adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    product["price"] = float(input("Məhsulun qiymətini daxil edin: "))
    products.append(product)  # elave edirem

for product in products:  # alt alta yazmaq üçün listden çıxardım.
    print("product name: {name} - price: {price} AZN".format(**product))

### Səhiyyə:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
patients = []

for i in range(5):
    patient = {}  # "Dictionaries" yaradıram
    patient["name"] = input("Xestenin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    patient["age"] = int(input("Xestenin yaşını daxil edin: "))
    patients.append(patient)  # elave edirem

for patient in patients:  # alt alta yazmaq üçün listden çıxardım.
    print("Patient name: {name} - age: {age}".format(**patient))

### Təhsil:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
students = []

for i in range(8):
    student = {}  # "Dictionaries" yaradıram
    student["name"] = input("Telebenin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    student["age"] = int(input("Telebenin yaşını daxil edin: "))
    students.append(student)  # elave edirem

for student in students:  # alt alta yazmaq üçün listden çıxardım.
    print("Student name: {name} - age: {age}".format(**student))

### Restoran:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Foods = []

for i in range(4):
    food = {}  # "Dictionaries" yaradıram
    food["name"] = input("Qidanın adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    food["price"] = float(input("Qidanın qiymətini daxil edin: "))
    Foods.append(food)  # elave edirem

for food in Foods:  # alt alta yazmaq üçün listden çıxardım.
    print("Food name: {name} - price: {price} AZN".format(**food))

### Texnologiya:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
dHouseelopers = []

for i in range(4):
    dHouseeloper = {}  # "Dictionaries" yaradıram
    dHouseeloper["name"] = input("Tertibatçının adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    dHouseeloper["age"] = int(input("Tertibatçının yaşını daxil edin: "))
    dHouseeloper["lang"] = input("Tertibatçının proqramlaşdırma diliyini daxil edin: ")
    dHouseelopers.append(dHouseeloper)  # elave edirem

for dHouseeloper in dHouseelopers:  # alt alta yazmaq üçün listden çıxardım.
    print("DHouseeloper name: {name} - age: {age}, lang: {lang}".format(**dHouseeloper))

### Əyləncə:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
movies = []

for i in range(4):
    movie = {}  # "Dictionaries" yaradıram
    movie["name"] = input("Filmin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    movie["date_of"] = int(input("Filmin istehsal tarixini daxil edin: "))
    movies.append(movie)  # elave edirem

for movie in movies:  # alt alta yazmaq üçün listden çıxardım.
    print("Movie name: {name} - date_of: {date_of}".format(**movie))

### Daşınmaz Əmlak:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Houses = []

for i in range(4):
    House = {}  # "Dictionaries" yaradıram
    House["area"] = input("Evin sahesini daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    House["price"] = float(input("Evin priceni daxil edin: "))
    Houses.append(House)  # elave edirem

for House in Houses:  # alt alta yazmaq üçün listden çıxardım.
    print("House area: {area} m² - House price: {price} Azn".format(**House))

### Elektron ticarət:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
products = []

for i in range(7):
    product = {}  # "Dictionaries" yaradıram
    product["name"] = input("Məhsulun adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    product["price"] = float(input("Məhsulun qiymətini daxil edin: "))
    products.append(product)  # elave edirem

for product in products:  # alt alta yazmaq üçün listden çıxardım.
    print("product name: {name} - price: {price} AZN".format(**product))

### Kənd Təsərrüfatı:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Vegetables = []

for i in range(2):
    Vegetable = {}  # "Dictionaries" yaradıram
    Vegetable["name"] = input("Vegetablein adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    Vegetable["price"] = float(input("Vegetablein qiymətini daxil edin: "))
    Vegetables.append(Vegetable)  # elave edirem

for Vegetable in Vegetables:  # alt alta yazmaq üçün listden çıxardım.
    print("Vegetable name: {name} - price: {price} AZN".format(**Vegetable))

### Telekommunikasiya:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Telephones = []

for i in range(6):
    Telephone = {}  # "Dictionaries" yaradıram
    Telephone["name"] = input("Telephone name daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    Telephone["price"] = float(input("Telephone price daxil edin: "))
    Telephones.append(Telephone)  # elave edirem

for Telephone in Telephones:  # alt alta yazmaq üçün listden çıxardım.
    print("Telephone name: {name} - price: {price} AZN".format(**Telephone))

### Maliyyə:
    
total_value = 0 # ümumi deyer

for i in range(3):
    count = int(input("Səhmin sayını daxil edin: "))
    price = float(input("Səhmin qiymətini daxil edin: "))
    total_value += count * price # deyeri hesablayıb ümumi deyere elave edirem

print(f"The total value of the stock portfolio: {total_value} AZN") # format ile yazdırıram

### Nəqliyyat:

distance = float(input("Qət olunmuş məsafəni kilometr cinsindən daxil edin: "))
time_m = int(input("Alınan timeı deqiqe cinsindən daxil edin: "))
time = time_m / 60
average_speed = distance / time
print(f"Avtomobilin orta sürəti: {average_speed} km/saat")

### Səyahət Sənayesi:

airfare_price = float(input("Aviabiletin qiymətini daxil edin: "))
hotel_price = float(input("Otelin qiymətini daxil edin: "))
car_rental_price = float(input("Avtomobil icarəsinin qiymətini daxil edin: "))

# travel_duration = int(input("Səyahətin müddətini gün cinsindən daxil edin: "))   # optional

total_cost = airfare_price + (hotel_price + car_rental_price) # * travel_duration
print(f"Səyahətin ümumi dəyəri: {total_cost:.2f} AZN") # :.2f 2 ondalık basamaklı sayı

### Tikinti sənayesi:

materials = ['taxta', 'sement', 'qum', 'dəmir']
total_cost = 0

for material in materials:
    quantity = float(input(f"{material.capitalize()} kəmiyyətini daxil edin: "))
    price = float(input(f"{material.capitalize()} qiymətini daxil edin: "))
    total_cost += quantity * price
print(f"The total cost of materials needed for the construction project: {total_cost:.2f} AZN")
"""