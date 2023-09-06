import sys
from typing import List


def solution(houses: List[List[int]]) -> List[int]:
    global cnt

    answer = []
    cnt = 0

    def dfs(x: int, y: int) -> bool:
        global cnt

        if x < 0 or y < 0 or x >= len(houses) or y >= len(houses):
            return False

        if houses[y][x] == 1:
            cnt += 1
            houses[y][x] = 0

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

            return True

        return False

    for ys in range(len(houses)):
        for xs in range(len(houses)):
            if dfs(xs, ys):
                answer.append(cnt)
                cnt = 0

    answer.sort()
    answer.insert(0, len(answer))
    return answer


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().rstrip())))

print(*solution(array), sep='\n')
