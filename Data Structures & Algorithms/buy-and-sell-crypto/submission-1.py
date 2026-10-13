class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minuend = prices[0]
        subtrahend = 0
        max_profit = 0
        
        for i in range(len(prices) - 1, 0, -1):
            if (prices[i] - min(prices[:i]) > max_profit):
                max_profit = prices[i] - min(prices[:i])

        return max_profit
        