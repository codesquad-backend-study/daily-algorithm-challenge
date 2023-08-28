import sys
from typing import List


def solution(favors_list: List[List[int]]) -> int:
    answer = float('inf')
    check = [False] * len(favors_list)

    def dfs(cnt: int, depth: int, S: int, B: int):
        nonlocal answer

        if cnt >= 1:
            answer = min(abs(S - B), answer)

        for i in range(depth, len(favors_list)):
            if check[i]:
                continue

            check[i] = True
            dfs(cnt + 1, i, S * favors_list[i][0], B + favors_list[i][1])
            # 백트래킹
            check[i] = False

    dfs(0, 0, 1, 0)

    return answer


N = int(sys.stdin.readline().rstrip())
favors_list: List[List[int]] = []

for _ in range(N):
    favors_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(favors_list))
