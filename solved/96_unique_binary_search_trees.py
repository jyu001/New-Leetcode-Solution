'''
96. Unique Binary Search Trees
DescriptionHintsSubmissionsDiscussSolution
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dct = {}
        def check(n):
            if n==0: return 1
            if n==1: return 1
            if n==2: return 2
            res = 0
            for i in range(1,n+1):
                if i-1 not in dct: dct[i-1] = check(i-1)
                if n-i not in dct: dct[n-i] = check(n-i)
                res += dct[i-1] * dct[n-i]
            return res
        return check(n)