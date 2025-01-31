"""

Mesela facebooka kaydolurken bazı adımları geçeriz ve sonra istersek ekleyebilirz mesela "ilişki durumu" gibi, burada da cevaplamak istemediğimiz inputu geçebiliriz

"""





"""
def kayıt_ekle(ad="bilgi yok" , soyad="bilgi yok" , yaş="bilgi yok" , ilişki="bilgi yok"):

    print("Hoş geldin")

    print("Ad: {}\nSoyad: {}\nYaş: {}\nİlişki: {} ".format(ad , soyad , yaş , ilişki))

    print("Kayıt başarılı...")



kayıt_ekle("Eray" , "İnal")    #Burada sırasıyla yazığımız için işlem oldu ama biz soyad girmeden yaş girsek bunu python anlamaz.Bunun için:

kayıt_ekle(ad = "Eray" , yaş = 20 , ilişki = "hep yek")     #İşte burada yukarıdaki sorunu çözmüş olduk...
"""





"""
#Pratik :

def insta_kayıt(ad = "-" , soyad = "-" , kullanıcıAdı = "-" , şifre = "-" ):

    print("Kayıt olmaya hoşgeldiniz...")

    print("Isim: {}\nSoyisim: {}\nKullanıcı: {}\nŞifre: {}".format(ad , soyad , kullanıcıAdı , şifre))

    print("Kayıt Başarılı...")


insta_kayıt(soyad = "İnal" , kullanıcıAdı = "inaleray" , şifre = "123234")

"""













"""

def insta(isim = "bilgi verilmedi" , soyisim = "Bilgi verilmedi" , yaş = "Bilgi verilmedi" , cinsiyet = "Bilgi verilmedi"):

    print("Hoşgeldiniz")
    print("İsim: {}\nSoyisim: {}\nYaş: {}\nCinsiyet: {}".format(isim , soyisim , yaş , cinsiyet) )


insta(soyisim = "İnal" , isim = "eray" )

"""

