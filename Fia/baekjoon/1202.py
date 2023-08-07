# 보석 도둑
import heapq
import sys

stone_count, bag_count = map(int, sys.stdin.readline().split())

stones = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(stone_count)]
bags = sorted([int(sys.stdin.readline()) for _ in range(bag_count)])

heapq.heapify(stones)

max_price = [0] * bag_count

for number, bag in enumerate(bags):
    heap = []  # (price, carat)
    passed = []

    while stones:
        carat, price = heapq.heappop(stones)

        if carat > bag:
            heapq.heappush(stones, (carat, price))
            break

        if price > max_price[number]:
            max_price[number] = price

            if len(heap) == 0:
                heapq.heappush(heap, (price, carat))
                continue

            popped = heapq.heappushpop(heap, (price, carat))
            passed.append((popped[1], popped[0]))

    stones.extend(passed)
    heapq.heapify(stones)

print(sum(max_price))
