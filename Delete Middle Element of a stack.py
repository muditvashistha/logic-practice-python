# Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure.

# Input: s = [10, 20, 30, 40, 50]
# Output: [50, 40, 20, 10]
# Explanation: The bottom-most element will be 10 and the top-most element will be 50. Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like [10, 20, 40, 50].


# Input: s = [5, 8, 6, 7, 6, 6, 5, 10, 12, 9]
# Output: [9, 12, 10, 5, 6, 7, 6, 8, 5]


stack=[1, 2, 3, 4, 5]

stack.pop(len(stack)//2)

for i in range(len(stack)-1,-1,-1):
    print(stack[i],end=" ")