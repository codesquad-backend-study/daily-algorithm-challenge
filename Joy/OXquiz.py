import sys
# 풀이 1. 52ms
n = int(input())

for i in range(n):
    lst = input()
    score = 0
    total = 0
    for ox in lst :
        if ox == 'X' :
            score = 0
            continue
        score += 1
        total += score
    print(total)
    total = 0

# 풀이 2. 44ms
n = int(input())
result = []

for i in range(n):
    result.extend(sys.stdin.readline().split())

result = [ s.replace('X',' ') for s in result]

for ox in result:
    accum = 0
    score = 0
    for s in ox:
        if s == " ":
            accum = 0
            continue
        accum += 1
        score += accum
    print(score)
