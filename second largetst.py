main=[45,2,300,34,12,0]
store=main[0]
length=len(main)
for i in range(length):
    if(main[i]>store):
        store=main[i]
    else:
        continue

max_index=main.index(store)
main.pop(max_index)
secondlargest=main[0]
for i in range(length-1):
    if(main[i]>secondlargest):
        secondlargest=main[i]
    else:
        continue
print("The largest number in the list is:-",end=" ")
print(store)
print("\n")
print("The second largest number in the list is:-",end=" ")
print(secondlargest)