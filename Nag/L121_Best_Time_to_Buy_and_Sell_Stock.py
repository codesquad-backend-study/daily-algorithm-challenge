#이건 도저희 못풜겠어서 답지 봤습니다...

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            if prices[left] <= prices[right]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right = right + 1
        return profit
