import sys
import heapq

hq = []
for _ in range(int(sys.stdin.readline())):
    heapq.heappush(hq, int(sys.stdin.readline()))

answer = 0
while len(hq) > 1:
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    plus = first + second
    answer += plus
    heapq.heappush(hq, plus)

print(answer)
