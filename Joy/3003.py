import sys

piece = [ 1, 1, 2, 2, 2, 8 ]
white = list(map(int, sys.stdin.readline().split()))
result = [ piece[i]-white[i] for i in range(6) ]

for i in result :
    print(i, end=" ")