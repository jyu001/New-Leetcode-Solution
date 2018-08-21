'''
119. Pascal's Triangle II
DescriptionHintsSubmissionsDiscussSolution
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?


'''

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst = [i for i in range(rowIndex, 0, -1)]
        res = [1]
        for i in range(rowIndex):
            a = res[i] * lst[i] // lst[rowIndex-1-i]
            res.append(a)
        return res