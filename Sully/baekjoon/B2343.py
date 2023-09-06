import sys
from typing import List


def solution(M: int, lengths: List[int]) -> int:
    answer = 0

    # lt: 블루레이가 가질 수 있는 가장 작은 크기
    # rt: 하나의 블루레이에 다 담을 수 있음 -> 즉, lengths의 합
    lt, rt = max(lengths), sum(lengths)
    while lt <= rt:
        mid = (lt + rt) // 2

        tmp_sum, cnt = 0, 1
        for length in lengths:
            if length + tmp_sum > mid:
                cnt += 1
                tmp_sum = 0

            tmp_sum += length

        if cnt <= M:
            answer = mid
            rt = mid - 1
            continue

        lt = mid + 1

    return answer


N, M = map(int, sys.stdin.readline().rstrip().split())
lengths = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(M, lengths))
