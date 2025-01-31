"""

def içerisine foksiyon adı girilerek ( F.E: def eray() ) fonsiyon altında işlemler tanınlanır ve bunu istediğimiz zaman kullanmamız sağlanır

def merhaba():
    print("Merhaba dünya")




merhaba()

"""







"""
def faktöriyel():

    faktöriyel = 1 

    while True:

        sayı = int(input("Pozitif bir sayı giriniz: "))

        if(sayı <= 0):
         print("pozitif bir sayı giriniz")

        else:
            for i in range(1 , sayı+1):
                print(i , ". döngüde yapılan iş: " , i , "*" , faktöriyel , " = " , i * faktöriyel)
                faktöriyel = faktöriyel * i
            print("sonuç: " , faktöriyel)
            break

"""











"""
def faktöriyel(numara):
    faktöriyel = 1 

    for i in range(1 , numara+1):
        faktöriyel = faktöriyel * i

    print("sonuç: " , faktöriyel)



sayı = int(input("Pozitif sayı girniz: "))
faktöriyel(sayı)     #Burada fonsiyonu çağırdık ve sayıyı karşıdan almak için inputlu olan "sayı"yı yazdık.İstesek direkt sayı da yazabiliriz. F.E : faktöriyel(4)



faktöriyel(4)      #Burada fonsiyonu çağırıp içine kendi istediğimiz sayıyı da yazabiliriz.Yukarıdan farkı orada sayıyı karşı taraf belirliyordu, burada ise biz.

"""










"""
def faktöriyel(numara):
    faktöriyel = 1 

    for i in range(1 , numara+1):
        faktöriyel = faktöriyel * i

    #print("sonuç: " , faktöriyel)       #Burada bi üsttekinden farklı olarak sonucu direk bastırmak yerine return atamak için bu işlevsiz hale getirdik
    return faktöriyel                    #Burada faktöriyeli print olarak değilde "return" olarak yazarak sonucu sonradan değişken aracılığıyla kullanmamızı sağlar




sayı = int(input("Pozitif sayı girniz: "))
a = faktöriyel(sayı)                    #Burada fanksiyonu tekrar çağırıp bir değişken atadık ki işimiz oldukça bu sonuçla tekrar tekrar işlem yapabilelim                    
                                        #Fonsiyon yani burada "kökbul" içine karşıdn ne istiyorsan onu yazacaksın

print(a) 

"""










"""
def kökbul(numara):
    a = numara ** (1/2)
    return a



sayı = int(input("sayı kaç olsun: "))
x = kökbul(sayı)      #Fonsiyon yani burada "kökbul" içine karşıdan ne istiyorsan onu yazacaksın

print(x)         

"""









"""
#ax **2 + bx + c 

def kökbul(a,b,c):

    delta = b*b - 4*a*c

    if(delta < 0):
        print("Kökleri yok")
        return

    else:
        x1 = (-b - (delta*0.5)) / 2*a
        x2 = -x1


    return(x1 , x2)



a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))



k = kökbul(a,b,c)


print(k)

"""


    
    






