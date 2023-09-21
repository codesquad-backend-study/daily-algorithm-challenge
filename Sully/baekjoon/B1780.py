import sys
from typing import List


def solution(N: int, nums_list: List[List[int]]) -> List[int]:
    zero, minus, plus = 0, 0, 0

    def quad_tree(nums_list: List[List[int]], x: int, y: int, n: int):
        nonlocal zero, minus, plus

        first_num = nums_list[y][x]

        for j in range(y, y + n):
            for i in range(x, x + n):
                # 현재 위치 (i, j)의 number가 first_num과 같다면
                # 아무 작업도 하지 않고 다음 숫자로 넘어감
                if first_num == nums_list[j][i]:
                    continue

                # 반복문을 돌면서 first_num과 다른 숫자가 나오면
                # 해당 영역을 9개의 영역으로 나누고 재귀적으로 돎
                # n // 3만큼 크기가 줄어든 작은 영역으로 분할
                division = n // 3
                quad_tree(nums_list, x, y, division)
                quad_tree(nums_list, x, y + division, division)
                quad_tree(nums_list, x, y + division * 2, division)
                quad_tree(nums_list, x + division, y, division)
                quad_tree(nums_list, x + division, y + division, division)
                quad_tree(nums_list, x + division, y + division * 2, division)
                quad_tree(nums_list, x + division * 2, y, division)
                quad_tree(nums_list, x + division * 2, y + division, division)
                quad_tree(nums_list, x + division * 2, y + division * 2, division)

                return

        if first_num == 0:
            zero += 1
        elif first_num == -1:
            minus += 1
        elif first_num == 1:
            plus += 1

    quad_tree(nums_list, 0, 0, N)

    return [minus, zero, plus]


N = int(sys.stdin.readline().rstrip())
nums_list: List[List[int]] = []
for _ in range(N):
    nums_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(*solution(N, nums_list), sep='\n')
