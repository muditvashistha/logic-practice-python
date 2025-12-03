# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

class Solution(object):
    def backspaceCompare(self, s, t):
        stack1 = []
        stack2 = []

        for i in s:
            if not stack1 and i == "#":
                pass
            else:
                if stack1 and i == "#":
                    stack1.pop()
                    continue
                stack1.append(i)
        
        for i in t:
            if not stack2 and i == "#":
                pass
            else:
                if stack2 and i == "#":
                    stack2.pop()
                    continue
                stack2.append(i)
        
        return (stack1 == stack2)

        