# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_string = min(strs ,  key=len)
        prefix = ""
        for i , ch in enumerate(shortest_string):
            for x in strs:
                if x[i] != ch:
                    return prefix
            prefix = prefix + ch
        return prefix






