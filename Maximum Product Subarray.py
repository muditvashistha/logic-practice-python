# Given an array that contains both positive and negative integers, the task is to find the product of the maximum product subarray. 
# nput: arr[] = {6, -3, -10, 0, 2}
# Output:  180
# Explanation: The subarray is {6, -3, -10}

# Input: arr[] = {-1, -3, -10, 0, 60}
# Output:   60
# Explanation: The subarray is {60}



def max_product_subarray(nums):
    if not nums:
        return 0

    
    current_max = current_min = overall_max = nums[0]

    
    for num in nums[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max
        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)
        overall_max = max(overall_max, current_max)

    return overall_max


nums = [6, -3, -10, 0, 2]
print("Maximum product subarray is:", max_product_subarray(nums))
