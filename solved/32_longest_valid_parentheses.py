'''
32. Longest Valid Parentheses
DescriptionHintsSubmissionsDiscussSolution
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m, n, count, curr = len(s), len(s), 0, 0
        if n < 2: return 0
        lst = range(n)
        
        left = 0
        while curr < n:
            if s[curr] == '(': 
                left += 1
                curr += 1
            elif left > 0: 
                left -= 1
                s = s[:curr] + s[curr+1:]
                lst = lst[:curr] + lst[curr+1:]
                n -= 2
                curr -= 1
            else: curr += 1
                
        if lst == []: return m
        lst = [-1] + lst + [m]
        print (lst)
        for i in range(len(lst)-1):
            count = max(count, lst[i+1]-lst[i]-1)
        return count
                
                
            