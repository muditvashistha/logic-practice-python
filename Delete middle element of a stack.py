# Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure.

# Input  : Stack[] = [1, 2, 3, 4, 5]
# Output : Stack[] = [1, 2, 4, 5]

# Input  : Stack[] = [1, 2, 3, 4, 5, 6]
# Output : Stack[] = [1, 2, 4, 5, 6]

stack=[]
n=int(input("Enter the number of elements for the stack"))

# creating the stack
for i in range(n):
    x=int(input("Enter the number"))
    stack.append(x)




# function for removing the middle term
def remove_middle(x):
    mid_point=(len(x)-1) // 2
    del x[mid_point]
    print("Stack after removal of the middle element is\n")
    print(x)


remove_middle(stack)