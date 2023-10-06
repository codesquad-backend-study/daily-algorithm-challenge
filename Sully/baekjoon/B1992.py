import sys
from typing import List


def solution(N: int, sizes_list: List[List[int]]) -> str:
    answer = ''

    def quad_tree(x: int, y: int, n: int):
        nonlocal answer

        first_size = sizes_list[y][x]

        for j in range(y, y + n):
            for i in range(x, x + n):
                if first_size == sizes_list[j][i]:
                    continue

                division = n // 2
                answer += '('
                quad_tree(x, y, division)
                quad_tree(x + division, y, division)
                quad_tree(x, y + division, division)
                quad_tree(x + division, y + division, division)
                answer += ')'

                return

        if first_size == 1:
            answer += '1'
        elif first_size == 0:
            answer += '0'

    quad_tree(0, 0, N)

    return answer


N = int(sys.stdin.readline().rstrip())
sizes_list = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
print(solution(N, sizes_list))
