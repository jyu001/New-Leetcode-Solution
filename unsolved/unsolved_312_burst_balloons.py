'''
312. Burst Balloons
DescriptionHintsSubmissionsDiscussSolution
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''
class Solution:

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #from https://www.hrwhisper.me/leetcode-burst-balloons/
        c = [1] + [i for i in nums if i > 0] + [1]
        n = len(c)
        dp = [[0] * n for _ in range(n)]
        
        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                dp[left][right] = max(dp[left][i] + c[left] * c[i] * c[right] + dp[i][right] for i in range(left + 1, right))
        return dp[0][n - 1]


'''
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        elif n == 2: 
            if nums[0]>=nums[1]: return nums[0]*(nums[1] + 1)
            else: return nums[1]*(nums[0] + 1)
        for i in range(len(nums)): # remove '0's
            if nums[i] == 0: nums.pop(i)
        for i in range(1,len(nums)-1): # remove minimum values
            a, b, c = nums[i-1],nums[i],nums[i+1]
            if a>=b and b<=c : 
                nums.pop(i)
                print('0',a*b*c,nums)
                return a*b*c + self.maxCoins(nums)
        # now there is no minimum value
        # find the maxm value, and there should be no more than one maxm
        nmax = 0
        start = nums[0]
        for i in range(len(nums)):
            if nums[i]>=start:
                nmax, start = i, nums[i]
        res = 0
        if nmax == 0: # no maximum, decreasing
            for i in range(len(nums)-2):
                res += nums[1]*nums[0]*nums[2] 
                nums.pop(1)
            
            print('1', res, nums)
            return res + nums[0]*(nums[1] + 1)
        else:       # one maximum
            if nmax > 1:
                for i in range(nmax-1):
                    res += nums[nmax-i]*nums[nmax-i-1]*nums[nmax-i-2]
                    nums.pop(nmax-1-i)
                    n -= 1
            if nmax < n-2:
                for i in range(n-2-nmax):
                    res += nums[nmax]*nums[nmax+1]*nums[nmax+2]
                    nums.pop(nmax+1)
                    n -= 1
            # now there should be exactly 3 numbers left
            
            print('2', res, nums)
            return res + nums[0]*nums[1]*nums[2] + self.maxCoins([nums[0]] + [nums[2]])
            
        # in case 5, 1, 3, 8, 4, 2, 1, => 5, 8, 4, 2, 1 => 5, 8, 4, 2, 1 => 5, 4, 2, 1
'''