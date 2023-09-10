# 주유소
import sys

city_count = int(sys.stdin.readline())
distances = [*map(int, sys.stdin.readline().split())]
prices = [*map(int, sys.stdin.readline().split())]

min_price = 1000000001
answer = 0

for index, price in enumerate(prices[:-1]):
    min_price = min(min_price, price)
    answer += distances[index] * min_price

print(answer)

