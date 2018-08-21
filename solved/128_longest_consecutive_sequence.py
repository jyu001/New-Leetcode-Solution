'''
128. Longest Consecutive Sequence
DescriptionHintsSubmissionsDiscussSolution
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        check = {}
        maxm = 0
        for n in nums:
            if n in check: continue
            l, r = n, n
            if n-1 in check:
                l = check[n-1][0]
                check[n-1][1] = n
                while l != check[l][0]:
                    l = check[l][0]
                    check[l][1] = n
            if n+1 in check:
                r = check[n+1][1]
                check[n+1][0] = n
                while r != check[r][1]:
                    r = check[r][1]
                    check[r][0] = n
            #print(n, nums, l, r)
            maxm = max(maxm, r-l+1)
            check[n] = [l,r]
        
        return maxm
            