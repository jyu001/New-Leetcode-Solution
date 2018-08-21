'''
87. Scramble String
DescriptionHintsSubmissionsDiscussSolution
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
'''

# note: find a seperator, so the left part (length l1) and right part(l2) are scrambled strings 
# of the original string's substring with length l1 and l2
# note that could be like this: s1: l1+l2, s2: l2+l1

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = list(s1)
        l2 = list(s2)
        def check(l1,l2):
            #print(l1,l2)
            if sorted(l1) != sorted(l2): return False
            n = len(l1)
            if n<=3: return True
            for i in range(1,n):
                #print('check i', i)
                if sorted(l2[:i]) == sorted(l1[:i]) and check(l1[:i], l2[:i]) and check(l1[i:], l2[i:]):
                    return True
                elif sorted(l2[:i]) == sorted(l1[-i:]) and check(l1[-i:], l2[:i]) and check(l1[:-i], l2[i:]):
                    return True
            return False
        return check(l1,l2)