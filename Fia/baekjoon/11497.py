# 통나무 건너뛰기
import collections
import sys


def tongtong():
    count = int(sys.stdin.readline())
    heights = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    sorted_logs = collections.deque()
    for i in range(count):
        if i % 2 != 0:
            sorted_logs.appendleft(heights[i])
        else:
            sorted_logs.append(heights[i])

    difficulty = sorted_logs[-1] - sorted_logs[0]
    for index in range(len(sorted_logs) - 1):
        difficulty = max(difficulty, abs(sorted_logs[index] - sorted_logs[index + 1]))
    print(difficulty)


T = int(sys.stdin.readline())
for _ in range(T):
    tongtong()
