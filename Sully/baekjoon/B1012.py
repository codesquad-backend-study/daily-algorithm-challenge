import sys
from typing import List

# DFS로 풀려면 넣어줘야 됨
sys.setrecursionlimit(10**7)


# m: 배추밭의 가로 길이
# n: 배추밭의 세로 길이
# nums: 배추의 위치 [x, y]를 기준으로 하는 2차원 배열
def solution(m: int, n: int, nums: List[List[int]]) -> int:
    answer = 0
    # 이 문제는 그래프를 만들어서 푸는 것밖에 생각나지 않음 ㅠㅠ
    graph = [[0] * m for _ in range(n)]

    for num in nums:
        xn, yn = num[0], num[1]
        graph[yn][xn] = 1

    def dfs(x: int, y: int):
        # 여기 m, n 뒤바뀐 거 인지 못 해서 2시간 날렸다
        if x < 0 or y < 0 or x >= m or y >= n:
            return False

        if graph[y][x] == 1:
            # visited 사용하지 않고 예전에 알고리즘 책에서 했던 것처럼 0으로 표시
            graph[y][x] = 0

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

            return True

        return False

    for ys in range(n):
        for xs in range(m):
            if dfs(xs, ys):
                answer += 1

    return answer


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    array = []
    for _ in range(K):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(solution(M, N, array))
