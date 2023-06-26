import sys
sys.setrecursionlimit(10000)

def solution():
    N, M, K = map(int, input().split())

    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    def dfs(x, y):
        if x < 0 or x >= M or y < 0 or y >= N or graph[x][y] == 0:
            return

        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x, y - 1)

    result = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                result += 1
                dfs(i, j)
    print(result)


for _ in range(int(input())):
    solution()
