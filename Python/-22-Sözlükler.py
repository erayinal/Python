
sozluk = {"pyton": "güzel bir dil" , "Eray": "Yakışıklı bir erkek "}


 



"""
print(sozluk["Eray"])       #Köşeli parantez içinde istediğimiz kelimenin anlamını yazdırabiliririz


"""



for i in sozluk.items():     #Burada ( ".items()" )  fonksiyonu ile her bir itemi aldık ve printliyerek sözlükteki her kelimeyi alt alta dizer

    print(i)

  




"""
for i in sozluk.items():

    print(i)                        #Burada işlemi anlamak için bunu yazdım

    print(i[0] + " " + i[1])        #Burada sırasıyla kelimelerin anlamlarını tırnak ve iki nokta işareti olmadan düz bir açıklama şeklinde yazdırdık

"""





"""
for i,j in sozluk.items():

    print(i)                 #Burada "i" kelimeyi tutacak            #Bunu anlayalım diye yazdım
    print(j)                 #"j" ise kelimenin anlamını tutacak     #Bunu da anlayalım diye yazdım

    print("---------")     

    print(i + " " + j)

    print("********")

"""






### Pratik ###




"""
dersler = {"Ahmet": "Matematik" , "Ömer": ["Edebiyat" , "Tarih"] , "Eray": ["Fizik" , "Kimya"]}


a = input("İsim: ")

if(a == "Ahmet"):
    print(dersler["Ahmet"])


elif(a == "Ömer"):
    print(dersler["Ömer"])


elif(a == "Eray"):
    print(dersler["Eray"])         #Bu Şekilde yapabilirsiniz ama bu çok uzun ya da aşağıdaki şekilde

"""





"""
dersler = {"Ahmet": "Matematik" , "Ömer": ["Edebiyat" , "Tarih"] , "Eray": ["Fizik" , "Kimya"]}


isim = input("İsim: ")

print("{}'in aldığı dersler: ".format(isim))

for i in (dersler[isim]):             #Yukarıda girilen isim String olduğu için burada da kullanabilirz ki isime göre dersleri bassın

    print(i)

"""










"""
sevgili = {"Nagihan": ["Beni seviyor"] , "Gizem": ["Sıkıldım"] , "Nur": ["Ben hoşlanıyorum ama o hoşlanmıyor"]}

isim = input("İsim: ")

for i in (sevgili[isim]):
    print(i)
"""







"""
gelmeyenler = {"Eray": ["Kargosu gelecekmiş"] , "Mert": ["Bilinmiyor neden gelmedinği"] , "Salih": ["Uyanamadı"]}


for i,j in gelmeyenler.items():

    print(i,j)


"""




