'''
152. Maximum Product Subarray
DescriptionHintsSubmissionsDiscussSolution
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        i, n = 0, len(nums)
        res = nums[0]
        while i<n:
            if nums[i]==0: 
                res = max(0, res, self.maxProduct(nums[:i]))
                if i == n-1: return res
                nums = nums[i+1:]
                i, n = -1, len(nums)
            i += 1
        
        # now, there is no 0 in the lst
        n = len(nums)
        lst = [] # list the negative nums index
        for j in range(n):
            if nums[j] < 0: lst.append(j)
        #print(nums, lst)
        if len(lst)%2:
            a = self.maxProduct(nums[:lst[0]]) if nums[0]>0 else nums[0]
            b = self.maxProduct(nums[lst[-1]+1:]) if nums[-1]>0 else nums[-1]
            c = max (  self.maxProduct(nums[:lst[-1]]), self.maxProduct(nums[lst[0]+1:])  ) if lst[-1]-lst[0] else nums[0]
            return max(res, a, b, c)
        else:
            curr = 1
            for j in range(n): curr *= nums[j]
            return max(res, curr)