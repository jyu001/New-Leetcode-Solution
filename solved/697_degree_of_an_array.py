'''
697. Degree of an Array
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for n in range(len(nums)):
            if nums[n] not in dct: dct[nums[n]]=[0,n,-1]
            else: dct[nums[n]][2] = n
            dct[nums[n]][0] += 1
        #print(dct)
        maxm, res = 1, 1
        for k,v in dct.items():
            count = v[2]-v[1]+1
            if v[2]==-1: count = 1
            if v[0] > maxm: 
                maxm = v[0]
                res = count
            elif v[0]==maxm:
                res = min(res, count)
        return res