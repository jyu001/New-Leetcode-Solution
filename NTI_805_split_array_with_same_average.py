'''
805. Split Array With Same Average
DescriptionHintsSubmissionsDiscussSolution
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
'''

class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        from fractions import Fraction
        if len(A) == 1: return False
        avg = Fraction(sum(A), len(A))
        B = []
        C = []
        for a in A:
            if a==avg: return True
            if a>avg: B.append(a-avg)
            if a<avg: C.append(avg-a)
        half = sum(B)
        setc = set([0, C[0]])
        setb = set([0, B[0]])
        for i in range(1,len(B)):
            for j in list(setb):
                if B[i]+j not in setb:
                    setb.add(B[i]+j)
        #print(B,C)
        #print(sorted(list(setb)))
        if C[0] in setb and C[0]<half: return True
        for i in range(1,len(C)):
            for j in list(setc):
                if C[i]+j not in setc:
                    if C[i]+j in setb and C[i]+j<half: return True
                    setc.add(C[i]+j)
        #print(sorted(list(setc)))
        return False