'''
139. Word Break
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ns = len(s)
        for c in wordDict:
            if c == s: return True
            n = len(c)
            if n > ns: continue
            if c == s[:n]:
                m = n
                while len(s[m:])>n and c == s[m:][:n]:
                    m += n
                if self.wordBreak(s[m:], wordDict): return True
        return False
            
            
'''
Custom Testcase( Contribute  )

"aaaaaaaaab"
["a","aaaaaab"]
Run Code Status: Finished
×
Run Code Result:
Your input
"aaaaaaaaab"
["a","aaaaaab"]
Your answer
false
Expected answer
true
'''