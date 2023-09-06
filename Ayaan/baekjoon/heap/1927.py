import sys
import heapq

hq = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(hq, x)
    else:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
