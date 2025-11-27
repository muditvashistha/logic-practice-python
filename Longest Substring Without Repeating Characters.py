# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = defaultdict(int)
        l=0
        curr=0
        max_len=0
        for r in range(len(s)):
            count[s[r]] = count[s[r]] + 1
            curr = curr + 1

            while count[s[r]] > 1:
                count[s[l]] = count[s[l]] - 1
                l = l + 1
                curr = curr - 1
            
            if curr >  max_len:
                max_len = curr
        return max_len
    
        