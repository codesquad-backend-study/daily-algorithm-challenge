# 회의실 배정
import sys

count = int(sys.stdin.readline())
meetings = [[*map(int, sys.stdin.readline().split())] for _ in range(count)]

meetings.sort()
last_end = meetings[0][1]
answer = 1

for meeting in meetings[1:]:
    start, end = meeting

    if end < last_end:
        last_end = end
    elif start >= last_end:
        answer += 1
        last_end = end

print(answer)
