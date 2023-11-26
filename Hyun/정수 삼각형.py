# d[0][0]
# d[1][0] d[1][1]
# d[2][0] d[2][1] d[2][2]

# d[n][0] = d[n-1][0] + a[n][0]
# d[n][i] = max(d[n-1][i-1], d[n-1][i]) + a[n][i]
# d[n][n] = d[n-1][n-1] + a[n][n]

def solution(triangle):
    d = [[0] * len(triangle) for _ in range(len(triangle))]

    d[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        d[i][0] = d[i - 1][0] + triangle[i][0]
        d[i][i] = d[i - 1][i - 1] + triangle[i][i]

        for j in range(1, i):
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + triangle[i][j]

    return max(d[-1])
