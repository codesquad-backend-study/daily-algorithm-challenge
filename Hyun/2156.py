n = int(input())

drinks = [int(input()) for _ in range(n)]

d = [[0] * 2 for _ in range(n)]

d[0][0] = 0
d[0][1] = drinks[0]

if n >= 2:
    d[1][0] = drinks[0]
    d[1][1] = drinks[0] + drinks[1]

for i in range(2, n):
    d[i][0] = max(d[i - 1])
    d[i][1] = max(d[i - 1][0], d[i - 2][0] + drinks[i - 1]) + drinks[i]

print(max(d[-1]))
