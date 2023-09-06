times = []
for _ in range(int(input())):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = times[0][1]
for i in range(1, len(times)):
    if times[i][0] >= end_time:
        count += 1
        end_time = times[i][1]

print(count)
