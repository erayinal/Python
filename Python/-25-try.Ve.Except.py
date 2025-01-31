#Kodda yapılan bir hatada terminalde çıkan ingilizce hata yerine biz kendi cümlelerimizle karşıya anlatmamızı sağlar

#TRY kısmında yapılabilecek hataları yazarız.Except kısmında ise yapılan bu hataları kendimiz anlatmaya çalışırız





sayı1 = input("Sayı1: ")
sayı2 = input("Sayı2: ")



try:
    sayı1 = int(sayı1)
    sayı2 = int(sayı2)
    print(sayı1/sayı2)


except ValueError:                 #Burada hatanın cinsini yazmazsak alttaki printi nerede kullanacağınız bilmez
    print("     ERROR: Lütfen 10luk tabanlı bir sayı giriniz")

except ZeroDivisionError:
    print("     ERROR: Bir sayı 0'ile bölünemez")












#Yukarıda iki farklı error tipi yazdık ama istersek tek bir except başlığı altında da toplayabiliriz

try:
    sayı1 = int(sayı1)
    sayı2 = int(sayı2)
    print(sayı1/sayı2)

except (ValueError , ZeroDivisionError):
    print("Bir Hata Oluştu")









