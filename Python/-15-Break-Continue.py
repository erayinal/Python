### BREAK ### : Yazıldığı yerde döngüyü kırar

"""
kullanıcı = "inaleray"
şifre = 123234


while True:
    username = input("Username: ")
    password = input("Password: ")

    if((username != kullanıcı) and (password != şifre)):
        print("Wrong password or username...")

    else:
        print("Welcome...")
        break                              #Break kullanarak döngüyü sonlandırdık
"""















### CONTİNUE ### :  Döngüyü yazılıdığı yerden alır ve tekrar başa sardırır. 

"""
liste = [2, 3 , 4]

for i in range(1,10):
    
    if(i in liste):
        continue          
    
    print(i)                #Continue'yi buraya bırakırsak runladığımızda 2,3,4ü basmaz çünkü 2,3,4e gelince contunei onu başa atar 

"""






"""
i = 0

while(i < 10):
    if(i == 2):
        continue

    i = i + 1

    print(i)

"""
#Continue kullanmak tehlikelidir mesela yukarıda continue yüzünden döngü sonsuza girdi. Sadece gerek varsa kullanılmalı yoksa "break" kullanılmalı

 


 