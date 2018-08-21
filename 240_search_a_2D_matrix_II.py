'''
240. Search a 2D Matrix II
DescriptionHintsSubmissionsDiscussSolution
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # first in row 0: go from left to right, untile matrix[0][j] > target, if not found, go to matrix[1][j]
        # go to matrix[1][j-1] and compare with target, if >: go to 2,j-2, elif <: go to 2, j-1
        # repeat until index goes beyond limits
        if not matrix or not matrix[0]: return False
        i = j = 0
        while j<len(matrix[0]): 
            if matrix[0][j] == target: return True
            elif matrix[0][j] < target and j<len(matrix[0])-1: j+=1
            else: break
        while i<len(matrix) and 0<=j: 
            if matrix[i][j] == target: return True
            elif matrix[i][j] < target: i+=1
            else: 
                if j==0: return False
                elif i==len(matrix)-1: j-=1
                elif matrix[i][j-1]>=target: j-=1
                else: i,j = i+1, j-1
        return False