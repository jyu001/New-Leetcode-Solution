'''
335. Self Crossing
DescriptionHintsSubmissionsDiscussSolution
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
Given x = [2, 1, 1, 2],
?????
?   ?
???????>
    ?

Return true (self crossing)
Example 2:
Given x = [1, 2, 3, 4],
????????
?      ?
?
?
?????????????>

Return false (not self crossing)
Example 3:
Given x = [1, 1, 1, 1],
?????
?   ?
?????>

Return true (self crossing)
'''

class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x)<=3: return False
        if len(x)==4: return x[3]>=x[1] and x[2]<=x[0]
        # define the horizontal and vertical boundaries
        side = []
        n = 3
        while x[n-1] > x[n-3] and x[n] > x[n-2]:
            n += 1
            if n>=len(x)-1: return False
            
        if n==3: side = [x[2], x[1]]
        elif x[n] < x[n-2] - x[n-4]: side = [x[n], x[n-1]] if n%2==1 else [x[n-1], x[n]]
        else: side = [x[n], x[n-1]-x[n-3]] if n%2==1 else [x[n-1]-x[n-3], x[n]]
        n += 1
        
        #print('0', n, x[n], side, side[(n-1)%2])
            
        while x[n]<side[(n-1)%2]: 
            #print(n, x[n], side, side[(n-1)%2])
            side[(n-1)%2] = x[n]
            n+=1
            if n==len(x):  return False
        return True