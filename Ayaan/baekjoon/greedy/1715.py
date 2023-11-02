import heapq
import sys

N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(sys.stdin.readline()))

result = 0
while len(hq) > 1:
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    union = first + second
    result += union
    heapq.heappush(hq, union)

print(result)
