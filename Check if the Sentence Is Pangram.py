# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


sentence = "thequickbrownfoxjumpsoverthelazydog"
# sentence = "leetcode"
sentence=sentence.replace(" ","")
letters="abcdefghijklmnopqrstuvwxyz"


check_dict={}

for p in letters:
    check_dict[p]=0

for i in sentence:
    check_dict[i]=check_dict[i]+1

for x in check_dict:
    if check_dict[x] == 0:
        print(False)
        break
    else:
        print(True)
        break



