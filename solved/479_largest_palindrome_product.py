'''
479. Largest Palindrome Product
DescriptionHintsSubmissionsDiscussSolution
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
'''

class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        if n == 2: return 987
        a = int('9'*(n-2))
        b = a
        for i in range(a):
            for j in range(i//2, -1, -1):
                m, l = a - j, a - (i-j)
                for (k1,k2) in [(9, 1), (1,9), (3, 3), (7, 7)]:
                    m1, n1 = 9*10**(n-1) + m*10 + k1, 9*10**(n-1) + l*10 + k2
                    #print(m1, n1)
                    res = m1*n1
                    x = str(res)
                    y = x[::-1]
                    if x==y: 
                        print(m1, n1)
                        return res%1337
                        