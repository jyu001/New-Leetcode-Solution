'''
260. Single Number III
DescriptionHintsSubmissionsDiscussSolution
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = sorted(nums)
        n = len(nums)
        i = n-1
        while i>=1:
            if nums[i] == nums[i-1]: 
                nums.pop(i)
                nums.pop(i-1)
                i-=2
            else: i-=1
        return nums