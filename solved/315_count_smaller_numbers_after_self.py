'''
315. Count of Smaller Numbers After Self
DescriptionHintsSubmissionsDiscussSolution
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        if n == 1: return [0]
        res = [0]
        #sl = sorted(set(nums)) # sortedlist
        nl = [nums[-1]]       #updated new list, including rear elements
        lennl = 1
        for i in range(n-1):
            new = nums[n-2-i]
            #insert new into nl
            l = 0
            r = lennl -1          # left: large number, right: small number
            m = (r+l)//2
            #print(l,m,r)
            while r-l > 0:
                if new > nl[m]: 
                    r = m-1
                    m = (r+l)//2   
                else: 
                    l = m
                    m = (r+l+1)//2    
                #print(new, nl, l, m, r)
            if new > nl[l]:
                res = [lennl - l] + res
                #nl = nl[0:l] + [new] + nl[l:]
                nl.insert(l, new)
            else:
                res = [lennl - l -1] + res
                if l == lennl-1:
                    #nl = nl + [new]
                    nl.append(new)
                else:
                    #nl = nl[0:l+1] + [new] + nl[l+1:]
                    nl.insert(l+1, new)
            lennl += 1
            #print(new, nl, res)
        return res
        