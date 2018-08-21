'''
63. Unique Paths II
DescriptionHintsSubmissionsDiscussSolution
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == [[0]]: return 1
        dct = {(1,1):1}
        m, n = len(obstacleGrid[0]), len(obstacleGrid) # m: element count in a row, n: count in col
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1: dct[(m-j, n-i)]=0
        #print(dct)
        def check(m,n):
            if (m,n) in dct: return dct[(m,n)]
            if m>=1 and n>=1: 
                if (m-1, n) not in dct:
                    a = check(m-1, n)
                    dct[(m-1, n)] = a
                if (m, n-1) not in dct:
                    a = check(m, n-1)
                    dct[(m, n-1)] = a
                return dct[(m-1, n)] + dct[(m, n-1)]
            if m==0 or n==0:
                return 0
        
        
            
        return check(m, n)