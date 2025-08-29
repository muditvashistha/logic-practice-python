# Given an array, print the Next Greater Element (NGE) for every element. 

# The Next greater Element for an element x is the first greater element on the right side of x in the array. 
# Elements for which no greater element exist, consider the next greater element as -1. 

# Examples: 

# Input: arr[] = [ 4 , 5 , 2 , 25 ]
# Output:  4      –>   5
#                5      –>   25
#                2      –>   25
#               25     –>   -1
# Explanation: except 25 every element has an element greater than them present on the right side

# Input: arr[] = [ 13 , 7, 6 , 12 ]
# Output:  13      –>    -1
#                 7       –>     12
#                 6       –>     12
#                12      –>     -1
# Explanation: 13 and 12 don’t have any element greater than them present on the right side


x=[11, 13, 21, 3]
for i in range(len(x)):
    greatest=-1
    for j in range(i+1,len(x)):
        if x[i]<x[j]:
            greatest=x[j]
            break
    print(x[i],"---->",greatest)