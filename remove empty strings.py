names = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("The list at present is:- ",end=" ")
print(names)
ind=0
while ind< len(names):
    if(names[ind]==""):
        names.pop(ind)
    else:
        ind=ind+1
    
print("The list with removed empty strings is:- ",end=" ")
print(names)