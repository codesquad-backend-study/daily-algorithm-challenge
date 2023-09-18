import sys
from typing import List


def solution(N: int, nums_list: List[List[int]]) -> int:
    # dp: 해당 위치로 올 수 있는 경로의 개수의 배열
    dp = [[0] * N for _ in range(N)]
    # (0, 0) 위치는 항상 올 수 있으므로 1로 설정
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            # 현재의 위치가 가장 오른쪽 아래 칸이라면 종료
            if i == N - 1 and j == N - 1:
                break

            current_jump = nums_list[i][j]

            # 현재 위치만큼 "아래로" 이동한 거리가 유효하다면
            # 그 위치의 경로의 개수에 현재 위치의 경로 개수를 더함
            if 0 <= i + current_jump < N:
                dp[i + current_jump][j] += dp[i][j]

            # 현재 위치만큼 "오른쪽으로" 이동한 거리가 유효하다면
            # 그 위치의 경로의 개수에 현재 위치의 경로 개수를 더함
            if 0 <= j + current_jump < N:
                dp[i][j + current_jump] += dp[i][j]

    return dp[N - 1][N - 1]


N = int(sys.stdin.readline().rstrip())
nums_list: List[List[int]] = []
for _ in range(N):
    nums_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, nums_list))
