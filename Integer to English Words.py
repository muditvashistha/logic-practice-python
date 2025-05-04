# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

# Constraints:

# 0 <= num <= 231 - 1,     2147483647 = two billion one hundred forty-seven million four hundred eighty-three thousand six hundred forty-seven


num=1234567

if num==0:
    print("Zero")

below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

thousands = ["", "Thousand", "Million", "Billion"]

def iterate(n):
    if n==0:
        return ""
    if n<20:
        return below_20[n]+""
    elif n<100:
        return tens[n//10]+""+iterate(n%10)
    else:
        return below_20[n//100]+"Hundred"+iterate(n%100)
    
i=0
result=""
while num > 0:
    if num%1000 !=0:
        result=iterate(num%1000)+thousands[i]+""+result
        num=num//1000
        i=i+1

print(result)