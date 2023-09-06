# 보석 도둑
import heapq
import sys

stone_count, bag_count = map(int, sys.stdin.readline().split())

stones = sorted([tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(stone_count)])
bags = sorted([int(sys.stdin.readline()) for _ in range(bag_count)])

max_price = 0
heap = []

for bag in bags:
    while stones and stones[0][0] <= bag:
        carat, price = stones[0]  # 정렬해서 맨 앞에 있는 가장 가벼운 보석
        heapq.heappush(heap, -price)  # 가격을 음수로 전환하여 저장
        heapq.heappop(stones)
    if heap:
        max_price -= heapq.heappop(heap)  # 가장 큰 가격을 max_price에 더하기

print(max_price)
