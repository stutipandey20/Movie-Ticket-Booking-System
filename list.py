import numpy as np
l =[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(1,6):
    l1.append("AVA")
    l2.append("AVA")
    l3.append("AVA")
    l4.append("AVA")
l.append(l1)
l.append(l2)
l.append(l3)
l.append(l4)
arr = np.array(l)

print(arr)

r = int(input("ROW: "))
c= int(input("Col: "))
arr[r,c] = "NA"

print(arr)
