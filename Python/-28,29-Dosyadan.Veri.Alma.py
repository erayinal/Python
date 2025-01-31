# Read : Dosyanin içinde ne var ne yok almamızı sağlar
# Readline : Dosyanın satırlarını basmamızı sağlar.İstersek alt alta yazarak, yazdığımız satır kadar dosya satırı yazdırabiliriz
# Readlines : Dosyanın hepsini liste haline getitir ve o şeklinde yazdırır. Buna bir değişken atayarak istediğimiz satırı bastırabiliriz.



dosya = open("Software" , "r")   #Böyle bir dosya VARSA onu okunacak tür haline(read) getirir.Eğer dosya yoksa çalışmaz


"""
print(dosya.read() )        #Read: Dosyanın içinde ne varsa almamızı sağlar
"""





"""
print(dosya.readline() )     #Readline: Dosyanın en başındaki satırı bastırır.Diğer satırları bastırmak istersek alt alta yazmamız lazım.Aşağıda 2.satırıda basalım:
print(dosya.readline() )     #Kötü yanı sıralı olması, yani 1. ve 3.satırı yazamazsınız, 2.yi de yazdırmak zorundasınız eğer 3.yü yazdırmak istiyorsanız
"""





"""
#print(dosya.readlines() )   #Dosyanın her bir satırını liste haline getirir ve aynı satıra yazar

liste = dosya.readlines()   #İstediğimiz satırı yazmak için dosyayı readlines yapıp sonrasında bir değişken atarız ve oradan istediğimiz liste elemanını seçeriz
print(liste[2])             #Burada listenin istediğimiz satırını yazdırabiliriz 
"""



























"""

############   PRATİK   ###########




file = open("Software" , "r")       #Eğer yazdığımız dosya var ise onu okunacak tür haline getirir

değişken = dosya.readlines()        # Okunabilecek hale gelen dosyanın her bir satırını liste türüne çevirir

print(değişken[0] )

"""





##############   PRATİK 2  ############

# Bu pratikte önce bir dosya açıcaz ve daha sonrasında bu dosyanın içindekişleri parça parça yazdırıcaz: Let's start

"""
blabla = open("Pratik" , "a")          #Öncelikle dosyamızı append türünde(a) açıyoruz ve sonra kullanabilmek için bir değişken atıyoruz(blabla)
blabla.write("Sevdaya düştü gitti")   #Dosyaya bir şeyler yazıyoruz
blabla.write("\nömrüm ömrüm")           #Dosyanın 2. satına geçip bir şeyler daha yazıyoruz


blabla = open("Pratik" , "r")          #Daha sonrasında dosyayı okunabilecek hale getiriyoruz
listehalinehetirilecekdosya = blabla.readlines()  #Dosyayı liste haline getirip değişken atıyoruz ki sonrasında kullanabilelim
print(listehalinehetirilecekdosya[0])      #Print içine belirlediğimiz değişken adını yazıp köşeli parantez içinde istediğimiz satırını yazıyoruz

"""














######################################################################################
######################################################################################
######################################################################################



#Biz başka bir yöntemle de dosya açabiliriz ve bu yöntem sonradan biz unutsak bile dosyanın kapanmasını sağlar 

"""
with open("dosyacık" , "a") as gluglu:     #Adı dosyacık olan append(a) türünde bir dosya açtık ve bir değişken atadık(gluglu)
    gluglu.write("Ocağım söndü")           #İçine her zamanki gibi bir şeyler saçmaladık
    gluglu.write("\nNasıl beladır")
"""

""" 
with open("dosyacık" , "r") as değişkencik:      #Önceden olan dosyayı okunacak tür haline getirdik
    değişkencik.seek(5)                          #DOsyada imlecin 5.bayt'a (harfe) gelmesini seek ile istedik.(Her harfin bir bayt olduğunu hatırlayalım)
    print(değişkencik.read())                    #Burada yukarıda 5.harfe getirdiğimiz imleçten sonrasını yazmasını istedik 
    print(değişkencik.read(12))                  #Burada ise 5.harften sonra 12 harf yazmasını istedik 
"""

"""
with open("folloşlar dosyası" , "a") as variable:
    variable.write("boşver loui gucci prada")
    variable.write("\nbaba ben senin için")


with open("folloşlar dosyası" , "r") as variable2:
    variable2.seek(5)
"""






