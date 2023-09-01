import sys
from typing import List


def solution(X: int, visitors: List[int]):
    # X일 동안의 누적 관광객 수
    max_visitors = sum(visitors[:X])
    most_visitor, period = max_visitors, 1

    for i in range(X, len(visitors)):
        # 누적 관광객 수 업데이트
        max_visitors += visitors[i] - visitors[i - X]

        if most_visitor < max_visitors:
            most_visitor = max_visitors
            period = 1
            continue

        # 유지한 기간 업데이트
        if most_visitor == max_visitors:
            period += 1

    if most_visitor:
        return [most_visitor, period]

    return ["SAD"]


N, X = map(int, sys.stdin.readline().rstrip().split())
visitors = list(map(int, sys.stdin.readline().rstrip().split()))

print(*solution(X, visitors), sep='\n')
