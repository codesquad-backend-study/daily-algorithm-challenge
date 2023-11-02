import sys

N = int(sys.stdin.readline())
times = []
for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().split())))
times.sort(key=lambda x: (x[1], x[0]))

answer = 1
prev_end = times[0][1]
for start, end in times[1:]:
    if start >= prev_end:
        answer += 1
        prev_end = end
print(answer)
