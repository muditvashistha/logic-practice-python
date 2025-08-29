# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

s="abcde"
goal="abced"
p=list(s)

class Solution(object):
    def rotateString(self, s, goal):
        p=list(s)
        flag = False
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if ("".join(p) == goal):
                flag=True
                break
            else:
                first=p.pop(0)
                p.append(first)
        return flag


