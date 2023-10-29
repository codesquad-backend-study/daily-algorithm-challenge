import collections
from typing import List


def solution(prices: List[int]):
    answer = []

    dq = collections.deque(prices)
    while dq:
        # 가격이 떨어지지 않은 기간
        period = 0
        # 주식 가격
        price = dq.popleft()

        for current_price in dq:
            period += 1
            # 현재 가격이 위의 가격보다 낮으면 가격이 떨어졌다는 것을 의미
            if current_price < price:
                break

        answer.append(period)

    return answer


print(solution([1, 2, 3, 2, 3]))
