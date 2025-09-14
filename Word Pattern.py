# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false



class Solution(object):
    def wordPattern(self, pattern, s):
        x=s.strip().split()

        if len(list(pattern)) != len(x):
            return False
        
        dic={}
        used=set()

        for a , b in zip(pattern, x):
            if a in dic:
                if dic[a] != b:
                    return False
            else:
                if b in used:
                    return False
                dic[a] = b
                used.add(b)
        return True
      