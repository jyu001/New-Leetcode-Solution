'''
163. Missing Ranges
DescriptionHintsSubmissionsDiscussSolution
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        l = r = 0
        if nums == []:
            l, r = lower, upper
            if l == r: res.append(str(l))
            else: res.append(str(l) + '->' + str(r))
            return res
        for i in nums:
            if i > lower:
                l = lower
                r = i - 1
                if l == r: res.append(str(l))
                else: res.append(str(l) + '->' + str(r))
                lower = i + 1
            elif i == lower:
                lower += 1
        if nums[-1] < upper:
            l = i + 1
            r = upper
            if l == r: res.append(str(l))
            else: res.append(str(l) + '->' + str(r))
        return res