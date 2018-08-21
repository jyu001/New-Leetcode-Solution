'''
125. Valid Palindrome
DescriptionHintsSubmissionsDiscussSolution
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(s.split(' '))
        new = []
        for c in s:
            n = ord(c)
            if n<48 or 57<n<65 or 90<n<97 or n>122: continue
            if n>96: n-=32
            new.append(n)
        return new == new[::-1]