# Given a string str of length N, consisting of ‘(‘ and ‘)‘ only, the task is to check whether it is balanced or not.

#Examples:

# Input: str = “((()))()()” 
# Output: Balanced
# Input: str = “( ) ) ( ( ( ) )” 
# Output: Not Balanced 


def check_para(str1):
    count=0
    for i in range(0,len(str1)):
        if str1[i]=="(":
            count+=1
        else:
            count-=1
        if (count<0):
            print("not balanced")
            break
    if (count==0):
        print("balanced")
        
check="((()))()()"

check_para(check)

