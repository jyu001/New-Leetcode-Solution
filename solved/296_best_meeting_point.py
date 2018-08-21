'''
296. Best Meeting Point
DescriptionHintsSubmissionsDiscussSolution
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.

'''


class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        lstx, lsty = [], []
        for i in range(r): lsty.append(0)
        for i in range(c): lstx.append(0)
        ttl, distx, disty = 0, 0, 0
        for i in range(c):
            for j in range(r):
                lstx[i] += grid[j][i]
                ttl += grid[j][i]
                distx += grid[j][i]*i
                disty += grid[j][i]*j
                lsty[j] += grid[j][i]
        #print (lstx, lsty)
        lst = [lstx, lsty]
        dst = [distx, disty]
        #print (dst)
        minm = [distx, disty]
        for a in range(2):
            l= lst[a]
            left, right = 0, ttl
            for i in range(1, len(l)):
                left += l[i-1]
                right = ttl - left
                dst[a] += left - right
                minm[a] = min(minm[a], dst[a])
                print ('i=', i, ':   ','left', left, 'right', right, dst[a])
        #print(minm[0], minm[1])
        return minm[0]+minm[1]