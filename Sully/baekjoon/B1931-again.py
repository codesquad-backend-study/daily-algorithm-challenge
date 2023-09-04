import sys
from typing import List


def solution(meetings: List[List[int]]) -> int:
    answer = 0

    # x[1]: end 시간이 빠를수록 최대에 가까움, 그러므로 가장 먼저 정렬
    # x[0]: end 시간과 start 시간이 가까울수록 최대에 가까움
    sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    before_end = 0
    for m in sorted_meetings:
        # 계산 순서: end -> start
        current_start, current_end = m[0], m[1]

        if current_start >= before_end:
            answer += 1

            # 현재의 end로 초기화
            before_end = current_end

    return answer


N = int(input())

meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

print(solution(meetings))
