# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"

# Output: ["sweet","sour"]

# Explanation:

# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:

# Input: s1 = "apple apple", s2 = "banana"

# Output: ["banana"]





from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1_list = s1.split()
        s2_list = s2.split()

        main_list = s1_list + s2_list
        result=[]
        dictionary=Counter(main_list)
        
        
        for i in dictionary:
            if dictionary[i]==1:
                result.append(i)
        return result

        