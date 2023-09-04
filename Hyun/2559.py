import collections

n, window_size = map(int, input().split())
temp = list(map(int, input().split()))

max_val = prev_val = sum(temp[:window_size])
queue = collections.deque(temp[:window_size])

for each in temp[window_size:]:
    out = queue.popleft()
    queue.append(each)

    prev_val -= out
    prev_val += each

    max_val = max(max_val, prev_val)

print(max_val)
