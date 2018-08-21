class Solution:

    def isValid(self, s, n):
        """
        :type s: str
        :rtype: bool
        """
        m = 0
        nleft = 0
        for i in range(len(s)):
            if s[i] == '(':
                m += 1
                nleft += 1
            else: 
                m -= 1
            if m <0: return False
        return m>= 0 and nleft <= n
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        res = ['(', ')']
        new = []
        for i in range(n * 2 - 1):
            for j in res:
                c = j + '('
                if self.isValid(c, n): new.append(c)
                c = j + ')'
                if self.isValid(c, n): new.append(c)
            res = new
            new = []
        return res
    