# d[n][0] = d[n-1][0]
# d[n][k] = d[n-1][k] + d[n][k-1]

d = [[0] * 10 for _ in range(65)]
for i in range(10):
    d[1][i] = 1

t = int(input())
for _ in range(t):
    n = int(input())

    for i in range(2, n + 1):
        d[i][0] = 1

        for j in range(1, 10):
            d[i][j] = d[i - 1][j] + d[i][j - 1]

    print(sum(d[n]))
