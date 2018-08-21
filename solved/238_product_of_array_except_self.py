'''
238. Product of Array Except Self
DescriptionHintsSubmissionsDiscussSolution
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if i==0: res.append(1)
            else: res.append(res[i-1]*nums[i-1])
        new = 1
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1: continue
            new *= nums[i+1]
            res[i] *= new
        return res