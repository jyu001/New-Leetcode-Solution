'''
189. Rotate Array
DescriptionHintsSubmissionsDiscussSolution
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)>=2:
            k = k%len(nums)
            l = [nums[j] for j in range(len(nums)-k, len(nums))]
            for i in range(len(nums)-1,-1,-1):
                if i<k: nums[i] = l[i]
                else: nums[i] = nums[i-k]
            
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n>=2:
            k = k%n
            a, b= n, k
            while b: a,b = b, a%b 
            p = a # greatest common factor，hcf
            
            for i in range(p):
                a, j = nums[i], i
                while j-i-k:
                    nums[j] = nums[j-k]
                    if j-k<0: j += n
                    j -= k
                nums[j] = a            



