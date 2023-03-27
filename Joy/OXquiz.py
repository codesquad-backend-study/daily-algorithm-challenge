import sys

n = int(input())

for i in range(n):
    lst = list(input())
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
