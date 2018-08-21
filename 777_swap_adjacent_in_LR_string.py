'''
777. Swap Adjacent in LR String
DescriptionHintsSubmissionsDiscussSolution
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.

'''

class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if not len(start)==len(end): return False
        if not start.replace('X','')==end.replace('X',''): return False
        
        def check(s):
            lst = []
            for i in range(len(s)):
                if s[i] == 'R': lst.append(-i-1)
                if s[i] == 'L': lst.append(i+1)
            return lst
        
        st, e = check(start), check(end)
        for i in range(len(st)):
            #print(st[i], e[i])
            if st[i]*e[i]<0: return False
            elif st[i]<e[i]: return False
        return True