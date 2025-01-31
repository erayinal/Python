# Dosyada istediğimiz yere yazı yazabilmemiz için metodlar vardır. Birincisi dosyanın sonuna ekleme:


"""
# 1. YOL: Dosyanın sonuna ekleme

with open("Software" , "a") as değişken:
    değişken.write("\nSusuyor konuşmuyorsun, bakıyor donuyorsun")
    print(değişken)               #Bu olayı zaten biliyorduk, bir önceki derste öğrenmiştik

"""
















"""
# 2. YOL: Dosyanını başına ekleme ::

with open("Software" , "r+") as değişken2:     #Burada dosyayı hem yazma hem okuma(r+) türü haline getirdim 
    data = değişken2.read()                    #Dosyayı burada okunacak tür haline getirdim ve bir değişken atadım ki sonra kullanabileyim
    değişken2.seek(0)                          #Burada dosyanın en başına gittim yani imleç artık dosyanın en başında
    data = "başına ekledim artık başındasın:D\n " + data    #Burada eklemek istediğim metni yazdım
    değişken2.write(data)                      #Burada dosyaya metni yazdırdım
 




####### Pratik #######
open("practice" , "a")       #Burada practice adında bir dosya açtık. Yazı ekleyecek olursak bir değişken atayarak yapabiliriz


with open("practice" , "r+") as a:    
    b = a.read()
    a.seek(0)
    b = b + "postscript"
    a.write(b)


"""























"""


# 3.YOL : Dosyanın ortasıne ekleme 


#Başlamadan önce bir liste metodu öğrenmemiz gerekecek 

liste = [1 , 2 , 3 , 4 , 5]
liste.insert(2 , 15)               #Listedeki 2. indexi "15" ile değiştiriyor 
print(liste)



#Öğrendiğimize göre hadi geçelim 3. yola


with open("software" , "r+") as passo:
    x = passo.readlines()
    x.insert(1 , "araya gitme yazık olur\n")
    passo.seek(0)
    passo.writelines(x)





######  PRATİK:  ######

with open("Yazılım.txt" , "r+") as a:
    b = a.readlines()
    b.insert(1 , "acaba oldu mu\n")
    a.seek(0)
    a.writelines(b)

"""








