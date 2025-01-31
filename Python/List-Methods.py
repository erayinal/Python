"""
letters = ["Eray","Ahmet","Abdullah"]
numbers = [2 , 3 , 5 , 7 , 11]
"""


"""
a = letters[1:3]           #Burada 3.dahil olmayacak şekilde 1.indexten 3.indexe kadar olan üyeleri seçer ve printlersek yazdırır
print(a)
"""




"""
letters[1] = "sadullah"      #Burada lettes listesinde 1.index yerine "sadullah" yerleştirdik
print(letters)
"""





"""
numbers[3] = 13            #Burada numbers'daki 3. index yerine 13 yerleştirdik 
print(numbers)
"""




"""
letters.append("kazım")     #burada letters listesine "kazım"ı ekledik
print(letters)
"""




"""
numbers.insert(3 , 6)      #Burada 3.indexe 6 sayısını kaynatma yapıyor
print(numbers)


numbers.insert(-1 , 113)   #Burada listenin sondan bir öncesine 113 rakamını ekler. Yazılan -1 sondan bir önceki indexi temsil eder
#Eğer sona bir sayı eklemek istersek önceden öğrenmiş olduğumuz .append'i kullanabiliriz
"""




"""
numbers.pop(2)         #Burada numbers'daki 2.indexi siler.
numbers.pop(-1)        #Burada numbers'daki sonuncu indexi siler
print(numbers)
"""





"""
numbers.remove(7)     #Burada listedeki 7'yi silmiş oluruz.Yukarıda index numarasıyla silebileceğimizi burada kendisini yazarak da silebiliriz
print(numbers)
"""




"""
numbers.sort()       #Burada listedeki rakamları sen sıralı yazmasan da küçükten büyüğe sıralar.
letters.sort()       #Burada kelimeleri alfabeye göre ilkten sona sıralar
print(numbers)

numbers.reverse()    #Burada listedeki rakamlaru tersten sıralar(Büyükten küçüğe)
letters.reverse()    #Burada kelimeleri alfabeye göre tersten sıralar
print(letters)
"""




"""
print(len(numbers))       #Burada numbers listesinde kaç eleman olduğunu yazdırabiliriz
print(numbers.count(2))   #Burada 2 rakamından listede kaç tane olduğunu sorarız
"""





"""
numbers.clear()        #Burada numbers listesini temizlemiş oluruz
print(numbers)
"""




#Daha fazla metodu google'a "List methods in Python" yazarak burabiliriz





#[a + "," + b + "," + c + ","]




print("PLAYES REGISTRATION PROGRAM")
a = input("Player Name: ")
b = input("Player Surname: ")
c = input("Player's Team: ")


print("Adı: {} Soyadı: {} Takımı: {}".format(a,b,c))







#print("Name: {} \nSurname: {} \nTeam: {}".format(a, b, c))







