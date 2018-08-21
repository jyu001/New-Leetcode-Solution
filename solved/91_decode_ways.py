'''
91. Decode Ways
DescriptionHintsSubmissionsDiscussSolution
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

# seperate the string into substrings: by deciding whether 'ij' can be decoded into ij together
# if ij can only be decoded into i + j, then seperate them
# special cases: 00, 30, 40... return 0
# special cases: 10, 20: need to avoid counting the '1' and '2' into previous substrings

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #print(s)
        if s == '': return 0
        elif s[0] == '0': return 0
        n = len(s)
        if n==1: return 1
        curr = 1
        lst = []
        for i in range(len(s)-1):
            n = int(s[i:i+2])
            if (n>10 and n<20) or (n>20 and n<27):
                if i<len(s)-2 and s[i+1:i+3] in ['10','20']: continue
                curr += 1
            elif n%10==0 and n not in [10,20]: return 0
            else: 
                lst.append(curr)
                curr = 1
        lst.append(curr)
                
        #print(lst)
                
        dct = {1:1, 2:2}
        res = 1
        for i in lst:
            if i not in dct:
                for j in range(3,i+1):
                    dct[j] = dct[j-1] + dct[j-2]
            res *= dct[i]
        return res
            