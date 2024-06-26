# Given a sorted array arr[] (may be distinct or may contain duplicates) of size N that is rotated at some unknown point, the task is to find the minimum element in it. 

# Input: arr[] = {5, 6, 1, 2, 3, 4}
# Output: 1
# Explanation: 1 is the minimum element present in the array.

# Input: arr[] = {1, 2, 3, 4}
# Output: 1

arr=[1, 2, 3, 4]
temp=arr[0]

for x in range(len(arr)):
    if arr[x]<temp:
        temp=arr[x]
print(temp)


