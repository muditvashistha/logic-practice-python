# Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai) . ‘ n ‘ vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# The program should return an integer which corresponds to the maximum area of water that can be contained (maximum area instead of maximum volume sounds weird but this is the 2D plane we are working with for simplicity).

# Note: You may not slant the container. 

# Input: array = [1, 5, 4, 3]
# Output: 6
# Explanation : 
# 5 and 3 are distance 2 apart. 
# So the size of the base = 2. 
# Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6

# Input: array = [3, 1, 2, 4, 5]
# Output: 12
# Explanation : 
# 5 and 3 are distance 4 apart. 
# So the size of the base = 4. 
# Height of container = min(5, 3) = 3. 
# So total area = 4 * 3 = 12



array=[1, 5, 4, 3]

x=len(array)

left=0

right=x-1
greatest_area=0

while(left<right):
    area=min(array[left],array[right])*(right-left)

    greatest_area=max(area,greatest_area)

    if(array[left]<array[right]):
        left=left+1
    else:
        right=right-1

print(greatest_area)





# class Solution(object):
#     def maxArea(self, height):
#         x = len(height)
#         l = 0
#         r = x - 1
#         max_area = 0

#         while l < r:
#             w = r - l
#             h = min(height[l] , height[r])
#             area = w * h
#             max_area = max(max_area , area)

#             if height[l] < height[r]:
#                 l = l + 1
#             else:
#                 r = r - 1
#         return max_area

        


