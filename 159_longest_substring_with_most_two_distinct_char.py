"""
159. Longest Substring with At Most Two Distinct Characters
DescriptionHintsSubmissionsDiscussSolution
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3: return len(s)
        char1 = s[0]
        char2 = ''
        n1 = 0
        prechar, prenum = char1, 0
        maxm = 1
        for i in range(1,len(s)):
            if s[i] == char1 or s[i] == char2:
                maxm = max(maxm, i - n1 + 1)
                if s[i] != prechar:
                    prechar, prenum = s[i], i
            elif char2 == "":
                char2 = s[i]
                maxm = max(maxm, i - n1 + 1)
                prechar, prenum = s[i], i
            else:
                char2 = s[i]
                char1 = prechar
                n1 = prenum
                prechar, prenum = s[i], i
                maxm = max(maxm, i - n1 + 1)
            #print (i, maxm, n1, prechar, prenum)
        return maxm