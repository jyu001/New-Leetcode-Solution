'''
483. Smallest Good Base
DescriptionHintsSubmissionsDiscussSolution
For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format. 

Example 1:
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
Note:
The range of n is [3, 10^18].
The string representing n is always valid and will not have leading zeros.
'''

# 2^60 = 483. Smallest Good Base1.1529215e+18
# k^i < m < (k+1)^i
# 

class Solution:
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        import math
        m = int(n)
        maxm = math.floor(math.log(m, 2))
        for i in range(maxm):
            ii = maxm - i
            if ii>1: base = math.floor(math.pow(m, 1/ii))
            else: return str(int(m - 1))
            print(ii, base)
            if base==1: continue
            check = m
            for k in range(1,ii+1):
                if check%base != 1: break
                check = check//base
                if k == ii: return str(int(base))
                
                