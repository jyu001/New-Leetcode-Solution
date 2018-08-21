'''
46. Permutations
DescriptionHintsSubmissionsDiscussSolution
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []: return []
        if len(nums) == 1: return [nums]
        res = []
        for l in self.permute(nums[1:]):
            for i in range(len(nums)):
                a = l.copy()
                a.insert(i, nums[0])
                res.append(a)
        return res