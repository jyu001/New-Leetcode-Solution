'''
279. Perfect Squares
DescriptionHintsSubmissionsDiscussSolution
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

'''

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # any integer can be the sum of AT MOST 4 n(i)^2
        # if n%8 == 7: ans = 4
        # if n%4 == 0: ans = ans(n//4)
        
        while not n%4: n = n//4
        if n%8 == 7: return 4
        dct = {1:1, 2:2, 3:3, 4:1}
        a = int(math.sqrt(n))
        if a**2 == n: return 1
        for i in range(1, a+1):
            m = n - i*i
            b = int(math.sqrt(m))
            #print(m,n,b)
            if b**2 == m: return 2
        return 3
    