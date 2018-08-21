'''
303. Range Sum Query - Immutable
DescriptionHintsSubmissionsDiscussSolution
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
Seen this question in a real interview before?  

'''

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # save the sum of the first i elements into a list: self.sum, when calling sumRange, use self.sum to quickly get the res.
        
        lst = nums
        new = []
        for i in range(len(nums)):
            if not i: new.append(nums[0])
            else: new.append(new[i-1]+nums[i])
        self.sum = new

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not i: return self.sum[j]
        else: return self.sum[j]-self.sum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)