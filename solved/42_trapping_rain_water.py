'''
42. Trapping Rain Water
DescriptionHintsSubmissionsDiscussSolution
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height) - 1
        while (r>l):
            prel, prer = height[l], height[r]
            if height[l] <= height[r]:
                l += 1
                while l<r and prel >= height[l]:
                    res += prel - height[l]
                    l += 1
                prel = height[l]
            else:
                r -= 1
                while l<r and prer >= height[r]:
                    res += prer - height[r]
                    r -= 1
                prer = height[r]
            print ( l, r, res)
        return res