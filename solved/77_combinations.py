'''
77. Combinations
DescriptionHintsSubmissionsDiscussSolution
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        full = [i for i in range(1,n+1)]
        
        def check(k,lst):
            n = len(lst)
            if n==k: return [lst]
            if k>n or k==0: return [[]]
            res = []
            #print('n,k', n, k)
            for i in range(n-k+1):
                l = lst[i+1:]
                for ll in check(k-1, l): 
                    res.append([lst[i]] + ll)
            return res
        
        return check(k,full)    