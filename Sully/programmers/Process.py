import collections
from typing import List


def solution(priorities: List[int], location: int) -> int:
    answer = 0

    dq = collections.deque((index, process) for index, process in enumerate(priorities))
    while dq:
        current = dq.popleft()

        higher_priority_exists = False
        for q in dq:
            if current[1] < q[1]:
                higher_priority_exists = True
                continue

        if higher_priority_exists:
            dq.append(current)
            continue

        answer += 1
        if current[0] == location:
            break

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
