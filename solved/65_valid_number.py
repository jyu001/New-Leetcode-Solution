'''
65. Valid Number
DescriptionHintsSubmissionsDiscussSolution
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.


'''


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == ' ': return False
        while s[0] == ' ': s=s[1:]
        while s[-1] == ' ': s=s[:-1]
        if s[0] == '-' or s[0] == '+': s=s[1:]
        if s == '.' or s[:2] == '.e' or s[0] == 'e' or s[-1] == 'e' or s[-1] == '-' or s[-1] == '+' : return False
        lst = set(['0','1','2','3','4','5','6','7','8','9','e','.'])
        show_e, show_point = 0, 0
        pre = ''
        for c in s:
            if pre == 'e':
                if c == '+' or c == '-': continue
                else: pre = ''
            if c not in lst: return False
            if c <= '9' and c >= '0':continue
            if show_e == 0 and c == 'e': 
                show_e = 1
                pre = 'e'
                continue
            if show_e == 0 and show_point == 0 and c == '.': 
                show_point = 1
                continue
            if show_e == 1 and c == 'e' or c == '.': return False
            if show_point == 1 and c == '.': return False
        return True
        

'''
Input:
"e"
Output:
true
Expected:
false
        
Input:
"."
Output:
true
Expected:
false
        
Input:
".e1"
Output:
true
Expected:
false   
        
Input:
" 005047e+6"
Output:
false
Expected:
true   
        
Input:
"4e+"
Output:
true
Expected:
false    
        
Input:
"2e+60++604"
Output:
true
Expected:
false 
        
        
        
'''