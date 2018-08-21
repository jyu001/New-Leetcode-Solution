'''
224. Basic Calculator
DescriptionHintsSubmissionsDiscussSolution
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
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
        brck = 0
        brclist = [0]
        addminus = 1
        addlist = [1]
        checknum = False
        currnum = 0
        s = s + ' '
        for c in s:
            if ord(c) > 47 and ord(c) < 58: 
                currnum = currnum * 10 + int(c)
                checknum = True
                #print('1...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
            else: 
                if checknum: 
                    #print('2...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
                    brclist[brck] += currnum * addminus
                    #print('2.5...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
                if c == '(':
                    brclist.append(0)
                    brck += 1
                    addlist.append(addminus)
                    addminus = 1
                elif c == ')':
                    a = brclist.pop(brck)
                    b = addlist.pop(brck)
                    brck -= 1
                    brclist[brck] += a * b
                    #print('3...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
                elif c == '+':
                    addminus = 1
                elif c == '-':
                    addminus = -1
                    
                currnum = 0
                checknum = False
            
            #print('4...','brck:', brck, 'c:',c, 'currnum:', currnum, 'addlist:',addlist, 'brclist[]:',brclist)
        return brclist[0]