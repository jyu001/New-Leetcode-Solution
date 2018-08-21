'''
79. Word Search
DescriptionHintsSubmissionsDiscussSolution
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dct = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c not in dct: dct[c] = []
                dct[c].append((i,j))
        print(dct.keys())
        for c in word: 
            if c not in dct: return False
        lst = []
        def check(i, lst):
            #print('i', i, lst)
            if i == len(word): return True
            lst = lst[:i]
            for (k,j) in dct[word[i]]:
                if (k,j) in lst: continue
                if lst:
                    m,n = lst[-1]
                    if (m-k)**2 + (n-j)**2 != 1: continue
                if check(i+1, lst+[(k,j)]): return True
            return False
        return check(0,lst)