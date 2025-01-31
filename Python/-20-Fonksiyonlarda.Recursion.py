"""
### Without Recursion: ###

def topla(liste):

    toplam = 0

    for i in liste:
        print(i , ". döngüde yapılan iş: " , toplam , "+" , i , "=" , toplam+i)
        toplam = toplam + i

    return (toplam)


print(topla([1,2,3,4]))         #Parantez içine yazdıklarımız ilk satıda bulunan "liste" yerine geçti










### Recursion = Özyineleme ### 

def topla(liste):

    if(len(liste) == 0):
        return 0

    else:
        return(liste[0]) + topla(liste[1:])      #Burada fonsikyonu tekrar çağırarak Recursion yani Özyineleme yaptık.



print(topla([1,2,3,4]))                #Burada listenin içeriğini belirledik










def aa(listem):

    if(len(listem) == 0):
        return 0 

    else: 
        return(listem([0]) + aa(listem[1:]))




"""







def toplamafonksiyonu(liste):

    sayı = 0

    for i in liste:

        sayı = sayı +i

    return (sayı)




print(toplamafonksiyonu([1,2,3,4,5,6,7]))













def çarpmafonsiyonu (liste):

    sabit = 1

    for i in liste:

        sabit = sabit * i

    return(sabit)




print(çarpmafonsiyonu([1,2,3,4,5]))







