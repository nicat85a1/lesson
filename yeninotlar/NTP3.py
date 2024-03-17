class Ogrenci():
    def derscalis(self):
        print("ogrenci ders calisiyor")

class Calisan():
    def calis(self):
        print("calisan calisiyor")

class Yazilimci(Ogrenci,Calisan):
    def derscalis(self):
        print("yazilimci ders calisiyor")

yazilimci = Yazilimci()
yazilimci.derscalis()
yazilimci.calis()