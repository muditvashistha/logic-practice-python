# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.


# n = 8
# remaining = n

# for i in range(1,n+1):
#     if remaining < i:
#         print(i-1)
#         break
#     else:
#         remaining = remaining - i


class Solution(object):
    def arrangeCoins(self, n):
        comp = 0
        i = 1
        while n >=0:
            n = n - i

            if n>=0:
                comp = comp + 1
            i = i + 1
        return comp


