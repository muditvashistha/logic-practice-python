# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]



class Solution(object):
    def findWords(self, words):
        words_list=[]

        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")

        for i in words:
            if i.lower()[0] in row1:
                if set(i.lower()) | row1 == row1:
                    words_list.append(i)
                else:
                    continue
            elif i.lower()[0] in row2:
                if set(i.lower()) | row2 == row2:
                    words_list.append(i)
                else:
                    continue
            elif i.lower()[0] in row3:
                if set(i.lower()) | row3 == row3:
                    words_list.append(i)
                else:
                    continue
        return words_list

        




