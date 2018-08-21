'''
153. Find Minimum in Rotated Sorted Array
DescriptionHintsSubmissionsDiscussSolution
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, m, r = 0, (n-1)//2, n-1
        while r-l > 1:
            if nums[m] > nums[r]:
                l, m, r = m, (m+r)//2, r
            else:
                l, m, r = l, (l+m)//2, m
        return min(nums[l:r+1])