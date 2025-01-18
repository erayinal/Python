# OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])




# Vektörel Operasyonlar - FP

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b








##################################################################

                # MAP & FILTER & REDUCE


    # MAP 
list1 = [1,2,3,4,5]
for i in list1:
    print(i+10)
    

# Yine yukarıda yaptığımız aynı aynı operasyonu aşağıda daha kolay şekilde yapalım  
list( map(lambda x: x + 10, list1) )
# Aslında map fonksiyonu bize verilen bir nesnenin üzerinde belirli bir fonksiyonu çalıştırma imkanı verir





    # FILTER
list2 = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x%2==0, list2))





    # REDUCE - indirgeme

from functools import reduce
list3 = [1,2,3,4]
reduce(lambda a,b: a+b, list3)











