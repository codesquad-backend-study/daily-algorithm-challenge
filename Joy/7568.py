import sys

n = int(sys.stdin.readline())

dungchi = []
result = [ 1 for i in range(n)]

for i in range(n) :
    weight, height = map(int, sys.stdin.readline().split())
    dungchi.append((weight, height))

for x in dungchi :
    rank = 1
    for y in dungchi :
        if x[0] < y[0] and x[1] < y[1] :
            rank += 1
    print(rank ,end=" ")
