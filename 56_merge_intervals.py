'''
56. Merge Intervals
DescriptionHintsSubmissionsDiscussSolution
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        lst = [(i.start, i.end, indx) for indx, i in enumerate(intervals) ]
        lst = sorted(lst)
        res = []
        for i in range(len(lst)):
            if i==0: res.append(Interval(lst[i][0], lst[i][1]))
            if lst[i][0]>res[-1].end: res.append(intervals[lst[i][2]])
            elif lst[i][1]>res[-1].end: res[-1].end = lst[i][1]
        return res