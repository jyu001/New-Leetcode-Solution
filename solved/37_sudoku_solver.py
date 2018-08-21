'''
37. Sudoku Solver
DescriptionHintsSubmissionsDiscussSolution
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

'''

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        lst = []
        res = [[([1,2,3,4,5,6,7,8,9])]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': 
                    res[i][j] = ([int(board[i][j])])
                    lst.append([i,j,int(board[i][j])])
        print(res)
        while lst != []:
            #print(lst[0])
            [x,y,v] = lst[0]
            block = x//3*3 + y//3
            for i in range(81):
                m, n = i//9, i%9
                b = m//3*3 + n//3
                if m==x and n==y: continue
                if board[m][n] != '.': continue
                elif m==x or n==y or b==block: 
                    print('before',m,n,res[m][n])
                    if (v in res[m][n]): 
                        res[m][n].remove(v)
                        print('after', m, n, res[m][n])
                if len(res[m][n]) == 1: 
                    nv = res[m][n][0]
                    lst.append([m,n,nv])
                    board[m][n] = str(nv)
                    #print('Addnew',m, n, board[m][n])
            lst = lst[1:]
        print(board)



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print ()