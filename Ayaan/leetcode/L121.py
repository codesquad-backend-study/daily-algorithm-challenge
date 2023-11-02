def maxProfit(prices):
    profit = 0

    i = 0
    while(i < len(prices)-1):
        price = prices[i]
        for j in range(i+1, len(prices)):
            sell_price = prices[j]
            # sell_price가 price보다 작거나 같으면 i를 j로 바꾸고 반복문 탈출
            if sell_price <= price:
                i = j - 1
                break
            profit = max(profit, sell_price - price)
        i += 1

    return profit

result = maxProfit([7,6,5,4,3,2,1,0,0,0])
print(result)