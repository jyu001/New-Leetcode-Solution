'''
218. The Skyline Problem
DescriptionHintsSubmissionsDiscussSolution
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if buildings == []: return []
        n,i = len(buildings), 1
        while i < n:
            l1,r1,h1, l0,r0,h0 = buildings[i][0], buildings[i][1], buildings[i][2], buildings[i-1][0], buildings[i-1][1], buildings[i-1][2]
            if h1<=h0 and l1>=l0 and r1<=r0: 
                n -= 1
                buildings.pop(i)
            else: i+=1
        pset = set([])
        for bld in buildings:
            for i in [ bld[0], bld[1] ]:
                if i in pset: continue
                else: pset.add(i)
        plst = sorted(list(pset))
        #print (pset)
        lst = []
        for i in range(len(plst)-1):
            lst.append([plst[i],plst[i+1],0])
        for bld in buildings:
            l, r = bld[0], bld[1]
            for i in lst:
                if i[0]<l or i[1]>r : continue
                else: i[2] = max(bld[2], i[2])
        #print(lst)
        res = []
        i = 0
        while i < len(lst)-1:
            l1,r1,h1 = lst[i][0], lst[i][1], lst[i][2]
            while i+1 < len(lst) and lst[i+1][2] == lst[i][2]:
                r1 = lst[i+1][1]
                i += 1
            i += 1
            res.append([l1, h1])
        if i == len(lst): res.append([lst[i-1][1], 0])
        else: res += [ [lst[i][0], lst[i][2]], [lst[i][1], 0] ]
        #print(res)
        
        return res