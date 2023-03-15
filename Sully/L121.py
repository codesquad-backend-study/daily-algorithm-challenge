from typing import List


class Solution:
    # prices[i] -> i번째 날의 주식의 가격
    # 어느 하루에 주식을 살 수 있고, "그 후" 다른 날에 주식을 팔 수 있음.
    # 실현 가능한 가장 큰 이익 (return the maximum profit) 구하자! -> 어떤 이익도 없을 경우 0 리턴

    # O(n)
    # 주식이 가장 저렴했을 때를 생각하자 -> 각 시점에서의 최대 이익 구할 수 있음
    def maxProfit(self, prices: List[int]) -> int:
        # 최대 이익 -> 어떤 이익이 없을 경우 0을 리턴하니 초기값 0으로 세팅
        max_profit = 0
        # 과거의 "최저 주가" -> 초기값으로 첫번째 요소 세팅
        min_price = prices[0]

        # prices: i번째의 주식의 가격 배열 -> price: 그 주식의 가격
        for price in prices:
            # 현재 얻을 수 있는 그 시점에서의 최대 이익 계속 갱신
            # price에서 min_price를 빼주는 이유는
            # 최대 이익은 현재 주가에서 과거의 최저 주가를 그냥 빼주면 되기 때문
            # 현재 주가에서 과거의 최저 주가를 빼준 값에서 또 가장 큰 값이 최대 이익 중 가장 큰 값이 됨
            max_profit = max(price - min_price, max_profit)
            # prices의 최솟값 계속 갱신
            min_price = min(price, min_price)

        return max_profit

# O(n^2) -> Time Limit Exceeded로 실패
# 가능한 배열 모든 요소에서 주식 buy and sell
# def maxProfit(self, prices: List[int]) -> int:
#     # 어떤 이익이 없을 경우 0을 리턴하니 초기값 0으로 세팅
#     max_profit = 0
#
#     # len(prices) - 1: 주식을 사는 것은 마지막에서 바로 앞까지
#     for buy_stock in range(len(prices) - 1):
#         # 주식을 파는 것은 산 시점에서 한칸 뒤부터 마지막까지
#         for sell_stock in range(buy_stock + 1, len(prices)):
#             # 현재 이익 (sell의 주식 값 - buy의 주식 값)
#             profit = prices[sell_stock] - prices[buy_stock]
#             max_profit = max(profit, max_profit)
#
#     return max_profit
