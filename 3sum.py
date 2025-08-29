# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

x = [-1,0,1,2,-1,-4]
x.sort()

n=len(x)
answer=[]

for i in range(n):
    if x[i]>0:
        break
    elif i>0 and x[i]==x[i-1]:
        continue

    low=i+1
    high=n-1

    while low < high:
        sum=x[i]+x[low]+x[high]

        if sum==0:
            answer.append([x[i],x[low],x[high]])

            low=low+1
            high=high-1

            while low<high and x[low]==x[low-1]:
                low=low+1
            while low<high and x[high]==x[high+1]:
                high=high-1
        elif sum<0:
            low=low+1
        else:
            high=high-1

print(answer)


#thank you greg hogg! (his video helped solving this!)
