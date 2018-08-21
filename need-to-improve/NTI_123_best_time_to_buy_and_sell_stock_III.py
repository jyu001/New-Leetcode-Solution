'''
123. Best Time to Buy and Sell Stock III
DescriptionHintsSubmissionsDiscussSolution
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if len(prices)<2: return 0
        
        j = 1
        while j < n-1:
            if prices[j-1]>=prices[j]>=prices[j+1] or prices[j-1]<=prices[j]<=prices[j+1]: 
                prices.pop(j)
                n-=1
            else: j += 1
        
        #print ( prices)
        
        def check(prices):
            n = len(prices)
            if n<2: return 0
            minm = prices[0]
            res = 0
            for i in range(1, n):
                res = max(res, prices[i]-minm)
                minm = min(minm, prices[i])
            return res
        
        res = 0
        for i in range(1, len(prices)):
            res = max(res, check(prices[:i+1]) + check(prices[i+1:]))
        return res