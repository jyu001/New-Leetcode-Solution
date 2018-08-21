'''
386. Lexicographical Numbers
DescriptionHintsSubmissionsDiscussSolution
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


'''

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        stack = [1]
        while stack:
            y = stack.pop()
            result.append(y)
            if y < n and y % 10 < 9:
                stack.append(y + 1)
            if y * 10 <= n: 
                stack.append(y * 10)
        return result
        
        
'''

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        stack = [1]
        while stack:
            y = stack.pop()
            result.append(y)
            if y < n and y % 10 < 9:
                stack.append(y + 1)
            if y * 10 <= n: 
                stack.append(y * 10)
        return result        
'''