# 숨바꼭질
import collections

subin, sister = map(int, input().split())
queue = collections.deque([(subin, 0)])
visited = set()

if subin == sister:
    print(0)
    exit()

while True:
    current_subin, second = queue.popleft()
    if current_subin == sister:
        print(second)
        break

    visited.add(current_subin)
    directions = [current_subin - 1, current_subin + 1, current_subin * 2]
    for d in directions:
        if 100000 >= d >= 0:
            if d not in visited:
                queue.append((d, second + 1))
