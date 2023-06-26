import collections

def solution():
    N = int(input())
    map = []
    for _ in range(N):
        map.append(list(input()))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 연결된 단지 카운트
    count = collections.defaultdict(int)
    def dfs(num, x, y):
        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i]
            if move_x < 0 or move_x >= N or move_y < 0 or move_y >= N:
                continue
            # '1'인 경우 0으로 바꾸고 dfs 탐색
            if map[move_x][move_y] == '1':
                map[move_x][move_y] = 0
                count[num] += 1
                dfs(num, move_x, move_y)

    num = 1
    for i in range(N):
        for j in range(N):
            if map[i][j] == '1':
                map[i][j] = 0
                count[num] += 1
                dfs(num, i, j)
                num += 1

    print(len(count))
    print(*sorted(count.values()), sep="\n")

solution()
