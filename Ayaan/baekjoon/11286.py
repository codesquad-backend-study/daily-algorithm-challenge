import sys
import heapq

heap = []
for _ in range(int(input())):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
