# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

def reverseOnlyLetters(s):
    temp=list(s)
    start=0
    end=len(temp)-1

    while start < end:
        if temp[start].isalpha() == False:
            start =  start + 1
            continue
        if temp[end].isalpha() == False:
            end = end - 1
            continue
            
        temp[start] , temp[end] = temp[end] , temp[start]

        start = start + 1
        end = end - 1
        
    return ("".join(temp))