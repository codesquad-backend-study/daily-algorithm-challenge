import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)
ans = 0

if len(cards) == 1:
    print(0)
    exit(0)

while cards:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    ans += a + b

    if cards:
        heapq.heappush(cards, a + b)

print(ans)
