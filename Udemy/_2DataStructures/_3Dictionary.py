# List'ler ve Tuple'lar gibi birden fazla tipi barındırabilir
# List'ler gibi değiştirilebilirdir
# Farkı ise SIRALI DEĞİLDİR

# HashMap'ler gibidir yani key ve value ilişkisi vardır
# Süslü parantezler ile oluşturulur

dict = {"ssd" : "Solid State Driver",
       "VPN" : "Virtual Private Network",
       "DDR" : "Double Data Rate",
       10 : "Anladım"}




# OKUMA
dict["ssd"]




# EKLEME
dict["rom"] = "Read Only Memory"

# DEĞİŞTİRME
dict["ssd"] = "It means 'Solid State Driver'"

# SİLME



#### NOT
# Dictionary'lerde 'KEY' kısmına sabit veri yapıları kullanılır ki değişmesinden kaygı duymayalım
# Yani key olarak bir List kullanamayız ama onun yerine Tuple kullanabiliriz

myTuple = ("P", "J")
dict2 = {myTuple : "Python Java"}


