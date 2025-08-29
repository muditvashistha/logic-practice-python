# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

vowels={"a","e","i","o","u","A","E","I","O","U"}
x="IceCreAm"

temp=(list(x))
start=0
end=len(temp)-1

while start < end:
    if temp[start] in vowels and temp[end] in vowels:   
        temp[start] , temp[end] = temp[end] , temp[start]
        start = start+1
        end=end-1

    if temp[start] not in vowels:
        start = start + 1

    if temp[end] not in vowels:
        end = end - 1

    
print("".join(temp))
