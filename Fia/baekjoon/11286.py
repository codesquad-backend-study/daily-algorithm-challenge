# 절댓값 힙

from heapq import heappop, heappush
import sys

N = int(input())

heap = []

for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(number), number))
