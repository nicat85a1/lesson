import tkinter as tk

# Pencereyi oluştur
root = tk.Tk()
root.title('Hareket Eden İnsan')

# Tuvali oluştur
canvas = tk.Canvas(root, width=400, height=400, bg='black')
canvas.pack()

# İnsan figürünü çiz (basit bir daire olarak temsil edilmiştir)
insan = canvas.create_oval(190, 190, 210, 210, fill='white')

# Tuş basımını işleyecek fonksiyon
def hareket_et(event):
    if event.keysym == 'Up':
        canvas.move(insan, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(insan, 0, 10)
    elif event.keysym == 'Left':
        canvas.move(insan, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(insan, 10, 0)

# Tuş basım olaylarını bağla
root.bind('<KeyPress-Up>', hareket_et)
root.bind('<KeyPress-Down>', hareket_et)
root.bind('<KeyPress-Left>', hareket_et)
root.bind('<KeyPress-Right>', hareket_et)

# Ana döngüyü başlat
root.mainloop()