
# Listeler içerisine birden fazla türden değişken alabiliyordu, sıralıydı ve eğiştirilebilirdi
# Tuple'ın en önemli farklılığı DEĞİŞTİRİLEMEZ olmasıdır
# Bazı durumlarda veri yapıları sabir dursun ve ben değişip değişmeyeceğini endişe etmiyeyim tarzında istemler karşısında kullanılır

# Yine list'lerdeki gibi iki farlı oluşturma yolu vardır:
    #1: () ile -> ("ali", "veli", 1, 3)
    #2: virgül ile -> "ali", "veli", 1, 3
    
# Tuple'da tek elemanlı bir tuple oluşturmak istiyorsak yanına virgül koymamız lazım:
t = ("ali",)    #Yoksa String tipinde algılar

t = ("ali", "veli")



# Yine erişim işlemleri de List'ler gibi gerçekleştirilir:
t[1]

t[:1]
