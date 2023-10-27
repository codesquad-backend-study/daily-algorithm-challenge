def solution(prices):
    answer = [0 for _ in range(len(prices))]

    stack = []
    previous = prices[0]

    for index, price in enumerate(prices):
        if previous > price:
            while stack and stack[-1][1] > price:
                i, p = stack.pop()
                answer[i] = index - i

        stack.append((index, price))
        previous = price

    last_index = len(prices) - 1

    while stack:
        i, p = stack.pop()
        answer[i] = last_index - i

    return answer
