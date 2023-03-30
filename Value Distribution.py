import numpy as np
#starting capital.
x = int(input("Enter Starting Capital:  "))

#percentage in starting capital.
lisperx = []

l = int(input("Enter number of holder:  "))
print("Enter percentage of each holder in order.")
for i in range(0,l):
    ele = int(input())
    lisperx.append(ele)
print(lisperx)

#total percentage of starting capital.
perx = sum(lisperx)

#check
if perx != 100:
    print("Error in percentage of starting capital.")
else:
    print(perx)

#new added worth.
intlisy = []

print("Enter new individual worth of each holder in order.")
for i in range(0,l):
    ele = int(input())
    intlisy.append(ele)
lisy = np.array([float(a) for a in intlisy])
print(lisy)

#check
if len(lisy) != len(lisperx):
    print("Error in entry list.")
else:
    y = sum(lisy)
    print(f"Total of new added worth is {y}.")

#total new worth.
z = x + y
print(f"New total worth is {z}.")

#calculation for delta.
h = 100*(float(1/x) - float(1/z))

δ = float(y)*h
exδ = float(δ)/float(len(lisy))
print(δ, exδ)#removable

#calculation of delta list.
lisδ = np.array(np.multiply(h,lisy))
print(lisδ)

#calculation of new value of each percentage holder.
reduclisδ = np.array(np.subtract(exδ,lisδ))
print(reduclisδ)

modx = np.subtract(lisperx, reduclisδ)
print(modx)

#check
if sum(modx) != 100:
    print("Error in Final percentage calculation.")
else:
    print(modx)



