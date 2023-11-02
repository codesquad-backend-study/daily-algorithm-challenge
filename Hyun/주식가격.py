def solution(prices):
    stack = []
    ans = [0] * len(prices)

    for idx, price in enumerate(prices):

        while stack and stack[-1][1] > price:
            pop_idx, _ = stack.pop()
            ans[pop_idx] = idx - pop_idx

        stack.append((idx, price))

    while stack:
        pop_idx, _ = stack.pop()
        ans[pop_idx] = len(prices) - 1 - pop_idx

    return ans
