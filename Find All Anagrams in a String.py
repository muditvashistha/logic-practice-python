# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        p_counter = Counter(p)
        window = Counter()
        res = []
        for i in range(len(s)):
            window[s[i]] = window[s[i]] + 1

            if i >= len(p):
                if window[s[i-len(p)]] == 1:
                    del window[s[i-len(p)]]
                else:
                    window[s[i-len(p)]] = window[s[i-len(p)]] - 1
            
            if window == p_counter:
                res.append(i-len(p)+1)
        return res


        

    


