import sys

n = int(input())

point = []
rectangle = [[0 for i in range(100)] for i in range(100)]

for i in range(n) :
    x, y = map(int,sys.stdin.readline().split())
    point.append([x, y])

for x, y in point :
    for w in range(x, x+10) :
        for h in range(y, y+10) :
            rectangle[w][h] = 1

answer = 0

for line in rectangle :
    answer += sum(line)

print(answer)
