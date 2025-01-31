## Open fonksiyonu 2 tane parametre alır. 1.si dosyanın adı, 2.si ise yapacağımız işlemin komutu
## 2.ci parametrede kullanacağımız 3 çeşit komut vardır: Aslında daha fazla da şimdilik 3 :)
    # "w": Write,  Açtığımız dosya bulunduğumuz dizinde yoksa, yaratır ve bir şeyler yazmamızı sağlar.Varsa onu siler ve yenisini açar.Tehlikeli bir moddur:Önceki bilgileri silebilir
    # "r": Read, olan dosyayı açıp okumamızı sağlar
    # "a": Append. Olan dosyanın içindeki bilgileri değiştirmemizi veya ekleme yapmamızı sağlar. Dosya yoksa yeni dosya açararak içine yeni şeyler yazmamızı sağlar





"""
dosya = open("Yazılım.txt" , "w")      #Bunu çalıştırdığımızda Temeller içinde yazılım adında bir dosya açar.Ve türü "Write" olur 

dosya.write("Naber")     # Burada açılan dosyanın içine "Naber" yazılır

dosya.write("Hİ")     # Burada "Naber" yazısına "Hi"ı ekler. Yukarıyı silip bunu çalıştırsaydık önceden yazılmış "Naber"i olmaz ve sadece "Hi" yazardı 
"""







"""
dosya = open("Yazılım.txt" , "a")     #Dosya açılsın ve türü append olsun ki sonradan yazı yazabilelim veya yoksa oluşturup öyle yazabilelim 

dosya.write(" İyi misin")       #Burada önceden olan "Yazılım" dosyasına "İyi misin" yazısını ekler.W modu olsaydı önce içini siler sonra sadece "İyi misin" yazardı
    #Eğer önceden "yazılım.txt" adlı bir dosya açılmasaydı onu açar içine öyle yazardı.Bu yüzden "w" değilde "a" kullanılmalı
"""








"""
file = open("Software" , "a")      #Software diye bir dosya aç eğer zaten varsa elleme sadece ekleme yapılabilecek hale getir

file.write("selam bebek ben kelebek")

file.write("\nKelebek diye isim mi olur aq")    #Burada alt satıra geçip yazmasını sağladı.(\n) olmasa aynı satıra yazacaktı

"""









