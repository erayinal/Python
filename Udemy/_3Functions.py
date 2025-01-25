

def square(a):
    print(a*a)
    
    
    
# Default değerler tanımlama
def multiplication(x, y=2):     #Burada fonksiyonu kullanırken y tanımlanmasa bile 1 olarka girilir sadece x girmek zorundayız
    print(x*y)
#multiplication(5)  

#Peki bizim yazmadığımız bir methodda parametrelerin sıralamasını bilmiyorsak nasıl yazarız
multiplication(y=4, x=2) #şeklinde asıl fonksiyon sıralamasından bağımsız şekilde de tanımlayabiliriz 
    








