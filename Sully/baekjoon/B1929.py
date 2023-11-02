import collections
import sys
from typing import List


def solution(A: List[int], B: List[int]) -> List[int]:
    answer = []

    # A에 담긴 수들을 해시 테이블에 저장
    # {수: 1}
    A_map = collections.defaultdict()
    for a in A:
        A_map[a] = 1

    for b in B:
        if b in A_map:
            answer.append(1)
            continue

        answer.append(0)

    return answer


N = int(input())  # 무쓸모
A = list(map(int, sys.stdin.readline().split()))
M = int(input())  # 무쓸모
B = list(map(int, sys.stdin.readline().split()))

print(*solution(A, B), sep='\n')
