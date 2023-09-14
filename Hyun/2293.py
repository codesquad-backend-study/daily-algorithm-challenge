n, target = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [0] * 10_0001
d[0] = 1

for coin in coins:
    for i in range(coin, target + 1):
        d[i] += d[i - coin]

print(d[target])
