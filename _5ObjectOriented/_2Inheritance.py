

class Employees():
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.age = ""
    


class DataScientist(Employees):     #Parantez içerisine Employees yazarak extends ettik
    def __init__(self):
        self.skills = ""
        


eray = DataScientist()
eray.age = 23











