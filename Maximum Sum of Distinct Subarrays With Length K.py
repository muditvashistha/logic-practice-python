# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:

# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.

#Brute forcing my way through this problem (takes too much time for large inputs)

# class Solution(object):
#     def maximumSubarraySum(self, nums, k):
#         if not nums:
#             return 0
#         res = 0
#         for i in range(0 , len(nums)-(k-1)):
#             if len(set(nums[i:(i+k)])) == len(nums[i:(i+k)]):
#                 if res < sum(nums[i:(i+k)]):
#                     res = sum(nums[i:(i+k)])
#         return res

from collections import defaultdict
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        l = 0
        res = 0
        count = defaultdict(int)
        curr = 0

        for r in range(len(nums)):
            curr = curr + nums[r]
            count[nums[r]] = count[nums[r]] + 1

            if (r-l+1) > k:
                count[nums[l]] = count[nums[l]] - 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                curr = curr - nums[l]
                l = l + 1
            
            if len(count) == (r-l+1) == k:
                res = max(res , curr)
        return res







        


      