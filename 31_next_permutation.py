'''
31. Next Permutation
DescriptionHintsSubmissionsDiscussSolution
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mark = n-1
        if n==2: 
            nums[1],nums[0] = nums[0], nums[1]
        elif n>=3:
            for i in range(n-1):
                a,b = nums[n-1-i], nums[n-2-i]
                if a<=b: mark = n-2-i
                else: break
            if mark == 0: 
                for i in range(n//2): nums[i],nums[n-1-i] = nums[n-1-i], nums[i]
            else:
                nnums = nums[mark:][::-1]
                for j in range(mark,n): nums[j] = nnums[j-mark]
                for j in range(mark,n):
                    if nums[j]>nums[mark-1]:
                        nums[j], nums[mark-1] = nums[mark-1], nums[j]
                        break
                    
                