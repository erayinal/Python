a = 10

def fonksiyon():
    a = 3
    print(a)


fonksiyon()           #Burada sadece girinti içerisindeki a'yı bastıracak yani 3

print(a)               #Buradaki print değeriyle yukarıdaki print değerleri faklı çünkü oradaki a sadece orada geçerlidir









a = 10

def fonksiyon2():

    global a           #Burada a'yı sadece fonksiyon için değil glabale aldık
    a = 15

    print(a)           


fonksiyon2()           #Burada fonsiyon içindeki a'yı yani 15i basar


print(a)               #Burada 10 yazdırmasını bekleriz ama hayır çünkü girintideki fonksiyonu global yaptığımız için orada 10 olan a'yı 15 olarak değiştirdik 








### Çok kullanılmaz çünkü yanlışlıkla başka bir değişkeni değiştirebiliriz ve bulması zor olabilir 