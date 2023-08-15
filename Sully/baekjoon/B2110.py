import sys
from typing import List


def solution(C: int, houses: List[int]) -> int:
    answer = 0

    houses.sort()

    # lt: 최소 공유기 거리 -> 1
    # rt: 최대 공유기 거리 -> (맨 끝 - 맨 앞)
    lt, rt = 1, houses[-1] - houses[0],

    while lt <= rt:
        current = houses[0]
        mid = (lt + rt) // 2
        # cnt: lt를 1로 둔 것과 같은 이유
        cnt = 1

        # 맨 앞에는 항상 공유기를 설치해야 -> 거리가 최대가 될 수 있음
        for i in range(1, len(houses)):
            if houses[i] - current >= mid:
                current = houses[i]
                cnt += 1

        if cnt >= C:
            # 위 조건에 answer를 mid의 값으로 갱신
            if answer < mid:
                answer = mid

            lt = mid + 1
            continue

        # if cnt < C: -> mid 값이 너무 크다는 뜻
        rt = mid - 1

    return answer


N, C = map(int, sys.stdin.readline().rstrip().split())
houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline().rstrip()))

print(solution(C, houses))
