'''
233. Number of Digit One
DescriptionHintsSubmissionsDiscussSolution
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution:
    def times10(self, n):
        if n == 0: return 0
        if n == 1: return 1
        return 10*self.times10(n-1) + 10**(n-1)
    
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        res = 0
        l = len(str(n))-1
        if l == 0: return 1
        m = n//(10**l)
        n = n%(10**l)
        if m == 1: res += n+1
        elif m > 1: res += 10**l  # ***** important *****
        #print (res, n)
        res += self.times10(l) * m + self.countDigitOne(n)
        return res