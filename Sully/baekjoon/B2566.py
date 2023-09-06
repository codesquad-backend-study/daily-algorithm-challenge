from typing import List


def solution(matrix: List):
    # maximum = [0, 0, 0]
    # cur_maximum = [0, 0, 0]
    #
    # for i in range(9):
    #     cur = matrix[i]  # 1차원
    #     cur_maximum = (max(cur), cur.index(cur_maximum[0]), i)
    #     maximum = (max(cur_maximum[0], maximum[0]), (cur.index(maximum[0]), i))

    maximum = []
    for i in range(9):
        cur_maximum = max(matrix[i])
        maximum.append((cur_maximum, matrix[i].index(cur_maximum), i))

    check_max = (0, 0, 0)
    for i in range(9):
        if maximum[i][0] > check_max[0]:
            check_max = maximum[i]

    print(check_max[0])
    print(check_max[2] + 1, check_max[1] + 1, )


matrix = []
for _ in range(9):
    matrix.append(list(map(int, input().split())))

print(solution(matrix))
