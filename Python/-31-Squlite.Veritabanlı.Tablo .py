# #Bu veritabanı sunucusuz yani internetsiz kullanılabilir



import sqlite3

con = sqlite3.connect("dersler.db")   #Burada dersler.db adında bir database yoksa oluşturacak eğer var ise ona bağlanacak  

cursor = con.cursor()                 



def tabloolustur():
    cursor.execute("CREATE TABLE ")  





