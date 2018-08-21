'''
149. Max Points on a Line
DescriptionHintsSubmissionsDiscussSolution
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        from fractions import Fraction
        
        if len(points) < 3: return len(points)
        
        ovlp = {} # count of overlapping points
        for p in points:
            x,y = p.x, p.y
            if (x,y) not in ovlp: ovlp[(x,y)] = 1
            else: ovlp[(x,y)] += 1
        uniq = list(ovlp.keys())
        #print(uniq)
        if len(uniq) < 3: return len(points)
        
        dct = {}
        for i in range(len(uniq)-1):
            for j in range(i+1,len(uniq)):
                p, q = uniq[i], uniq[j]
                x, y = p[0]-q[0], p[1]-q[1]
                (slope,inter) = (2147483647,0)
                if x!=0: (slope,inter) = (Fraction(y,x), Fraction(p[1]*x-p[0]*y, x))
                else: inter = p[0]
                #print(i,j, slope, inter)
                if (slope,inter) not in dct: dct[(slope,inter)] = [i, j]
                else: dct[(slope,inter)] += [i, j]
        #print(dct.values())
        maxm = 0
        
        for l in dct.values():
            pts = list(set(list(l)))
            count = 0
            for i in range(len(pts)): count += ovlp[uniq[pts[i]]]
            maxm = max(maxm, count)
        return maxm
        
            