# Given a string, the task is to count all palindrome substring in a given string. Length of palindrome substring is greater than or equal to 2.

# Examples:

# Input : str = "abaab"
# Output: 3
# Explanation : 
# All palindrome substring are :
#  "aba" , "aa" , "baab" 

# Input : str = "abbaeae"
# Output: 4
# Explanation : 
# All palindrome substring are : 
# "bb" , "abba" ,"aea","eae"


x="abbaeae"
y=len(x)
store=[]
for i in range(y):
    for j in range(i+1,y+1):
        t=x[i:j]
        if t==t[::-1] and len(t)>=2:
            store.append(t)

print(len(store))
