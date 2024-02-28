"""
file = open("C:/Users/user/Desktop/dosya1.txt","w") # w dosya oluşturur. a ekleme yapar.
file.write("Merhaba\nNaber") # ve ya file.write("Merhaba\n") file.write("Naber") yazılabilir.
file.close()

file = open("C:/Users/user/Desktop/dosya.txt","r") # r okur.
file.seek(2) # 2.ci karakterden sonrasını okur
veri = file.read() # .read(2) yazarsan ilk 2 karaktere kadar okur.
print(veri)
file.close()
"""
"""
file = open("C:/Users/user/Desktop/dosya.txt","r")
for satir in file:
    print(satir) # for döngüsü ile okuma
file.close()
"""
class Accaunt: # veri tipinin ismi
    def __init__(self,isim,numara,bakiye): # objenin özelliklerini oluştur
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapBilgileri (self):
        print("isim : ",self.isim)
        print("numara : ",self.numara)
        print("bakiye : ",self.bakiye)
    def paraCek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("Yetersiz Bakiye")
        else:
            self.bakiye =self.bakiye - miktar
            print(f"Para çekildi. Kalan Bakiye : {self.bakiye}" )
    def paraYatir(self,miktar):
        self.bakiye += miktar
        print(f"Para yatırıldı. Yeni Bakiye : {self.bakiye}",)

accaunt = Accaunt("Ali",944559998877,1000)

accaunt.hesapBilgileri()
accaunt.paraCek(400)
accaunt.paraYatir(600)

# git init -  bir projeyi git ile yönetmeye başlama
# git add -  dosyayı staging area'ya ekleme
# git add . - tüm değişiklikleri staging area'ya ekleme
# git commit - snapshot alma
# git status -  değişenleri gösterme
# git push - sunucuya gönderme
# git pull - sunucudan alma
# git clone - projeyi klonlama
# git chekout - branch geçişi / dal
# git rm - dosyayı silme (takip edilenlerden)
# yeni bir branch açmak için : git checkout -b newbranch
# git log - tüm geçmişi görme
# git diff - farkları görme
# git show - detaylı bilgi görme
# git config --list - konfigürasyonları görme
# git merge - birleştirme (branch ler arasıda)
# git remote add - uzak repo ekleme
# git fetch - uzak repo dan veriyi getirme
# git push origin master - sunucuya gönder
# pwd - şu anki dizinin tam adresini verir
# ls - dosyaları listeler
# cd - dizin değiştirme
# mkdir - yeni klasör oluşturulması
# touch - yeni dosya oluşturulması
# cat > filename <<EOF - dosyanın içeriğini belirtme
# nano filename - dosyaya giriş yapabilmem için kullanılan editör
# vi/vim/emacs - text editor açılır
# ctrl+o - kaydetme
# ctrl+x - çıkış
# clear - terminali temizleme
# whoami - kullanıcı adını verir
# kill - pid numarası ile processi sonlandırma
# man command - komut hakkında bilgi verir
# whatis command -  komutun ne işe yaradığını söyləyir
# apt-get install - linux da paket yüklemesi
# apt update - yeni versiyon var mı kontrol et
# apt upgrade - yükseltmə
# sudo su - root yetkilisi alma