import sys
from typing import List


def solution(N: int, values: List[int]) -> List[int]:
    #  정렬 -> 용액의 최소: 왼쪽, 최대: 오른쪽
    values.sort()

    start, end = 0, N - 1
    min_start, min_end = 0, 0
    # 파이썬에서 제일 큰 수: float('inf')
    min_total = float('inf')

    while start < end:
        total = values[start] + values[end]

        if abs(total) < abs(min_total):
            min_total = total
            min_start = values[start]
            min_end = values[end]

        if total == 0:
            break

        if total < 0:
            start += 1
        else:
            end -= 1

    return [min_start, min_end]


N = int(sys.stdin.readline().rstrip())
values = list(map(int, sys.stdin.readline().rstrip().split()))

print(*solution(N, values))
