# Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 

# Input: arr = {-2,-3,4,-1,-2,1,5,-3}
# Output: 7
# Explanation: The subarray {4,-1, -2, 1, 5} has the largest sum 7.

# Input: arr = {2}
# Output: 2
# Explanation: The subarray {2} has the largest sum 1.

arr = [-2,-3,4,-1,-2,1,5,-3]
sum=0
maxi=arr[0]

for i in range(len(arr)):
    sum=sum+arr[i]

    maxi=max(maxi,sum)

    if sum<0:
        sum=0

print(maxi)