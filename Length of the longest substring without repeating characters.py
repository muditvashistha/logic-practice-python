# Given a string str, find the length of the longest substring without repeating characters. 

# Example 1:
# Input: “ABCDEFGABEF”
# Output: 7
# Explanation: The longest substring without repeating characters are “ABCDEFG”, “BCDEFGA”, and “CDEFGAB” with lengths of 7

# Example 2:
# Input: “GEEKSFORGEEKS”
# Output: 7
# Explanation: The longest substrings without repeating characters are “EKSFORG” and “KSFORGE”, with lengths of 7



str="GEEKSFORGEEKS"

# y=len(str)
# empty=[]
# for i in range(y):
#     for j in range(i+1,y+1):
#         t=(str[i:j])
#         if len(t)==len(set(t)):
#             empty.append(t)




# temp=""
# for i in empty:
#     if len(i)>len(temp):
#         temp=i

# print(len(temp))


# for i in empty:
#     if len(i)==len(temp):
#         print(i)

temp=""
y=len(str)
empty=[]
for i in range(y):
    for j in range(i+1,y+1):
        t=(str[i:j])
        if len(t)==len(set(t)) and len(t)>len(temp):
            temp=t

print(len(temp))



       

        





