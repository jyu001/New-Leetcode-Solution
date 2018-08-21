'''
179. Largest Number
DescriptionHintsSubmissionsDiscussSolution
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.


'''

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums==[]: return ''
        lst = sorted([str(i) for i in nums])[::-1]
        print(lst)
        
        j = 1
        while j < len(lst):
            i = j
            while i>0:
                if int(lst[i-1]+lst[i]) < int(lst[i]+lst[i-1]): lst[i-1], lst[i] = lst[i], lst[i-1]
                i -= 1
            j+=1
        #print(lst)
        
        res = ''.join(lst)
        if not int(res): return '0'
        return res
    
