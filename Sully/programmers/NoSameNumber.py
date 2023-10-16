from typing import List


def solution(arr: List[int]):
    answer = [arr[0]]
    judge = set()

    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
