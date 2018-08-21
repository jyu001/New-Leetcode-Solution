'''
248. Strobogrammatic Number III
DescriptionHintsSubmissionsDiscussSolution
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.


'''

class Solution:
    def findallStro(self, n):
        if n==0: return []
        if n==1: return ['1','0','8']
        if n==2: return ['00',"11","69","88","96"]
        res = []
        if n>2:
            listn = self.findallStro(n-2)
            for s in listn:
                res.extend(['1'+s+'1', '0'+s+'0', '6'+s+'9','9'+s+'6','8'+s+'8'])
        return res
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        n = len(high)
        numl, numh = int(low), int(high)
        res = []
        for i in range(n+1): res.extend(self.findallStro(i)) 
        #newres = []
        count = 0
        for s in res:
            if len(s)!= 1 and s[0] == '0': continue
            num = int(s)
            #print(s, numl, numh)
            if num >= numl and num <= numh:
                #newres.append(s)
                count += 1
        #print (count, newres)
        return count
        
        