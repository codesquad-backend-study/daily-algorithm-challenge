# 점프
import sys

size = int(sys.stdin.readline())
game = [[*map(int, sys.stdin.readline().split())] for _ in range(size)]

accumulated_count = [[0] * size for _ in range(size)]
accumulated_count[0][0] = 1

for row in range(size):
    for column in range(size):
        jump = game[row][column]
        current = accumulated_count[row][column]
        if current != 0 and jump != 0:
            if row + jump < size:
                accumulated_count[row + jump][column] += current
            if column + jump < size:
                accumulated_count[row][column + jump] += current

print(accumulated_count[-1][-1])
