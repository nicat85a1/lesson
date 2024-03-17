class Calisan():
    def __init__(self,isim,maas,departman):
        print("calisan sinifinin yapici fonksyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgi(self):
        print("calisan sinifinin bilgileri gosteriliyor")
        print("isim:",self.isim,"maas:",self.maas,"departman:",self.departman)

    def zam_yap(self,zam_miktari):
        print("maasa zam yapildi")
        self.maas += zam_miktari

    def departman_degistir(self,yeni_departman):
        print("departman degistirildi")
        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        # overridinq
        print("yonetici sinifinin yapici fonksyonu")
        super().__init__(isim,maas,departman)
        self.kisi_sayisi = kisi_sayisi
    
    def bilgi(self):
        print("yonetici sinifinin bilgileri gosteriliyor")
        print("isim:",self.isim,"maas:",self.maas,"departman:",self.departman,"kisi_sayisi:",self.kisi_sayisi)


yonetici = Yonetici("ahmet",5000,"muhasebe",20)
yonetici.bilgi()