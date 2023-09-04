import collections

days_len, window_size = map(int, input().split())
days = list(map(int, input().split()))

queue = collections.deque(days[:window_size])
max_val = prev_val = sum(days[:window_size])

visitor_dict = collections.defaultdict(int)
visitor_dict[max_val] += 1

for day in days[window_size:]:
    out = queue.popleft()
    prev_val -= out
    prev_val += day
    queue.append(day)

    visitor_dict[prev_val] += 1
    max_val = max(max_val, prev_val)

if max_val == 0:
    print("SAD")
    exit(0)

print(max_val)
print(visitor_dict[max_val])
