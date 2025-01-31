"""
x = 5
y = 10


#x = input("1.sayı:")
#y = input("1.sayı:")
"""



"""
toplam = int(x) + int(y)

print(toplam)
"""




"""
a = input("name: ")
b = input("surname: ")

toplam = a + " " + b 
print(toplam)
"""




"""
π = 3.14
r = float(input("yarıçap kaç olsun: ")) #
Alan = π * (r ** 2)
çevre = 2 * π * r
print("Alan: ", str(Alan) + "çevre: ", str(çevre))
"""




"""
#karşıdan kardeş sayısı ve gelir istiyorum ve bu sayede kişi başına düşen geliri hesaplayacağım:

a = float(input("kardeş sayısı: "))
b = float(input("aile gelir toplamı: "))

print(b / a)
"""





"""
m = float(input("kütle: "))
a = float(input("ivme: "))
f = m * a
print(f)
"""




"""
m = float(input("kütle: "))
v_0 = float(input("ilk hız: "))
v_1 = float(input("anlık hız: "))
h = float(input("anlık yerden yükseklik: "))
g = 10

e = (1 / 2 * m * v_1**2) + m * g * h 
print(e)
"""





"""
m = input("kütle: ")
m_float = float(m)

v_0 = input("ilk hız: ")
v_0_float = float (v_0)

v_1 = input("anlık hız: ")
v_1_float = float (v_1)

h = input("anlık yerden yükseklik: ")
h_float = float (h)

g = 10
g_float = float (g)

e = ( 1 / 2 * m_float * v_1_float**2) + m_float * g_float * h_float 
print(e)
"""




"""
v = float(input("anlık hız: "))
r = float(input("yol yarıçap: "))
m = float(input("araba kütlesi: "))
sk = 0.6
π = 3
g = 10

f = m * v**2 / r          #savrulma kuvveti
s = sk * m * g            #sürtünme kuvveti

if(f > s):
    print("takla atar")
else:
    print("güvenli geçiş")
"""




"""
m = input("kütle: ")
m_float = float(m)

v_0 = input("ilk hız: ")
v_0_float = float (v_0)

v_1 = input("anlık hız: ")
v_1_float = float (v_1)

h = input("instant ground clearance: ")
h_float = float (h)

g = 10
g_float = float (g)

e = ( 1 / 2 * m_float * v_1_float**2) + m_float * g_float * h_float 
print(e)
"""




v = float(input("instantaneous speed: "))
r = float(input("radius of the road: "))
m = float(input("mass of the car: "))
sk = 0.6
π = 3
g = 10

f = m * v**2 / r          
s = sk * m * g  

if(f > s):
    print("skid")
if(s > f):
    print("safe")


