'''
64. Minimum Path Sum
DescriptionHintsSubmissionsDiscussSolution
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, l = len(grid), len(grid[0])
        dct = {(1,1):grid[r-1][l-1]}
        def check(m, n):
            if (m,n) in dct: return dct[(m,n)]
            if m>0 and n>0:
                if (m-1, n) not in dct: dct[(m-1,n)]=check(m-1,n)
                if (m, n-1) not in dct: dct[(m,n-1)]=check(m,n-1)
                return grid[r-m][l-n] + min(dct[(m-1, n)], dct[(m, n-1)])
            elif m==0 or n==0: return 2147483648
        return check(r,l)