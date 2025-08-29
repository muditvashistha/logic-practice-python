# turn every element of the list into its squared values
values=[]
x=int(input("Enter the number of the elements to be entered in the list:- "))
for i in range(x):
    y=int(input("Enter the element"))
    values.append(y)
print("The current list is:- ")
print(values,end=" ")
print("\n")
for i in range(len(values)):
    values[i]=values[i]*values[i]
print("The updated list with all the elements squared are:-",end=" ")
print(values)