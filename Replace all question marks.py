# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

# Example 1:

# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
# Example 2:

# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

class Solution(object):
    def modifyString(self, s):
        s=list(s)
        n=len(s)
        for i in range(n):
            if s[i]=="?":
                if i > 0 :
                    left=s[i-1]
                else:
                    left=''

                if i < n-1:
                    right=s[i+1]
                else:
                    right=''

                for ch in 'abc':
                    if ch != left and ch != right:
                        s[i]=ch
                        break
        return ("".join(s))
        