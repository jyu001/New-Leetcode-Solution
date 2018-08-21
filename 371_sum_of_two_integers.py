'''
371. Sum of Two Integers
DescriptionHintsSubmissionsDiscussSolution
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.


'''

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b==0: 
            if a < 0x7FFFFFFF: return a
            else: return ~(a^0xFFFFFFFF)
        summ, carry = (a^b)&0xFFFFFFFF, ((a&b)<<1)&0xFFFFFFFF
        return self.getSum(summ, carry)