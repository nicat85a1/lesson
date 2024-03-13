"""
# task 1

weight = float(input("çeki daxil et: "))
height = int(input("boy daxil et(sm): "))

BMI = round(weight / (height / 100)**2, 2)

print("BMI:", BMI)

if BMI < 18.5:
    print("zeif")
elif BMI > 18.5 and BMI < 25:
    print("normal")
elif BMI > 25 and BMI < 30:
    print("kilolu")
else:
    print("obez")

r_min_BMI = round(18.5 * (height / 100)**2, 2)
r_max_BMI = round(25 * (height / 100)**2, 2)
print("Sizin üçün ideal çəki: ",r_min_BMI,"-",r_max_BMI)
"""
"""
# task 2

onlineMarket = {
    "Smartphone": {"iphone": 50, "samsung": 40},
    "Laptop": {"asus": 35, "dell": 40},
    "headset": {"jbl": 25, "apple": 30},
    "keyboard": {"logitech": 15, "razer": 20},
    "usb memory": {"sandisk": 10, "giga": 5}
}
print(onlineMarket)
shopping_cart = []
for i in range(5):
    print("sifarişi sonlandırmaq üçün 'cancel'")
    add_to_cart = input("Almaq istediyiniz məhsulun adını daxil edin: ")
    if add_to_cart == "iphone":
        shopping_cart.append(onlineMarket["Smartphone"]["iphone"])
    if add_to_cart == "samsung":
        shopping_cart.append(onlineMarket["Smartphone"]["samsung"])
    if add_to_cart == "asus":
        shopping_cart.append(onlineMarket["Laptop"]["asus"])
    if add_to_cart == "dell":
        shopping_cart.append(onlineMarket["Laptop"]["dell"])
    if add_to_cart == "jbl":
        shopping_cart.append(onlineMarket["headset"]["jbl"])
    if add_to_cart == "apple":
        shopping_cart.append(onlineMarket["headset"]["apple"])
    if add_to_cart == "logitech":
        shopping_cart.append(onlineMarket["keyboard"]["logitech"])
    if add_to_cart == "razer":
        shopping_cart.append(onlineMarket["keyboard"]["razer"])
    if add_to_cart == "sandisk":
        shopping_cart.append(onlineMarket["usb memory"]["sandisk"])
    if add_to_cart == "giga":
        shopping_cart.append(onlineMarket["usb memory"]["giga"])
    if add_to_cart == "cancel":
        break
total_price = 0
for i in shopping_cart:
    total_price += i
total_price_VAT = total_price * 1.18
print(f"Toplam ödənəcək məbləğ (ədv daxil) : {total_price_VAT:.2f} AZN")
if total_price_VAT > 50 and total_price_VAT < 100:
    print("10 Azn kupon qazandınız, indi istifade etmek üçün 'yes', eks halda 'no' yazın")
    if input("İstifadə etmək istədiyinizə əminsiz? (yes/no) : ") == "yes":
        print(f"ödənəcək məbləğ : {total_price_VAT - 10:.2f} AZN")
    elif input("İstifadə etmək istədiyinizə əminsiz? (yes/no) : ") == "no":
        print(f"ödənəcək məbləğ : {total_price_VAT} AZN")
elif total_price_VAT >= 100:
    print("15 Azn kupon qazandınız, indi istifade etmek üçün 'yes', eks halda 'no' yazın")
    if input("İstifadə etmək istədiyinizə əminsiz? (yes/no) : ") == "yes":
        print(f"ödənəcək məbləğ : {total_price_VAT - 15:.2f} AZN")
    elif input("İstifadə etmək istədiyinizə əminsiz? (yes/no) : ") == "no":
        print(f"ödənəcək məbləğ : {total_price_VAT} AZN")
        """

# task 3

distance = float(input("Distance (km): "))
type_of_vehicle = input("Type of vehicle(car/bus/truck) : ")
if type_of_vehicle == "car":
    print(f"Səfərin qiyməti {distance * 0.50:.2f} $")
elif type_of_vehicle == "bus":
    print(f"Səfərin qiyməti {distance * 1.00:.2f} $")
elif type_of_vehicle == "truck":
    print(f"Səfərin qiyməti {distance * 2.00:.2f} $")
else:
    print("Select vehicle type!")