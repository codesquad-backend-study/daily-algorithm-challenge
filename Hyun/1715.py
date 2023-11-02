import heapq

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

ans = 0

while len(heap) >= 2:
    cards = heapq.heappop(heap) + heapq.heappop(heap)
    ans += cards
    heapq.heappush(heap, cards)

print(ans)
