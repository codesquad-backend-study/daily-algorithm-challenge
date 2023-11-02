import sys
import heapq

course = []
# 정렬
for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(course, (start, end))

rooms = [heapq.heappop(course)[1]]
while course:
    start, end = heapq.heappop(course)
    if start < rooms[0]:
        heapq.heappush(rooms, end)
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
print(len(rooms))
