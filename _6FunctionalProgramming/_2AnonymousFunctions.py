

def sum1(a,b):
    return a+b


sum2 = lambda a,b: a+b


sum1(4,6)
sum2(4,6)






# Daha complex bir örnek:
myList = [('b', 3), ('a',8), ('d',12), ('c',1)]
sorted(myList, key= lambda x: x[1])



