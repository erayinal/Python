"""
Döngü değişkeni başlatma

while(mantık cümlesi):
    yapmak istediğimiz işlem
    artırılacak işlem

"""








"""
i = 0
while(i < 10):
    print("i'nin değeri: " , i)
    i += 2                       #Burayı i = i+2 şeklinde de yazılır ama bu daha cool duruyor..."+" yerine her işlem gelebilir

"""











##!! Break : Döngülerde döngünün sonsuza kadar gitmesini durdurur ve yeniden çalıştırmamamız gerekir



kullanıcıAdı = "erayinleray"
parola = "123234"


while(True): 
    kullanıcı = input("User Name: ")
    şifre = input("Password: ")
    if(kullanıcı == kullanıcıAdı and (parola == şifre)):
        print("Login Succesfull...")
        break                                                    #Break koyduğumuz için bu işlem sağlanırsa döngü duracak
    elif(kullanıcıAdı != kullanıcı):
        print("User wasn't found...")
    elif(kullanıcıAdı == kullanıcı and (şifre != parola)):
        print("Wrong Password..." , "Do you wanna change password? (E/H)" )
        cevap = input()
        if(cevap == "E"):
            yeniparola = input("Yeni parola: ")
            print("Please Wait")
            parola = yeniparola
            print("Password was changed")

        kullanıcıAdı = input("Kullanıcı adı: ")
        şifre = input("Şifreniz: ")

        if(kullanıcıAdı == kullanıcı and (yeniparola == şifre)):
            print("Welcome again")
        else:
            print("Kafanı sikim")
            break

        if(cevap == "H" ):
            print("Please Create New Account...")
    else:
        print("Try again...")








