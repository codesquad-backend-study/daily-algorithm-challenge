class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 풀이 1. 시간초과
        profit = 0
        for i, buy in enumerate(prices[:-1]):
            sell = max(prices[i+1:])
            profit = max(sell-buy,profit)
        profit = 0 if profit < 0 else profit
        # return profit

        # 풀이 2. 통과
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                profit = max(profit,price-buy)
        return profit