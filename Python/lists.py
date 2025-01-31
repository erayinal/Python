"""
My_List = ("bir", "iki", "üç", 5 ,True)
print(My_List)


list1 = ("bir" , "iki" , "üç")
list2 = ("dört" , "beş" , "altı")

numbers = list1 + list2
print(len(numbers))
"""



"""
user1 = ("Eray", 20)
user2 = ("İnal" , 15)
users = (user1 , user2)   #araya virgül(,) değilde artı(+) koysaydık tek bir eleman gibi yazacaktı
print(users)              #users'ten sonra köşeli parantez içinde numara yazarsak sadece o parçayı yazdırır
"""



"""
user1 = ("Eray", 20)
user2 = ("İnal" , 15)
users = (user1 , user2)
print(users[0])             #Burada users listesinden 1. parçayı yazdırmak için köşeli parantez içine 0 yazdık
"""











cars = "bmw, mercedes, opel, rolls_roys, porsche"


"""
cars = cars.replace("porsche" , "toyota")
print(cars)
"""



"""
a = cars.find("bmw")
print(a)
"""



"""
cars = cars.split()     #split() yapmasaydık bize sadece index numarası verecekti yani sadece harf, yaprığımız için kelime verir
cars = cars[-2]
print(cars)             #Burada bize sadece listenin sondan ikinci öğesini yazdıracak
"""



"""
cars = list in "araba"    #Burada liste içinde (araba) olup oladığını öğrendik
print(cars)
"""



"""
cars = cars.split()     #Burada arabaları liste haline getirdik getirmezsek aşağıda 3. indexe kadar yazardı
result = cars[0:2]      #Burada arabalar listesinde ilk 3 arabayı yazdıracak hale getirdik. [0:2] = [:2] aynı şeyler
print(result)

result2 = cars[-2:]     #Burada -2den başlayıp başa kadar gitmesini söyledik.
print(result2)

cars = cars.split()      #Bunu yapmazsak aşağıda tersten yazarken "ehcsrop, syor_sllor.." şeklinde giderdi, yaptığımız için "porsche, rolls_roys" şeklinde gidecek
result3 = cars[::-1]     #Burada cars listesini tersten yazdırırız, eğer 1 yazsaydık düz yazardı
print(result3)
"""


"""
cars = cars.split()
cars[2] = "eray" , "ahmet"     #Buarada cars[2]=opel yerine eray ve ahmet yazdırdık
print(cars)
"""


"""
result = cars + ", ford"  ", lamborgini"    #Burada listeye liste ekledik 
print(result)
"""


"""
cars = cars.split()
del cars[-1]                    #Burada arabalardan -1. içeriği sildik, yuakrıda split() yapmasak -1.harfi silerdi 
result = cars
print(result)
"""


