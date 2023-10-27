from typing import List


def solution(array: List[int], commands: List[List[int]]) -> List[int]:
    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        cut = array[i - 1:j]
        cut.sort()
        answer.append(cut[k - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
