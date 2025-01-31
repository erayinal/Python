"""
def geometri(şekil):

    if( len(şekil) == 3 ):              #len() ; değişkenin eleman sayısını verir
        a = şekil[0]
        b = şekil[1]
        c = şekil[2]

        if( (a+b) > c and (a+c) > b and (b+c > a)  ):
            if(a == b  == c ):
                print("Eşkenar üçgen")

            elif((a==b and a!=c) or (b==c and b!=a) ):
                print("İkizkenar üçgen")

            else:
                print("Çeşitkenar Üçgen")




    if( len(şekil) == 4 ):

        a = şekil[0]
        b = şekil[1]
        c = şekil[2]
        d = şekil[3]

        if(a == b and c == d and a != c):
            print("Dikdörtgen")

        elif(a == b == c == d):
            print("Eşkenar Dörtgen")

        else:
            print("Herangi bir dörtgen değil")







while True:
    eleman_sayısı = int(input("Kaç kenarı var: "))

    if(eleman_sayısı == 3):
        a = int(input("a kenar uzunluğu: "))
        b = int(input("b kenar uzunluğu: "))
        c = int(input("c kenar uzunluğu: "))

        geometri([a,b,c])     #Buranın içini yukarıdaki input istediklerimize göre doldururuz
        


    elif(eleman_sayısı == 4):
        a = int(input("a kenar uzunluğu: "))
        b = int(input("b kenar uzunluğu: "))
        c = int(input("c kenar uzunluğu: "))
        d = int(input("d kenar uzunluğu: "))
        geometri([a,b,c,d])
        

    else:
        print("Üçgen veya dörtgen değil...")
        
    break


"""















###  PRATİK  ###


def geometri(şekil):
    if(len(şekil) == 3):
        
        a = şekil[0]
        b = şekil[1]
        c = şekil[2]

        if( (a+b)>c and (a+c)>b and (b+c)>a):

            if(a == b == c):
                print("Eşkenar Üçgen")

            elif( (a == b != c) or (a != b == c) or (b == c != a)):
                print("İkizkenar üçgen")

            else:
                print("ÇEşitkenar üçgen")



    if( len(şekil) == 4 ):

        a = şekil[0]
        b = şekil[1]
        c = şekil[2]
        d = şekil[3]

        if(a == b == c == d):
            print("EŞkenar dörtgen")

        elif(a ==b and c == d and a != c):
            print("Dikdörtgen")

        elif( a != b != c != d):
            print("dörtgen değil")







while True:
    kenar_sayısı = int(input("Kaç kenarlı: "))

    if ( kenar_sayısı == 3 ):

        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))

        geometri([a,b,c])              #Burada köşeli parantez olmalıdır


    elif( kenar_sayısı == 4):

        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))

        geometri([a,b,c ,d])           #Burada köşeli parantez olmalıdır

    break
