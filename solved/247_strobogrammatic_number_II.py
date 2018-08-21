'''
247. Strobogrammatic Number II
DescriptionHintsSubmissionsDiscussSolution
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
'''

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = ['0','1','8','6','9']
        lno0 = ['1','8','6','9']
        l1 = ['0','1','8']
        dic = {'1':'1','6':'9','9':'6','8':'8', '0':'0'}
        res = []
        if n == 1: return l1
        for i in range(n//2):
            if i == n//2 - 1: l = lno0
            res = []
            if i == 0 and n%2 == 0: 
                for c in l:
                    res.append(c + dic[c])
            else:
                for c in l:
                    for c2 in l1:
                        res.append(c + c2 + dic[c])
            l1 = res
        return res