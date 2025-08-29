x=int(input("Enter the number of elements in the list  "))
print("\n")
l1=[]
for i in range(x):
    element=int(input("Enter the element"))
    l1.append(element)
print("The original list is:-",end=" ")
print(l1)
print("\n")
p=len(l1)
print("And thr reverse of the list is:-",end=" ")
print("[",end=" ")
for j in range(p-1,-1,-1):
    print((l1[j]),end=" ")
print("]")    
