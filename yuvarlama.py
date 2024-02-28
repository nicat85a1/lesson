x = int(input("x:"))
y = float(input("y:"))
z = x / y
# qalıq mod işlemi
decimal = z % 1
# qalıq 5 ise
if decimal == 5:  # bu koşulu vermesem x < y olduğunda z -= 0.5 olur, x > y olduğunda ise z += 0.5 olur. her dururmda da bu bilinen riyazi yuvarlama üçün uyğun deyil.
    # z oluğu kimi qalır
    pass
else:
    # else z'yi en yaxın tam ədədə yuvarla
    z = round(z, 0)
print("Toplam", z)