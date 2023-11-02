n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]

schedules.sort(key=lambda x: (x[1], x[0]))

cnt = 0
prev_end = 0

for start, end in schedules:
    if start >= prev_end:
        prev_end = end
        cnt += 1

print(cnt)
