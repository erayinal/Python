"""
string = "Eray İnal"

for i in string:
    yaptırmak istediğimiz işlemler 

"""





"""
a = "eray"

for i in a:
    print(i)        #Burada olay ilk satıra e'yi yazar sonra döngü yapar e'yi geçip r'yi yazar sonra döngü...Yani olay:



#a = "eray"
#a = "e"
#a = "r"
#a = "a"          #Bu 4 satırı olayı anlatmak için yazdım

"""





"""
string = "eray"

for i in string:
    print(i)              #Buraya -i- yerine unutupta -string- yazarsak alt alta 4 tane eray yazdırır...

"""







"""
liste = ["elma" , "armut" , "muz"]

for i in liste:        #Listede eleman eleman alt alta yazar
    print(i)

"""









# print( *range(10) )        #Burada range bize 0dan 10a kadar liste oluşturur.Range'i print ile yazdırabilmek için * şart           
# print( *range(2,10) )      #Burada 2den 10a kadar yazdırır
# print( *range(2,10,3) )    #Burada 2den 10a 3er 3er yazdırır






"""
for i in range(1,10):
    print(i * "*")           #Burada * ile her eleman değeri kadar "*" basmasını söyledik

"""













#print(i , ". döngüde de yaptığı iş : " ,  faktöriyel , "*" , i , " = " , faktöriyel*i , "= " , i , "!")


"""
faktöriyel = 1


while True:
    sayı = int(input("Pozitif bir sayı giriniz: "))

    if(sayı <= 0):
        print("Lütfen pozitif sayı giriniz...")

    else:
        for i in range(1, sayı+1):
            print(i , ". döngüde de yaptığı iş : " ,  faktöriyel , "*" , i , " = " , faktöriyel*i , )
            faktöriyel = faktöriyel * i
            
        
        print("faktöriyel:" , faktöriyel)
        break

"""










for i in range (5):
    print(i * "*")
    i =- i





