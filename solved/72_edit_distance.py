'''
72. Edit Distance
DescriptionHintsSubmissionsDiscussSolution
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dct = {}
        def check(i,j):
            if (i,j) in dct: return dct[(i,j)]
            w1, w2 = word1[i:], word2[j:]
            
            if w1=='' or w2=='': 
                dct[(i,j)] = max(len(w1), len(w2))
                return dct[(i,j)]
            if w1[0]==w2[0]:
                if (i+1, j+1) not in dct: dct[(i+1,j+1)] = check(i+1,j+1)
                return dct[(i+1, j+1)]
            #n = w2.find(w1[0])
            #if n == -1: 
            if (i, j+1) not in dct: dct[(i,j+1)]=check(i, j+1)
            if (i+1, j) not in dct: dct[(i+1,j)]=check(i+1, j)
            if (i+1,j+1) not in dct: dct[(i+1, j+1)]=check(i+1,j+1)
            
            dct[(i,j)] = min(dct[(i,j+1)],dct[(i+1,j)],dct[(i+1, j+1)]) + 1
            #else: return min(self.minDistance)
            #print(i, j, w1, w2, dct[(i,j)])
            return dct[(i,j)]
        return check(0,0)