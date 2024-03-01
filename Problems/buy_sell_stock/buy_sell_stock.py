'''
You are given an array prices where prices[i] is the price
of a given stock on the ith day.

You want to maximize your profit by choosing a single day to 
buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0
            
        max = 0
        min = 10001

        for price in prices:
            if price < min:
                min = price
            elif price - min > max:
                max = price - min
        return max
    
# Runtime: 744 ms -- Beats 67.22% of users with Python 3
# Memory: 28.15 mb -- Beats 27.04% of users with Python 3