'''
51. N-Queens
DescriptionHintsSubmissionsDiscussSolution
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # row 1: n options
        # row 2: n-3 options or n-2 options if on corner
        # row 3-n: only 1 option: follow the patter of 1 and 2
        if n==1: return [['Q']]
        elif n<4: return []
        nums = [[i] for i in range(n)]         
        ans = []
        for row in range(1,n):
            new = []
            for pre in nums:
                for check in range(n):
                    judge = True
                    for i in range(row):
                        if (check - pre[i]) in [0, row-i, i-row]: 
                            judge = False
                            break
                    if judge: new.append(pre+[check])
            nums = new
            #print('added row:', row, nums)
        
        for l in nums:
            new = []
            for i in l:
                res = "."*(n-1)
                res = res[:i] + 'Q' + res[i:]
                new.append(res)
            ans.append(new)
            
        return ans