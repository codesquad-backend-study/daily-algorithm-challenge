import sys
from typing import List

sys.setrecursionlimit(10 ** 6)


def solution(n: int, spaces: List[List[int]]) -> int:
    answer = []

    def dfs(x: int, y: int, h: int) -> bool:
        if x < 0 or y < 0 or x >= n or y >= n:
            return False

        if spaces[y][x] > h and not visited[y][x]:
            visited[y][x] = True

            dfs(x - 1, y, h)
            dfs(x, y - 1, h)
            dfs(x, y + 1, h)
            dfs(x + 1, y, h)

            return True

        return False

    # 1 < N < 101
    for h in range(101):
        cnt = 0
        visited = [[False] * n for _ in range(n)]

        for y in range(n):
            for x in range(n):
                if dfs(x, y, h):
                    cnt += 1

        answer.append(cnt)

        if cnt == 0:
            break

    return max(answer)


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, array))
