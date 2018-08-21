'''
204. Count Primes
DescriptionHintsSubmissionsDiscussSolution
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return 0
        res = [0,0]+[1]*(n-2)
        for i in range(n):
            if not res[i]: continue
            else:
                for j in range(i**2,n,i): res[j]=0
        return sum(res)