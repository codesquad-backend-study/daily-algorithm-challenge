import heapq
import sys

heap = []

n = int(input())
for _ in range(n):

    given = int(sys.stdin.readline())

    if given == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, given)
