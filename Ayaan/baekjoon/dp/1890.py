N = int(input())
board = [[*map(int, input().split())] for _ in range(N)]
dp = [[0 for _ in range(109)] for _ in range(109)]
dp[0][0] = 1

# dp[i][j] = (i,j)로 이동할 수 있는 경우의 수
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 0:
            continue
        dp[i][j + board[i][j]] += dp[i][j]
        dp[i + board[i][j]][j] += dp[i][j]

print(dp[N - 1][N - 1])
