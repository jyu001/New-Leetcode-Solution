'''
420. Strong Password Checker
DescriptionHintsSubmissionsDiscussSolution
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.


'''

class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 6
        res, n, pre = 0, len(s), ''
        lst = []
        typelst = [0,0,0]
        
        for c in s:
            if c == pre: lst[-1] += 1
            else: 
                lst.append(1)
                pre = c
                if ord(c) in range(48,58): typelst[0] = 1
                elif ord(c) in range(65,91): typelst[1] = 1
                elif ord(c) in range(97,123): typelst[2] = 1
        dup, addtype, insert, delete = 0, 3-sum(typelst), 6-n, n-20
        
        threetime = 0 # number of i%3==0 in lst, for these i, delete one repeat can reduce length and dup at the same time
        for i in lst:
            if i>=3: 
                dup += i//3
                if i%3==0: threetime += 1
        # first consider when n<=6 and 6<n<=20:
        if insert>=0: return max(insert, addtype)
        elif delete<=0: return max(dup, addtype)
        # below are the cases when n > 20; need to consider duplicate, addtype too.
        return max(dup,addtype) + delete -min(delete, threetime)
        
        
        
# input: "aaaaaabbbbbbccccccddddddeeeeee"
# output: 15
# expected: 14