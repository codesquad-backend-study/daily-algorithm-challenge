import collections

MAX = 100001

soobin, younger = map(int, input().split())

graph = [-1] * MAX

queue = collections.deque([(soobin, 0)])

while queue:
    loc, time, = queue.popleft()
    graph[loc] = time

    if loc == younger:
        break

    if 2 * loc < MAX and graph[2 * loc] == -1:
        queue.append((2 * loc, time + 1))

    if loc - 1 >= 0 and graph[loc - 1] == -1:
        queue.append((loc - 1, time + 1))

    if loc + 1 < MAX and graph[loc + 1] == -1:
        queue.append((loc + 1, time + 1))

print(graph[younger])
