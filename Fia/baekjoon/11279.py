# 최대 힙
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    number = int(sys.stdin.readline())

    if number > 0:
        heapq.heappush(heap, -number)
        continue

    print(-heapq.heappop(heap) if heap else 0)
