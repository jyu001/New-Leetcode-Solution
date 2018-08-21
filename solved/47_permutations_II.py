'''
47. Permutations II
DescriptionHintsSubmissionsDiscussSolution
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []: return []
        if len(nums) == 1: return [nums]
        res = []
        for l in self.permuteUnique(nums[1:]):
            pre = nums[0]-1
            for i in range(len(nums)):
                if nums[0] == pre: continue
                elif i == len(nums)-1: pre = nums[0]-1
                else: pre = l[i]
                a = l.copy()
                a.insert(i, nums[0])
                res.append(a)
        return res