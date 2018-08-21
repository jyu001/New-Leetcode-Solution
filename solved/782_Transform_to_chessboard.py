'''
782. Transform to Chessboard
DescriptionHintsSubmissionsDiscussSolution
An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

Examples:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.
Note:

board will have the same number of rows and columns, a number in the range [2, 30].
board[i][j] will be only 0s or 1s.
'''

class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # check 1: the number of '1' in each row/column is n/2 or n/2+1 (if n%2=1)
        # check 2: only two types of rows and two types of columns
        # if n%2 = 0: board[0][0] can be either 0 or 1; 
        # if n%2 = 1: board[0][0] can only be the majority element in the rows/ columns
        n = len(board)
        row, col = [], []
        for i in range(n):
            a = board[i]
            if a not in row: row.append(a)
        for j in range(n):
            b = []
            for i in range(n):
                b.append(board[i][j])
            if b not in col: col.append(b)
        #print ('row:', row, '\n', 'col:', col)
        
        # first check 
        if len(row)!=2 or len(col)!=2: return -1
        
        # only need to check one row/ column
        # countrow, countcol: times needed to move rows, cols
        r, c, countrow, countcol = row[0], col[0], 0, 0
        for i in range(n):
            if row[0][i] ^ row[1][i] and col[0][i] ^ col[1][i]: 
                countrow += r[i]
                countcol += c[i]
            else: return -1
        if countrow > (n+1)//2 or countcol > (n+1)//2: return -1
        
        countrow, countcol = 0, 0
        for i in range(n):
            countrow += (i%2)^(c[0]^board[i][0])
            countcol += (i%2)^(r[i]^r[0]) 
            #print('i', i, 'countrow', countrow, 'i%2', i%2, 'c[0]', c[0], 'board[i][0]', board[i][0], 'countcol', countcol, 'r[i]', r[i])
            
        if countrow%2: countrow = n - countrow
        if countcol%2: countcol = n - countcol
        
        if n%2==0: countrow, countcol = min(countrow, n-countrow) , min(countcol, n-countcol)
        
        countrow, countcol = countrow//2 , countcol//2
        move = countrow + countcol
        
        
        return move
            
        
        