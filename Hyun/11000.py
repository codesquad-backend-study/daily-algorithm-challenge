import heapq

n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]
schedules.sort()

rooms = []

for schedule in schedules:
    if rooms and rooms[0] <= schedule[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, schedule[1])
    else:
        heapq.heappush(rooms, schedule[1])

print(len(rooms))
