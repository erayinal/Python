
# Object Oriented

class Engineer():
    name = "Eray İnal"
    age = "23"
    skills = ["Java"]



eray = Engineer()
eray.skills
eray.skills.append("Swift")


ahmet = Engineer()
ahmet.skills #Aslında biz Swift dilini Eray için eklemiştik ahmet için değil ama Ahmet de artık swift biliyor gibi gözüküyor
#Yani başka bir instance üzerinden yapılan bir değişiklik diğer sınıfları da etkiler




#Peki bunu gidermek için ne yapmalıyız: Sınıfın tanım şeklini değiştirmeliyiz. Bunun adı Örneklem Özellikleri
class NewEnginner():
    company = "Google"
    def __init__(self):
        self.name = ""
        self.skills = []
#Yukarıdaki tanımlama şekilden company her instance için geçerli yani ortaktır ve herkes Google'da çalışıyordur ama skiller farklı 
        
mustafa = NewEnginner()
mustafa.skills.append("Python")
mustafa.skills

salih = NewEnginner()
salih.skills








# ÖRneklem Methodları
class NewEnginner2():
    company = "Google"
    def __init__(self):
        self.name = ""
        self.skills = []
        
    def appendSkill(self, newSkill):
        self.skills.append(newSkill)


ne = NewEnginner2()
ne.appendSkill("R")
ne.skills 















