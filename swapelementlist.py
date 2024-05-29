x=int(input("Enter the number of elements of the list--> "))
leest=[]
for i in range(0,x):
    y=int(input("Enter the element--> "))
    leest.append(y)
max=len(leest)
while True:
    while True:

        pos1=int(input("Enter Position Number that is to be swapped with the element of the other position--> "))
        if(pos1>max+1):
            print("Position does not exist in the list!")
        else:
            break

    while True:

        pos2=int(input("Enter the second position--> "))
        if(pos2>max+1):
            print("Position does not exist in the list!")
        else:
            break
    if(pos1==pos2):
        print("Both positions are the same, cannot swap!")
    else:
        break


temp1=leest[pos1-1]
temp2=leest[pos2-1]
print("\n")
print("The original list is:-",end=" ")
print(leest)
print("\n")
leest[pos2-1]=temp1
leest[pos1-1]=temp2
print("The list after swapping the elements is:-  ")
print(leest)











