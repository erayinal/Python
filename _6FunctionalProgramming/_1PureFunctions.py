
# Birinci sınıf nesneler
# Yan etkisiz fonksiyonlar (stateless, input-output)
# Yüksek seviye fonksiyonlar
# Vektörel operasyonlar




    ## Yan etkisiz(Pure) fonksiyonlar (stateless, input-output)
    
# Örnek 1 : Bağımsızlık
a = 9

def impureSum(b):
    return a + b


def pureSum(m,n):
    return m+n

#İlk tanımladığımız impureSum fonksiyonu pure değildir çünkü dışarıdaki bir değişkene bağlı yani o değişirse sonuç da her zaman değişir
#Ama ikinci pureSum fonksiyonu pure'dur çünkü dışarıdan bir variable'ye bağlı değil









# Örnek 2 : Ölümcül yan etkiler
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)


lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

#Yukarıda read yapmadan önce dosyayı okumadığı için line'ları boş ve sayısını 0 olarak yazdıracak
#Ama aşağıdaki read() ile okuduktan sonra line'ları bize tek tek yazacak ve satır sayısını verecek
lc.read()
print(lc.lines)
print(lc.count())
#Yani başka bir fonksiyonu çalıştırdığımızda değerlerin değiştiğini gördük
#Bu yukarıda yaptığmız OOP programlama örneğiydi şimdi ise FunctionalProgramming örneğini yapalım


# Functional Programming
def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

exLines = read('deneme.txt')
linesCount = count(exLines)
linesCount

#Yukarıda iki tane birbiririnden bağımsız iki tane fonksiyon yazdık ve girdi değişmediği sürece çıktı değişmeyecek 
#Yani başka bir kod kullanımı bu output'u değiştirmeyecek eğer input değişmemişse






