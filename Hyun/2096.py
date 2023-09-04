# d[n][0] = max(d[n-1][0], d[n-1][1]) + a[n][0]
# d[n][1] = max(d[n-1]) + a[n][1]
# d[n][2] = max(d[n-1][1], d[n-1][2]) + a[n][2]


n = int(input())
d = [[0] * 3 for _ in range(n)]

a = [list(map(int, input().split())) for _ in range(n)]

d[0] = a[0]

for i in range(1, n):
    d[i][0] = max(d[i - 1][0], d[i - 1][1]) + a[i][0]
    d[i][1] = max(d[i - 1]) + a[i][1]
    d[i][2] = max(d[i - 1][1], d[i - 1][2]) + a[i][2]

max_val = max(d[-1])

for i in range(1, n):
    d[i][0] = min(d[i - 1][0], d[i - 1][1]) + a[i][0]
    d[i][1] = min(d[i - 1]) + a[i][1]
    d[i][2] = min(d[i - 1][1], d[i - 1][2]) + a[i][2]

min_val = min(d[-1])

print(max_val, min_val)
