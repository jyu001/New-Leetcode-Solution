'''
140. Word Break II
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''
#https://www.hrwhisper.me/leetcode-dynamic-programming/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ans = []
        if self.check(s, wordDict):
            self.dfs(0, len(s), '', s, ans, wordDict)
        return ans
 
    def check(self, s, wordDict):
        dp = [True] + [False] * len(s)
        n = len(s)
        for i in range(n):
            for j in range(i + 1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[n]
 
    def dfs(self, cur, n, path, s, ans, wordDict):
        if cur == n:
            ans.append(path)
            return
 
        for i in range(cur, n):
            if s[cur:i + 1] in wordDict and self.check(s[i + 1:n], wordDict):
                if path:
                    self.dfs(i + 1, n, path + ' ' + s[cur:i + 1], s, ans, wordDict)
                else:
                    self.dfs(i + 1, n, s[cur:i + 1], s, ans, wordDict)