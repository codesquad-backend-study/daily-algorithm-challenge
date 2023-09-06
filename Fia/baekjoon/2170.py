# 선 긋기
import sys

N = int(sys.stdin.readline())
lines = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])

total_length = 0
start, end = lines[0]

for line_start, line_end in lines[1:]:

    if line_start <= end:
        end = max(end, line_end)
    else:
        total_length += end - start
        start = line_start
        end = line_end

total_length += end - start

print(total_length)
