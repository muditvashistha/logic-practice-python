# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# [1,3,1
#  1,5,1
#  4,2,1]

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        

        for i in range(m):
            for j in range(n):
                if i==j==0:
                    continue
        
                top = left = float('inf')
                if i!=0:
                    top = grid[i][j] + grid[i-1][j]
                if j!=0:
                    left = grid[i][j] + grid[i][j-1]
                grid[i][j] = min(top,left)
        return grid[m-1][n-1]
                

        