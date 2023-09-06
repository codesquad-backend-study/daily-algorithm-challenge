# N번째 큰 수
import heapq
import sys

line_count = int(sys.stdin.readline())

top_numbers = [*map(int, sys.stdin.readline().split())]

for _ in range(line_count - 1):
    numbers = [*map(int, sys.stdin.readline().split())]
    for number in numbers:
        heapq.heappushpop(top_numbers, number)

print(heapq.heappop(top_numbers))
