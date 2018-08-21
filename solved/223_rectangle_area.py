'''
223. Rectangle Area
DescriptionHintsSubmissionsDiscussSolution
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.


'''

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # the key is to find out the overlapping part:
        l = max(A,E)
        r = max(l,min(C,G)) # if l>min(C,G): no overlap
        b = max(B,F)
        t = max(b,min(D,H))
        return (C-A)*(D-B) + (G-E)*(H-F) - (r-l)*(t-b)
            