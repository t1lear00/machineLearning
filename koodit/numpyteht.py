import numpy as np

a = np.arange(25).reshape(5,5)
print(a)

print("\n")

print(a[0:,1::2]) #red
#print(a[0:,1:4:2])
#print(a[0:,1::2])
#print(a[0:-1,1:-1:2])
print("\n")
print(a[4])#yellow

print("\n")

#print(a[1::2,0::2])#blue
print("\n")
print(a[-2::-2,-3::-2])
print("\n")
print(a[1:4:2,0:3:2]) # rivit 1-4 kahden välein, columnit 0-3 kahden välein



