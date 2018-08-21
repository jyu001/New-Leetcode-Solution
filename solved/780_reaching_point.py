'''
780. Reaching Points
DescriptionHintsSubmissionsDiscussSolution
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

'''

class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx>=sx and ty>=sy:
            if tx>ty and tx-sx>ty: tx, ty = tx-ty*((tx-sx)//ty), ty
            elif tx>ty: tx, ty = tx-ty, ty
            elif ty>tx and ty-sy>tx: tx, ty = tx, ty-tx*((ty-sy)//tx)
            elif ty>tx: tx, ty = tx, ty-tx
                
            print(tx, ty)
                
            if tx==sx and ty==sy: return True
            elif tx<sx or ty<sy or tx==ty: return False
        return False