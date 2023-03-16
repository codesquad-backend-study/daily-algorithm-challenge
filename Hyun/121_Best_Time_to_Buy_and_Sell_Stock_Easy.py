class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        profit = 0

        for i in range(len(prices) - 1, -1, -1):
            max_price = max(max_price, prices[i])
            profit = max(profit, max_price - prices[i])

        return profit