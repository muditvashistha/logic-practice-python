x=int(input("Enter the number of elements--> "))
l=[]
for i in range(0,x):
    y=int(input("Enter the element--> "))
    l.append(y)
print("\n")
print("The original list is:-",end=" ")
print(l)
max=len(l)
temp=l[0]
temp2=l[max-1]
l[max-1]=temp
l[0]=temp2
print("\n")
print("The list after the swapping of the first and last digits is:-",end=" ")
print(l)