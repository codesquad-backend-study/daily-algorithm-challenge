import collections

q = collections.deque()

for i in range(1, int(input()) + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())
