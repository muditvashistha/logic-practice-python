#Given an array arr[] of integers, the task is to find the Next Greater Element for each element of the array in order of their appearance in the array.
# Note: The Next Greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

# Examples: 

# Input: arr[] = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn’t exist, it is -1.


arr=[124,126,1,2]
x=len(arr)
result=[-1]*x


for i in range(x):
    for j in range(i+1, x):
        if arr[j] > arr[i]:
            result[i]=arr[j]
            break
print(result)
