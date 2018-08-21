'''
115. Distinct Subsequences
DescriptionHintsSubmissionsDiscussSolution
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

'''


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dct = {}
        
        def check(s,t):
            m,n, res = len(s), len(t), 0
            if s==t or not t: return 1
            elif len(s)<len(t): return 0
            if (m,n) in dct: return dct[(m,n)]
            for i in range(len(s)-len(t)+1):
                if s[i]==t[0]: 
                    if (m-i-1, n-1) not in dct: dct[(m-i-1,n-1)] = check(s[i+1:], t[1:])
                    if (m-i-1, n) not in dct: dct[(m-i-1, n)] = check(s[i+1:], t)
                    res += dct[(m-i-1,n-1)] + dct[(m-i-1, n)]
                    break
            dct[(m,n)] = res
            return res
        return check(s,t)