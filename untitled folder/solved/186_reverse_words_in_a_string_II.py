'''
186. Reverse Words in a String II
DescriptionHintsSubmissionsDiscussSolution
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?


'''


class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        n = len(str)
        if n>2: 
            for i in range(n//2): str[i], str[n-1-i] = str[n-1-i], str[i]
            l = r = 0
            while r < n-1:
                if str[r+1] == ' ' or r==n-2:
                    if r==n-2: r=n-1
                    for i in range((r-l+1)//2): str[l+i], str[r-i] = str[r-i], str[l+i]
                    l, r = r + 2, r + 1
                r += 1