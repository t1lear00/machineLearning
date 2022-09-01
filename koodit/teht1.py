'''Tee python skripti tiedosto, jossa luot 
lista,tuple,set ja dictionary muutujat. 
Laita jokaiseen 3 elementtiä'''

#python list



a = [1, 5.8, "string"]
print(a[1])
print(a, type(a))
a.append("testi")
#print(a)


#python tuple
b = (3, 4.5, "tuple")
print(b, type(b))
print(b[1])

#python set
c = {"on",1,-1}
print(c, type (c))
c.discard("on")
c.discard(-1)
print(c)

#python dictionary
d = {1:"a",True:2, 4.5:"f"}
print(d, type(d))
print(d[1])