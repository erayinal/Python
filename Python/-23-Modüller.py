
### Başka sayfada yazmış olduğun zor fonksiyonları istediğimiz başka bir sayfada tekrar kullanmamıza olanak sağlar


def naber():
    print("Naber ")

def mutlak(numara):

    if(numara<0):
        return -numara

    else:
        return numara









################    BURADAN AŞAĞISI BAŞKA BİR SAYFAYMIŞ GİBİ İLERLİYORUZ   ##############




"""
import Modüller


Modüller.naber()                #Burada başka bir sayfada yazılmış olan naber fonksiyonunu aldık 


print(Modüller.mutlak(-2))      #Burada başka bir sayfada yazılmış olan mutlak fonsiyonunu çağırdık

"""













#######   BAŞKA BİR YÖNTEM DAHA VAR ŞİMDİ DE ONU DENEYELİM  ###########


from Modüller import naber


from Modüller import *       #Burada yıldız(*) fonksiyonların hepsini kapsamasını sağlar.İstesek yukarıdaki şekilde birisini de çağırabiliriz ama böyle daha kullanışlı:
print(mutlak(-120))


#Bu yöntem fazla önerilmez çünkü mesela iki farklı sayfadan dahil elliğiniz fonsiyoonlarda aynı isimde fonksiyon varsa python kafayı yer
    #Melesa A ve B sayfasında "naber" adında iki tane fonsiyon var ve siz ikisini de sayfaya dahil ettiniz ve kullanmak istiyorsunuz
        #Altına "number()" yazarsanız python bu fonsiyonu A'dan mı B'den mi alacağını anlamaz


















########## BUNLARIN YANINDA BİR DE HAZIR KÜTÜPHANELRİMİZ  VAR YANİ BAŞKA SAYFADA YAZILMASINA GEREK KALMADAN DAHİL EDEBİLİRSİNİZ ########### 


import math

print(math.factorial(6))   #Burada math kütüphanesinden factorial fonsiyonunu dahil ettik