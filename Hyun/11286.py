import sys
from heapq import *

heap = []

for _ in range(int(input())):
    i = int(sys.stdin.readline())
    if i != 0:
        heappush(heap, (abs(i), i))

    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
