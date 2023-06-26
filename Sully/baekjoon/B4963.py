import sys
from typing import List

sys.setrecursionlimit(10 ** 4)


def solution(weight: int, height: int, maps: List[List[int]]) -> int:
    answer = 0

    def dfs(x: int, y: int):
        if x < 0 or y < 0 or x >= weight or y >= height:
            return False

        if maps[y][x] == 1:
            maps[y][x] = 0

            dfs(x - 1, y - 1)
            dfs(x - 1, y)
            dfs(x - 1, y + 1)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y)
            dfs(x + 1, y + 1)

            return True

        return False

    for y in range(height):
        for x in range(weight):
            if dfs(x, y):
                answer += 1

    return answer


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())

    if w == 0 and h == 0:
        break

    array = []
    for _ in range(h):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(solution(w, h, array))
