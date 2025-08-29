main=[1,2,3,34,12,0]
store=main[0]
minimum=21378
print(store)
length=len(main)
count=main[length-1]
for i in range(length):
    if(main[i]>store):
        store=main[i]
    else:
        continue
for i in range(length-1):
    
    if(main[i]<main[i+1]):
        if main[i]<minimum:
            minimum=main[i]
        else:
            continue
if(count<minimum):
    minimum=count
print("The bigges element in the provided list is:-",end=" ")
print(store)
print(minimum)