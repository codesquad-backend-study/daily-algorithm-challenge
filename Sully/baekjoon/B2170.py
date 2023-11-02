import sys
from typing import List


def solution(location_list: List[List[int]]) -> int:
    location_list.sort()

    # length = y - x
    length = location_list[0][1] - location_list[0][0]
    # target = y
    target = location_list[0][1]

    for i in range(1, len(location_list)):
        if location_list[i][0] < target < location_list[i][1] \
                or location_list[i][0] == target:
            # length += y값들 - target
            length += location_list[i][1] - target
            # target = y값들 (다시 업데이트)
            target = location_list[i][1]
            continue

        # 선이 끊어져 있다는 의미
        if location_list[i][0] > target:
            # length += y값들 - x값들
            length += location_list[i][1] - location_list[i][0]
            # target = y값들 (업데이트)
            target = location_list[i][1]

    return length


N = int(sys.stdin.readline().rstrip())
locations_list: List[List[int]] = []
for _ in range(N):
    locations_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(locations_list))
