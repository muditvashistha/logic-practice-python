# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false


x=4
check=[]
num=str(x)

if x==1:
    print("It is a trivially Happy Number!") #edge case to check If 1 the number provided
else:
    while num not in check:
        check.append(num)
        sum=0
        for i in num:
            sum=sum+(int(i)**2)
        num=str(sum)
        if sum==1:
            print(True)
            break
    if num in check:
        print(False)



    
    
  







