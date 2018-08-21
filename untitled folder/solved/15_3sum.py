'''
15. 3Sum
DescriptionHintsSubmissionsDiscussSolution
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n<3: return []
        nums = sorted(nums)
        lstpop = []
        for i in range(n-2):
            if nums[i] == nums[i+1] and nums[i] == nums[i+2]: 
                lstpop.append(i)
                if nums[i] == 0 and [0,0,0] not in res : res.append([0,0,0])
        for i in lstpop[::-1]: 
            nums.pop(i)
            n-=1
        #print nums
        dct = {value:indx  for indx,value in enumerate(nums)}
        for i in range(n-2):
            for j in range(i+1,n):
                target = -nums[i]-nums[j]
                if target in dct and dct[target]>j:
                    res.append([nums[i],nums[j],target])
        check = set([])
        lstpop = []
        for i in range(len(res)):
            c = str(res[i][0]) + ' ' + str(res[i][1]) + ' ' + str(res[i][2])
            if c not in check:
                check.add(c)
            else: lstpop.append(i)
        for i in lstpop[::-1]: res.pop(i)
        return res