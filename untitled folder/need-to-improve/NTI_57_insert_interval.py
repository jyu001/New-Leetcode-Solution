'''
57. Insert Interval
DescriptionHintsSubmissionsDiscussSolution
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []: return [newInterval]
        n = len(intervals)
        nl, nr = newInterval.start, newInterval.end
        if nr < intervals[0].start: return [newInterval] + intervals
        elif nl > intervals[n-1].end: return intervals + [newInterval]
        
        lst = []
        for i in intervals:
            lst += [i.start, i.end]
        left, right = 0, 2*n+2
        
        #print(lst)
        
        for i in range(n):
            if nl > lst[2*i + 1]: continue
            elif nl >= lst[2*i]: 
                left = 2*i + 1
                break
            else: 
                left = 2*i
                break
        for i in range(n):
            j = n-1-i
            if nr < lst[2*j]: continue
            elif nr <= lst[2*j+1]: 
                right = 2*j + 1
                break
            else: 
                right = 2*j+2
                break
        
        #print(left, right)
        
        
        if left%2: newInterval.start = intervals[left//2].start
        if right%2: 
            newInterval.end = intervals[right//2].end
            right += 2
        return intervals[:left//2] + [newInterval] + intervals[right//2:]
        
                