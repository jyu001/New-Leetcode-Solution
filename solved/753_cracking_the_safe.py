'''
753. Cracking the Safe
DescriptionHintsSubmissionsDiscussSolution
There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
Note:
n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.
'''

class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = '0'*n
        dct=set([res])
        if k == 1: return res
        if n == 1: 
            for i in range(1,k): 
                res += str(i)
            return res
        lst = [k-1-i for i in range(k)]
        
        check = True
        while check:
            for i in range(k):
                new = res[-n+1:] + str(lst[i])
                #print ('res:', res, 'new:', new, 'dct:', dct)
                if new not in dct:
                    dct.add(new)
                    res += str(lst[i])
                    break
                if i == k-1: 
                    check = False
        return res
        
        
        '''
        # deep first search tree *****
        lst = []
        for i in range(k):
            lst.append(i)
        #print (lst)
        for i in range(1,n):
            l = []
            for j in range(k):
                #res2 = str(j)
                res2 = str(j)
                for x in range(k):
                    res2 += str(lst[(j+i+x)%k])
                    if j ==2: print('j:', j, res2)
                l.append(res2)
                print ('l', l)
            lst = l
        for i in range(k):
            res += lst[i]
        
        dup = []
        for i in range(len(res)+1-n):
            s=res[i:i+n]
            if s not in dct: dct.add(s)
            else: dup += [i, s]
        print(dup)
        return res
        '''