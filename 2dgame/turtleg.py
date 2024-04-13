import turtle

# Pencereyi oluştur
wn = turtle.Screen()
wn.title('Hareket Eden İnsan')
wn.bgcolor('black')

# İnsan figürünü çiz (basit bir daire olarak temsil edilmiştir)
insan = turtle.Turtle()
insan.shape('circle')
insan.color('white')
insan.penup()  # Kalem kaldırılarak iz bırakması engellenir

# Tuş basımını işleyecek fonksiyonlar
def hareket_et_yukari():
    insan.sety(insan.ycor() + 10)

def hareket_et_asagi():
    insan.sety(insan.ycor() - 10)

def hareket_et_sol():
    insan.setx(insan.xcor() - 10)

def hareket_et_sag():
    insan.setx(insan.xcor() + 10)

# Tuş basım olaylarını bağla
wn.listen()
wn.onkey(hareket_et_yukari, 'Up')
wn.onkey(hareket_et_asagi, 'Down')
wn.onkey(hareket_et_sol, 'Left')
wn.onkey(hareket_et_sag, 'Right')

# Ana döngüyü başlat
wn.mainloop()