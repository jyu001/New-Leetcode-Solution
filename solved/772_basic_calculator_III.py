'''
772. Basic Calculator III
DescriptionHintsSubmissionsDiscussSolution
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

Note: Do not use the eval built-in library function.

Your input
"13/(1--1)"
Your answer
Line 24: ZeroDivisionError: integer division or modulo by zero
Expected answer
6

'''

class Solution:
    def calculate_wn_parentheses(self, s):
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
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        lists = []
        count = 0
        #print(s)
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                count += 1
                if count == 1:
                    left = i
            if c == ")":
                count -= 1
                if count == 0:
                    right = i
                    lists.append([left, right])
        if lists == []: return self.calculate_wn_parentheses(s)
        for i in range(len(lists)):
            i = len(lists) - 1 - i
            left, right = lists[i][0], lists[i][1]
            s = s[:left] + str(self.calculate(s[left+1:right])) + s[right + 1:]
            #print (s)
        return self.calculate(s)
            