import sys

result = {0: 'D', 1: 'C', 2: 'B', 3: 'A', 4: 'E'}

for _ in range(3):
    line = list(map(int, sys.stdin.readline().split()))
    print(result[line.count(1)])
