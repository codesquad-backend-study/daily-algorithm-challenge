from collections import deque

T = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(T):
    n = int(input())
    chess = [[0] * n for _ in range(n)]
    this_x, this_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    q = deque([(this_x, this_y)])
    def bfs():
        while q:
            now = q.popleft()
            if now[0] == target_x and now[1] == target_y:
                print(chess[now[0]][now[1]])
                return
            for i in range(8):
                next_x = now[0] + dx[i]
                next_y = now[1] + dy[i]
                if 0 <= next_x < n and 0 <= next_y < n and chess[next_x][next_y] == 0:
                    chess[next_x][next_y] = chess[now[0]][now[1]] + 1
                    q.append((next_x, next_y))

    bfs()
