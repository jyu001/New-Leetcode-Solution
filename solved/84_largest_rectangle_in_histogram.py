'''
84. Largest Rectangle in Histogram
DescriptionHintsSubmissionsDiscussSolution
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.


'''


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []: return 0
        res = []
        lst = [(heights[0],0)]
        for j in range(1,len(heights)):
            h, left = heights[j], j
            n = len(lst)
            for i in range(n-1, -1, -1):
                if lst[i][0]>h: 
                    left = lst[i][1]
                    res.append((j-lst[i][1])*lst[i][0])
                    lst.pop(i)
                    if i == 0: lst += [(h, left)]
                elif lst[i][0]<h:
                    if i==n-1: lst += [(h, j)]
                    else: lst += [(h, left)]
                    break
            #print(lst, res)
        n = len(heights)
        for i in range(len(lst)):
            res.append((n-lst[i][1])*lst[i][0])
                
        return max(res)
        