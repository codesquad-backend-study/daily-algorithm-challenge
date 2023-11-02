import sys
from typing import List


def solution(N: int, orders_list: List[List[int]]) -> int:
    trains = [[0] * 20 for _ in range(N)]

    for i in range(len(orders_list)):
        first_order = orders_list[i][0]
        second_order = orders_list[i][1]
        third_order = 0
        if len(orders_list[i]) == 3:
            third_order = orders_list[i][2]

        # 사람이 없는 곳은 0
        # 사람이 있는 곳은 1

        if first_order == 1:
            trains[second_order - 1][third_order - 1] = 1
            continue

        if first_order == 2:
            trains[second_order - 1][third_order - 1] = 0
            continue

        if first_order == 3:
            trains[second_order - 1].insert(0, 0)
            trains[second_order - 1].pop()
            trains[second_order - 1][0] = 0
            continue

        trains[second_order - 1].pop(0)
        trains[second_order - 1].append(0)
        trains[second_order - 1][-1] = 0

    return len(set(map(tuple, trains)))


N, M = map(int, sys.stdin.readline().rstrip().split())
orders_list: List[List[int]] = []
for _ in range(M):
    orders_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, orders_list))
