import collections
import sys
from typing import List


def solution(m: int, n: int, nums: List[List[int]]) -> int:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x: int, y: int) -> int:
        dq = collections.deque()
        dq.append((x, y))

        while dq:
            x, y = dq.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if nums[ny][nx] == 0:
                    continue

                if nums[ny][nx] == 1:
                    nums[ny][nx] = nums[y][x] + 1
                    dq.append((nx, ny))

        return nums[n - 1][m - 1]

    return bfs(0, 0)


N, M = map(int, sys.stdin.readline().rstrip().split())

# 문제 잘못 읽어서 M, N 또 반대로 생각함. 여기서 시간 날림
array = []
for _ in range(N):
    array.append([int(x) for x in sys.stdin.readline().rstrip()])

print(solution(M, N, array))
