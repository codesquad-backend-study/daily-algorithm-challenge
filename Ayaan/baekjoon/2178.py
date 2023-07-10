import collections

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = collections.deque([(0, 0)])

# bfs
while q:
    x, y = q.popleft()

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < N and 0 <= my < M and graph[mx][my] == '1':
            q.append((mx, my))
            graph[mx][my] = int(graph[x][y]) + 1
print(graph[N - 1][M - 1])
