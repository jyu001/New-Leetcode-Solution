'''
219. Contains Duplicate II
DescriptionHintsSubmissionsDiscussSolution
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k== 0: return False
        if k >= len(nums)-1: return not len(nums)==len(list(set(nums)))
        lst = nums[:k]
        l = set(lst)
        if len(l) < k: return True
        for i in range(k,len(nums)):
            if nums[i] in l: return True
            else: 
                #print(k, l)
                l.remove(nums[i-k])
                l.add(nums[i])
        return False