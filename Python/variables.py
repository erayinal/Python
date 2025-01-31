maaşEray = 50000
maaşÖmer = 20000
print(maaşEray - maaşÖmer)

# DEĞİŞKEN DEĞİŞTİRME KURALLARI  
# Rakam ile başlayamaz (1adam = 4000), simgelerle başlamasında sakınca YOKTUR (adam1 = 4000)

# Birinci değişkendeki sayıyı değiştirebiliriz
adamım1 = 20 
adamım1 += 30
print(adamım1)  #bu işlemin sonucu Adamım1 ile sonradan belirlediğimiz 30'un toplamıdır yani 50

# Değişkenlerde büyük küçük harf ayrımı vardır yani adamım2 ile Adamım2 aynı değildir

# Türkçe yazmamaya özen gösterelim eğer illa yazacaksakda ŞİÖÇÜ gibi ifadeler kelimede yer almasın


# Değişkeni illa sayısal olarak değil ("") içinde kelime olarak da yazabiliriz
a = 10   
b =20       #Print ile burada normal bir toplama yapılır
x = "9"  
y = "8"     #Print ile burada toplama yapılmaz sadece yan yana yazar
print(a+b)
print(x+y)
name = "Eray"   #Print ile bunları toplarsak bize Erayinal yazısını verir
surname = "inal"
print(name+surname)


# Değişkenleri aynı satıra da yazabiliriz
clio = 500
bmw = 800
nameler = "Eraysss"  #yerine:
clio, bmw, nameler = (500, 800, "Eraysss") #yazabiliriz
print(clio + bmw) #sonuç iki şekilde de değişmez


# Değişken yazarken kelime arası boşluk olamaz "_" kullanılması tavsiye edilebilir
first_past = 45  #olabilir fakat bunu (first past) şeklinde yazarsak sorun verir



place = "akdeniz"
secondName = "kütüphanesi"
print(place + " " + secondName)


satır = 500
print(satır)     #buranın sonucu bilindiği gibi 500 çıkar yani alttaki toplama bunu etkilemez
satır += 100*4
print(satır)     #buranın sonucu yukarıdıkinden farklı olarak 900 çıkar.Her kod kendinden sonraki satırları bağlar




customerName = "Ahmet"
customerSurname = "Bakan"
customerNameSurname = customerName + " " + customerSurname
customerDateOfBİrth = 2010
print(2021 - customerDateOfBİrth)


order1 = 150
order2 = 100.75
order3 = 570
print(150 +100.75 + 570)

print(order1 + order2 + order3)

total = order1 + order2 + order3
print("Total:", total)

