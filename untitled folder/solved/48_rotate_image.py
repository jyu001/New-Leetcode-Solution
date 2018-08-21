'''
48. Rotate Image
DescriptionHintsSubmissionsDiscussSolution
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # (i, j) => (n-1-j, i)
        n = len(matrix)
        (x, y) = (n//2,n//2+1) if n%2 else (n//2,n//2)
        for i in range(x):
            for j in range(y):
                i1, j1 = n-1-j, i
                i2, j2 = n-1-j1, i1
                i3, j3 = n-1-j2, i2
                matrix[i][j], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3] = matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i][j]