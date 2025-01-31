
#message = "  Hello there. My name is Eray İnal"

"""
message = message.upper()         #Her harfi büyük yazar
message = message.lower()         #Her harfi küçük yazar
message = message.title()         #Her kelimenin baş harfi büyük olur
message = message.capitalize()    #Sadece metnin baş harfini büyük yazar
message = message.strip()         #Yazılan metnin önünde ve sonundan sonra boşluk varsa onları ortadan kaldırır, metin içi boşluklara karışmaz
message = message.split()         #Yazılan metindeki her kelimeyi tırnak içinde ayrı ayrı yazdırır.Burada parantez içi boş olması boşlukları kaldırmasını belirtir
message = " ".join(message)       #Bunda mesajları tekrar birleştirir." "bunu koymasaydık bir kelime gibi yazardı kelime arası boşluk olmazdı
message.find("Eray")              #Burada metinde Eray yazısı olup olmadığını ararız ve varsa bize kaçıncı indexten sonrasında yazdığının numarasını verir.Yoksa -1 verir
message.startswith("H")           #Metnin H harfi ile başlayıp başlamadığını öğreniriz.Başlıyorsa True verir başlamıyorsa False verir
message = message.replace("Eray", "Ahmet")  #Burada metindeki Eray yazısını Ahmet ile değiştirir
message = message.center(100)     #Burada metni 100 karaktere ulaşıncaya kadar boşluk bırakır ve metni ortalar. center(100, "-") şeklinde yazarsak da 100e kadar - ile doldurur

print(message)
"""



"""
message = message.split()
print(message[0])                  #Burada hem split hem de messageye numara verirsek normaldeki gibi 1 harf değil bütün kelimeyi verir
"""




"""
message = message.split(".")      #Burada parantez içine "." koyduğumuzdan metindeki noktalara göre ayrım yaptı 
print(message)                    #Burada messageden sonra [] içine sayı koyup sadece belli bir cümleyi de yazdırabiliriz.Örneğin
print(message[0]) veya print(message[1])    #Burada iki ya da daha fazla yazamazsın çünkü noktadan önce ve sonra olmak üzere 2 yer ver => 0 ve 1
"""

"""
message = message.split()
message = " " .join(message)      #Burada tırnakla ayırdığımız mesajları tekrar birleştirip arasına " " ile boşluk koymasını söyledik.Tırnak içine - yazsak her kelime arasına - koyar
print(message)
"""



"""
a = message.find("Eray")     #Burada bize Eray kelimesini metinde varsa kaçıncı index ve sonrasında olduğunu söyler bunu öğrenmek için de bir değişken atayarak yazdırmak gerekir
print(a)                     #Yukarıda Eray kelimesi kaçıncı indexten sonrasında olduğunu öğrenmek için salladığım bir a değişkeni ile bunu yazdırıyorum
"""



"""
message = message.replace("Eray", "Ahmet")    #Burada metindeki Eray yazısını Ahmet ile değiştirir
message = message .replace(" " , "_")         #Burada metindeki boşlukları _ ile değiştirir
message = message .replace("ç" , "c") .replace("ş" , "s")         #Mesela bir Türkçe metni İngilizce karakterlerle yazmak istersek bu yöntemle kolayca değiştiririz
print(message)
"""



"""
message = message.center(200 , "-")          #Burada metni ikiyüz karaktere kadar - ile doldurur ve metni ortalar
print(message)
"""





#Bu string metodları ve daha fazlası için String Methods Python şeklinde aratıp bulabiliriz 




"""
#message = message.split()
message = "-".join(message)
print(message)
"""




"""
message = "www.erayinal.com"
message = message.strip("wwwcom")
print(message)
"""








