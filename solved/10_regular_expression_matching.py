class Solution:

    wild = False
    repeat = ""
    repeattime = 0
    last = ""
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "" and s == "": return True
        elif p == "" and s[0] == last: s = s[1:]
        elif s == "":
            if len(p) >= 2 and p[1] == "*": p = p[2:]
            if p[0] == "*": 
                repeat = last
                p = p[1:]
            else: return False
            
        if p[0] == ".": 
            wild = True
            last = "wild"
            s, p = s[1:], p[1:]
            
        if p[0] == "*":
            repeat = last
            if last == "wild": return True
            if s[0] != last: return False
            s, p = s[1:], p[1:]
            repeattime += 1
            
        if p[0] == s[0]: 
            last = p[0]
            wild = False
            return self.isMatch(s[1:], p[1:])
            
        if p[0] != s[0]:
            if last == "wild":
                p = p[1:]
                last = p[0]
                wild = 
            if len(p) >= 2 and p[1] == "*": 
                p = p[2:]
            if s[0] == last:
                repeattime += 1
            if p[0] == last:
                repeattime -= 1
                if repeattime < 0: return False
        
        elif repeat != s[0] and repeat != "wild":
            return False

        return self.isMatch(s, p)
        
print ("true", Solution().isMatch("aaa", "ab*a*c*a"))
print ("false", Solution().isMatch("aa", "a"))
print ("true", Solution().isMatch("aa", "a*"))
print ("true", Solution().isMatch("ab", ".*"))
print ("true", Solution().isMatch("aab", "c*a*b"))
print ("false", Solution().isMatch("mississippi", "mis*is*p*"))