'''
45. Jump Game II
DescriptionHintsSubmissionsDiscussSolution
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3: return n-1
        if nums[0] >= n-1: return 1
        
        check = n - nums[0]
        for i in range(1, n):
            if n - i - nums[i] == check:
                nums[i] = 0
        
        lst = [n-1] * len(nums)
        for i in range(n-1):
            j = n-2-i
            
            if nums[j] == 0: continue
            
            if j == n-2: 
                lst[j] = 1
            elif nums[j] >= n-1-j: 
                lst[j] = 1
                continue
            else:
                curr = n-1-j
                for k in range(1, nums[j]+1):
                    check = nums[j]+1-k
                    if lst[j+check] == 1: 
                        curr = 2
                        break
                    curr = min(curr, 1+lst[j+check])
                lst[j] = curr
        return curr