# Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets exactly one packet.
# The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.



# Example 1:
# Packets: [3, 4, 1, 9, 56, 7, 9, 12]
# Students: 5
# If we sort this array: [1, 3, 4, 7, 9, 9, 12, 56]
# We could pick:

# [1, 3, 4, 7, 9] → Difference: 9-1 = 8
# [3, 4, 7, 9, 9] → Difference: 9-3 = 6
# [4, 7, 9, 9, 12] → Difference: 12-4 = 8
# [7, 9, 9, 12, 56] → Difference: 56-7 = 49

# The best option here would be the second one with a difference of 6.
# Example 2:
# Packets: [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Students: 3
# Some possible selections:

# [10, 20, 30] → Difference: 30-10 = 20
# [20, 30, 40] → Difference: 40-20 = 20
# [30, 40, 50] → Difference: 50-30 = 20
# [40, 50, 60] → Difference: 60-40 = 20
# [70, 80, 90] → Difference: 90-70 = 20



arr=[3, 4, 1, 9, 56, 7, 9, 12]
arr.sort()
students=5

#creating reference points to compare and update the minimum difference and the solution sub array
sol_arr=arr[0:students]
min_diff=sol_arr[-1] - sol_arr[0]

for i in range(len(arr)-students+1):
     x=arr[i:i+(students)]
     curr_diff=x[-1] - x[0]
     if curr_diff < min_diff:
          min_diff=curr_diff
          sol_arr=x

print(sol_arr)
print(min_diff)