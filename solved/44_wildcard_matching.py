'''
44. Wildcard Matching
DescriptionHintsSubmissionsDiscussSolution
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''


'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """        
        lst = []
        indx, lens, cc, ques, star, count =0, 0, '', 0, 0, 0
        for i in range(len(p)):
            if p[i]=='*' or p[i]=='?': 
                if indx!=i: 
                    lst=[indx, lens, cc, ques, star]
                    #indx, lens, cc, ques, star = i+1, 0, '', 0, 0
                    break # only scan the first substring, not the whole string
                if p[i]=='*': star+=1
                else: 
                    ques, count = ques+1, count+1
                indx = i+1
            else: 
                lens, cc, count = lens+1, cc+p[i], count+1
            if i == len(p)-1: lst=[indx, lens, cc, ques, star]
        #print('lst:',lst)
        
        # first check
        if p == '': return False if s else True
        elif lst[1:4:2]==[0,0]: return True
        elif s == '': return False 
        elif count > len(s): return False
        
        # check the first substrings
        s = s[ques:]
        if s[:lens] == cc: return self.isMatch(s[lens:], p[indx + lens:])
        if star == 0: 
            if s[:lens]==cc: return self.isMatch(s[lens:], p[indx+lens:])
        else:
            n = s.find(cc)
            #print ('0', n, cc, s, p)
            while n>=0:
                #print ('1', n, s[n+lens:], p[indx+lens:])
                if self.isMatch(s[n+lens:], p[indx+lens:]): return True
                s = s[n+1:]
                n = s.find(cc)
                
        return False
        
import time
start = time.time()
s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

Solution().isMatch(s,p)
   
end = time.time()
print(int((end-start)*1000), 'ms')


'''


'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """   
        print(s,p)
        lst = p.split('*')
        for i in range(len(lst)): 
            if lst[len(lst)-1-i]== '': lst.pop(len(lst)-1-i)
        lenlst = [len(c) for c in lst]
        #print (lst, '\n', lenlst)
        
        if p[0]!="*":
            if lst[0]!= '?' and s[:lenlst[0]] != lst[0]: return False
            else: return self.isMatch(s[lenlst[0]:], '*'+'*'.join(lst[1:]))
        elif p[-1]!='*':
            if lst[-1]!= '?' and s[-lenlst[-1]:] != lst[-1]: return False
            else: return self.isMatch(s[:-lenlst[-1]], "*.join(lst[:-1])+'*'")
        else:
            
        
        
        
import time
start = time.time()
s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

Solution().isMatch(s,p)
   
end = time.time()
print(int((end-start)*1000), 'ms')



'''


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # remove common head and tail elements
        while p and s and p[0]==s[0]: p, s=p[1:], s[1:]
        while p and s and p[-1]==s[-1]: p, s=p[:-1], s[:-1]
        
        # deal with empty strings
        if s=='' and p=='': return True
        elif p=='': return False
        elif s=='':
            for c in p:
                if c!= '*': return False
            return True
        #check head and tail
        if p[0]!='*' and p[0]!='?' and p[0]!=s[0]: return False
        if p[-1]!='*' and p[-1]!='?' and p[-1]!=s[-1]: return False
        
        # in case there is only * and ? in p
        n, count = len(s), 0
        for c in p:
            if c!="*": count += 1
        if count > len(s): return False
        
        #print(s, p)
        
        # deal with the * and ? at the head, before any characters showing up
        i, star, question = 0, 0, 0
        while p[i]=='*' or p[i]=='?' :
            if p[i] == '?': question += 1
            if p[i] == '*': star += 1
            i += 1
            if i == len(p): 
                if star!=0 or i==n: return True
                else: return False
        
        c = p[i]
        #print('c:',c, 'p:',p, 'i',i)
        for j in range(question, n):
            if star==0 and s[j] != c: return False
            elif star==0 and s[j]==c: return self.isMatch(s[j+1:], p[i+1:])
            elif star>0:
                if s[j] != c: continue
                elif self.isMatch(s[j+1:], p[i+1:]): return True
        return False
        
        
        
        