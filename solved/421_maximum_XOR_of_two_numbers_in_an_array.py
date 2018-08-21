'''
421. Maximum XOR of Two Numbers in an Array
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start from highest bit: from 31 to 0
        # if highest bit has 1^0 = 1, keep 1; repeat to 2nd highest bit...
        #***** if max(a^b) = m, then m^a=b.
        mask = 0
        res = 0
        for bit in range(31,-1,-1):
            mask |= 1<<bit
            prefixSet = {num & mask for num in nums}
            guess = res | 1<<bit
            #print (prefixSet)
            for prefix in prefixSet:
                #print(prefix, guess, prefix^guess)
                if prefix ^ guess in prefixSet: #*****
                    res =guess
                    break        
        return res