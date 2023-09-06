# 신입 사원

import sys

test = int(sys.stdin.readline().strip())

for _ in range(test):
    people = int(sys.stdin.readline().strip())
    rank = [list(map(int, sys.stdin.readline().split())) for _ in range(people)]
    rank.sort(key=lambda x: (x[0]))

    count = 1
    highest = rank[0][1]
    for point in rank[1::]:
        if point[1] < highest:
            highest = point[1]
            count += 1

    print(count)

