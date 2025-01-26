

 #Listeler:
     # İki tür vardır birincisi []
     #İkincisi ise list()

    
grades = [20, 30, 10, "AA", "BB"]


# YAZDIRMA
grades[:3] #Baştan başlar ve 3. index dahil olmayacak şekilde 3e kadar olan elemanları verir
grades[2:] #2. indexten (3. elemandan) başlar ve listenin kalan elemanlarını yazar



# EKLEME
grades + [66]  #66 listeye eklenir ama kalıcı olarak eklenmez yani o anlık bir şeydir
grades = grades + [66]  #Ancak bu şekilde kalıcı olarak eklenir
grades.append("BA")

grades.insert(0, "10")     #Bu şekilde istediğimiz indexe eleman ekleyebiliriz
grades.insert(len(grades), 12)    #Sona ekler



# SİLME
grades.remove("BA")
grades.pop(2)   #2. indexi siler
#del grades[2] #2. indexi yani 3. elemanı siler yani listeden kaldırır




# DEĞİŞTİRME
grades[0:3] = 5, 15, 20  #Bu şekilde birden fazla liste elemanının değiştirebiliriz



# DİĞER İŞLEMLER
grades.count(10)    #Liste içerisinde kaç tane 10 olduğunun sayısını verir
spareList = grades.copy()
grades.extend(spareList)    # spareList'in elemanlarını grades'e ekler
grades.index("AA")    #10'un hangi indexte olduğunu bize verir
grades.reverse()    #Bu method ile listeyi tersten verir
#grades.sort()   #Listeyi sortlar ama listede hem integer hem de string olduğu için bu satır hata verir
grades.clear()




