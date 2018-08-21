'''
246. Strobogrammatic Number
DescriptionHintsSubmissionsDiscussSolution
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        dic = {'1':'1','6':'9','9':'6','8':'8', '0':'0'}
        for i in range(0,(n+1)//2):
            if num[i] in dic and num[n-1-i] == dic[num[i]]:
                continue
            else:
                return False
        return True