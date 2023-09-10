# A -> B
import collections
import sys

a, b = map(int, sys.stdin.readline().split())

queue = collections.deque([(a, 1)])

while queue:
    value, count = queue.popleft()
    if value == b:
        print(count)
        exit()
    if value * 2 <= b:
        queue.append((value * 2, count + 1))
    if value * 10 + 1 <= b:
        queue.append((value * 10 + 1, count + 1))

print(-1)
