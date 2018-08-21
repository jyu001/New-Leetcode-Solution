'''
85. Maximal Rectangle
DescriptionHintsSubmissionsDiscussSolution
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

# refer to problem #84
#

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        lst = [-1]
        for j, h in enumerate(heights):
            while lst[-1]!=-1 and heights[lst[-1]]>h:
                res=max(res, heights[lst.pop(-1)] * (j-1-lst[-1]))
            lst.append(j)
        n = len(heights)
        while lst[-1] != -1:
            res = max(res, heights[lst.pop()] * (n-1-lst[-1]))
        return res
        
        
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0
        matrix.append(['0']* len(matrix[0]))
        for i in range(1,len(matrix)):
            j = len(matrix)-1-i
            for k in range(len(matrix[0])):
                if matrix[j][k]!='0': matrix[j][k] = int(matrix[j][k]) + int(matrix[j+1][k])
                else: matrix[j][k] = 0
        res = 0
        for i in range(len(matrix)-1):
            #print(matrix[i])
            res = max(res, self.largestRectangleArea(matrix[i]))
        return res