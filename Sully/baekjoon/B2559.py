import sys
from typing import List


def solution(K: int, dates: List[int]) -> int:
    # 아래 반복문을 K부터 시작하니 K 전까지 슬라이싱한 값의 합을 저장
    current_sum, current_max = sum(dates[:K]), sum(dates[:K])

    for i in range(K, len(dates)):
        # dates[i: i + K]로 슬라이싱 하면서 구해줘도 되지만 O(N^2)이 돼버림
        # 그러니 효율적으로 끝과 끝을 비교하여 투포인터로 탐색
        current_sum += dates[i] - dates[i - K]
        current_max = max(current_max, current_sum)

    return current_max


N, K = map(int, sys.stdin.readline().rstrip().split())
dates = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(K, dates))
