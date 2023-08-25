import sys
from typing import List


def solution(N: int, nums_list: List[List[int]]) -> List[int]:
    answer = [0] * 1001

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            # and 연산을 실패하여 나타난 것이 -> nums_list
            # 반복문을 돌아주면서 모든 값을 or 연산
            answer[i] |= nums_list[i][j]

    return answer[:N]


nums_list: List[List[int]] = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    nums_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(*solution(N, nums_list))
