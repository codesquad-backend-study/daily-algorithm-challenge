# 동전 1
import sys

# 동전의 종류, 목표로 하는 가치의 합
count, target = map(int, sys.stdin.readline().split())

# 동전의 가치
coins = [int(sys.stdin.readline()) for _ in range(count)]

# 목표로 하는 가치의 합 + 1만큼의 리스트 생성
table = [0 for _ in range(target + 1)]

# 인덱스 0은 동전을 1개만 사용할 때의 경우의 수를 의미한다
table[0] = 1

# 가치가 c인 동전을 사용해서 합이 k가 되는 경우의 수 += (k - c)의 경우의 수
for coin in coins:
    for j in range(coin, target + 1):
        table[j] += table[j - coin]

print(table[target])

