n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]

schedules.sort(key=lambda x: (x[1], x[0]))

idx = 0
cnt = 0
while idx < n:
    cnt += 1
    end_time = schedules[idx][1]

    idx += 1
    while idx < n and end_time > schedules[idx][0]:
        idx += 1

print(cnt)
