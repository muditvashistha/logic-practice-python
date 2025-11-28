# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

class Solution(object):
    def isValid(self, s):
        store = {")":"(", "}":"{" , "]":"["}
        stack = []

        for x in s:
            if x not in store:
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    removed = stack.pop()
                    if removed != store[x]:
                        return False
        return not stack


        