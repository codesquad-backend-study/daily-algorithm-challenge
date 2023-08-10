import sys
from typing import List


def solution(L: int, waters: List[int]) -> int:
    # 물이 새는 위치의 거리 < 테이프의 길이 -> 한 번에 막을 수 있음
    answer = 1

    waters.sort()

    # 테이프 시작 위치
    start = 0
    for i in range(1, len(waters)):
        # waters[i] - waters[start]: 물이 새는 위치의 거리
        if waters[i] - waters[start] < L:
            continue

        # 테이프 시작 위치 업데이트
        start = i
        # 테이프 개수들 계속 추가해 나가자
        answer += 1

    return answer


N, L = map(int, sys.stdin.readline().rstrip().split())
waters = list(map(int,sys.stdin.readline().rstrip().split()))

print(solution(L, waters))
