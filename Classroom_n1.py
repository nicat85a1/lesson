"""
### Pərakəndə:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
mehsullar = []

for i in range(6):
    mehsul = {}  # "Dictionaries" yaradıram
    mehsul["Adı"] = input("Məhsulun adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    mehsul["Qiymeti"] = float(input("Məhsulun qiymətini daxil edin: "))
    mehsullar.append(mehsul)  # elave edirem

for mehsul in mehsullar:  # alt alta yazmaq üçün listden çıxardım.
    print("Mehsulun adı: {Adı} - Qiymeti: {Qiymeti} AZN".format(**mehsul))

### Səhiyyə:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
xesteler = []

for i in range(5):
    xeste = {}  # "Dictionaries" yaradıram
    xeste["Adı"] = input("Xestenin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    xeste["Yaşı"] = int(input("Xestenin yaşını daxil edin: "))
    xesteler.append(xeste)  # elave edirem

for xeste in xesteler:  # alt alta yazmaq üçün listden çıxardım.
    print("Xestenin adı: {Adı} - Yaşı: {Yaşı}".format(**xeste))

### Təhsil:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Telebeler = []

for i in range(8):
    telebe = {}  # "Dictionaries" yaradıram
    telebe["Adı"] = input("Telebenin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    telebe["Yaşı"] = int(input("Telebenin yaşını daxil edin: "))
    Telebeler.append(telebe)  # elave edirem

for telebe in Telebeler:  # alt alta yazmaq üçün listden çıxardım.
    print("Telebenin adı: {Adı} - Yaşı: {Yaşı}".format(**telebe))

### Restoran:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Qidalar = []

for i in range(4):
    qida = {}  # "Dictionaries" yaradıram
    qida["Adı"] = input("Qidanın adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    qida["Qiymeti"] = float(input("Qidanın qiymətini daxil edin: "))
    Qidalar.append(qida)  # elave edirem

for qida in Qidalar:  # alt alta yazmaq üçün listden çıxardım.
    print("Qidanın adı: {Adı} - Qiymeti: {Qiymeti} AZN".format(**qida))

### Texnologiya:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
developers = []

for i in range(4):
    developer = {}  # "Dictionaries" yaradıram
    developer["Adı"] = input("Tertibatçının adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    developer["Yaşı"] = int(input("Tertibatçının yaşını daxil edin: "))
    developer["P.dili"] = input("Tertibatçının proqramlaşdırma diliyini daxil edin: ")
    developers.append(developer)  # elave edirem

for developer in developers:  # alt alta yazmaq üçün listden çıxardım.
    print("Tertibatçının adı: {Adı} - Yaşı: {Yaşı}, Proqramlaşdırma Dili: {P.dili}".format(**developer))

### Əyləncə:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Filmler = []

for i in range(4):
    film = {}  # "Dictionaries" yaradıram
    film["Adı"] = input("Filmin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    film["İstehsal tarixi"] = int(input("Filmin istehsal tarixini daxil edin: "))
    Filmler.append(film)  # elave edirem

for film in Filmler:  # alt alta yazmaq üçün listden çıxardım.
    print("Filmin adı: {Adı} - İstehsal tarixi: {İstehsal tarixi}".format(**film))

### Daşınmaz Əmlak:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Evler = []

for i in range(4):
    ev = {}  # "Dictionaries" yaradıram
    ev["Sahesi"] = input("Evin sahesini daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    ev["Qiymeti"] = float(input("Evin Qiymetini daxil edin: "))
    Evler.append(ev)  # elave edirem

for ev in Evler:  # alt alta yazmaq üçün listden çıxardım.
    print("Evin sahesi: {Sahesi} m² - Evin Qiymeti: {Qiymeti} Azn".format(**ev))

### Elektron ticarət:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
mehsullar = []

for i in range(7):
    mehsul = {}  # "Dictionaries" yaradıram
    mehsul["Adı"] = input("Məhsulun adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    mehsul["Qiymeti"] = float(input("Məhsulun qiymətini daxil edin: "))
    mehsullar.append(mehsul)  # elave edirem

for mehsul in mehsullar:  # alt alta yazmaq üçün listden çıxardım.
    print("Mehsulun adı: {Adı} - Qiymeti: {Qiymeti} AZN".format(**mehsul))

### Kənd Təsərrüfatı:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Tərəvəzlər = []

for i in range(2):
    Tərəvəz = {}  # "Dictionaries" yaradıram
    Tərəvəz["Adı"] = input("Tərəvəzin adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    Tərəvəz["Qiymeti"] = float(input("Tərəvəzin qiymətini daxil edin: "))
    Tərəvəzlər.append(Tərəvəz)  # elave edirem

for Tərəvəz in Tərəvəzlər:  # alt alta yazmaq üçün listden çıxardım.
    print("Tərəvəzin adı: {Adı} - Qiymeti: {Qiymeti} AZN".format(**Tərəvəz))

### Telekommunikasiya:

# {} içerisinde eyni adlı key veremediğim için list oluşturdum
Telefonlar = []

for i in range(6):
    Telefon = {}  # "Dictionaries" yaradıram
    Telefon["Adı"] = input("Telefonun adını daxil edin: ")  # key'lere value vermmek üçün input isteyirem.
    Telefon["Qiymeti"] = float(input("Telefonun qiymətini daxil edin: "))
    Telefonlar.append(Telefon)  # elave edirem

for Telefon in Telefonlar:  # alt alta yazmaq üçün listden çıxardım.
    print("Telefonların adı: {Adı} - Qiymeti: {Qiymeti} AZN".format(**Telefon))


### Maliyyə:
    
total_value = 0 # ümumi deyer

for i in range(3):
    count = int(input("Səhmin sayını daxil edin: "))
    price = float(input("Səhmin qiymətini daxil edin: "))
    total_value += count * price # deyeri hesablayıb ümumi deyere elave edirem

print(f"Səhm portfelinin ümumi dəyəri: {total_value} AZN") # format ile yazdırıram

### Nəqliyyat:

mesafe = float(input("Qət olunmuş məsafəni kilometr cinsindən daxil edin: "))
vaxtd = int(input("Alınan vaxtı deqiqe cinsindən daxil edin: "))
vaxt = vaxtd / 60
orta_suret = mesafe / vaxt
print(f"Avtomobilin orta sürəti: {orta_suret} km/saat")
"""
"""
### Səyahət Sənayesi:

aviabilet_qiymeti = float(input("Aviabiletin qiymətini daxil edin: "))
otel_qiymeti = float(input("Otelin qiymətini daxil edin: "))
avtomobil_icarəsi_qiymeti = float(input("Avtomobil icarəsinin qiymətini daxil edin: "))

# seyahet_muddeti = int(input("Səyahətin müddətini gün cinsindən daxil edin: "))   # optional

umumi_deyer = aviabilet_qiymeti + (otel_qiymeti + avtomobil_icarəsi_qiymeti) # * seyahet_muddeti
print(f"Səyahətin ümumi dəyəri: {umumi_deyer:.2f} AZN") # :.2f 2 ondalık basamaklı sayı
"""
"""
### Tikinti sənayesi:

materiallar = ['taxta', 'sement', 'qum', 'dəmir']
umumi_deyer = 0

for material in materiallar:
    kemiyyet = float(input(f"{material.capitalize()} kəmiyyətini daxil edin: "))
    qiymet = float(input(f"{material.capitalize()} qiymətini daxil edin: "))
    umumi_deyer += kemiyyet * qiymet
print(f"Tikinti layihəsi üçün lazım olan materialların ümumi dəyəri: {umumi_deyer:.2f} AZN")
"""