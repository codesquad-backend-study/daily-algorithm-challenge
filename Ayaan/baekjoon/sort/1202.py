import collections
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jewelries = []
for _ in range(N):
    weight, price = map(int, sys.stdin.readline().split())
    jewelries.append((weight, price))
jewelries.sort()
jewelries = collections.deque(jewelries)

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline().rstrip()))
bags.sort()

max_price = 0
whats_in_my_bag = []
for bag in bags:
    while jewelries and jewelries[0][0] <= bag:
        heapq.heappush(whats_in_my_bag, -jewelries[0][1])
        jewelries.popleft()
    if whats_in_my_bag:
        max_price += (-heapq.heappop(whats_in_my_bag))
print(max_price)
