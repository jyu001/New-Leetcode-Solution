'''
227. Basic Calculator II
DescriptionHintsSubmissionsDiscussSolution
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        front = 0
        simbol = 1 # + 1, - 2, * 3, / 4
        checknum = False
        currnum = 0
        s = s + '+0'
        for c in s:
            if ord(c) > 47 and ord(c) < 58: 
                currnum = currnum * 10 + int(c)
                checknum = True
                #print('1...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
            else: 
                if checknum: 
                    #print('2...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
                    if simbol == 1: front += currnum
                    elif simbol == 2: front -= currnum
                    elif simbol == 3: front *= currnum
                    elif front >= 0: front = front//currnum
                    else: front = - (-front //currnum)
                    #print('2.5...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
                
                if c == '+':
                    simbol = 1
                elif c == '-':
                    simbol = 2
                elif c == '*':
                    simbol = 3
                elif c == '/':
                    simbol = 4
                if c == '+' or c == '-':
                    res = res + front
                    front = 0
                
                currnum = 0
                checknum = False
            
            #print('4...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
        return res