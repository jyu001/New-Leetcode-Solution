'''
347. Top K Frequent Elements
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(nums)):
            a = nums[i]
            if a not in dct: dct[a] = 0
            dct[a] += 1
        count = 0
        res = []
        for w in sorted(dct, key = dct.get, reverse = True):
            res.append(w)
            count += 1
            if count == k: return res