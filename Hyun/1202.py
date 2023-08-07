import heapq

jewel_cnt, bag_cnt = map(int, input().split())

jewels = []

for _ in range(jewel_cnt):
    heapq.heappush(jewels, tuple(map(int, input().split())))

bags = sorted([int(input()) for _ in range(bag_cnt)])

price_sum = 0

liftable_jewels = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(liftable_jewels, -heapq.heappop(jewels)[1])

    if liftable_jewels:
        price_sum -= heapq.heappop(liftable_jewels)
    elif not jewels:
        break

print(price_sum)
