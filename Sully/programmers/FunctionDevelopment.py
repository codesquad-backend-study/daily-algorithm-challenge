import collections
import math
from typing import List


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    MAX = 100
    answer = []

    judge = [math.ceil((MAX - progresses[0]) / speeds[0])]
    for i in range(1, len(progresses)):
        remain = MAX - progresses[i]
        current_ceil = math.ceil(remain / speeds[i])
        if judge[-1] < current_ceil:
            judge.append(current_ceil)
            continue

        judge.append(judge[-1])

    # 카운터 사용하면 편할 거 같긴 한데 그냥 직접 하자
    tmp_dict = collections.defaultdict(int)
    for num in judge:
        tmp_dict[num] += 1

    for v in tmp_dict.values():
        answer.append(v)

    return answer


# [7, 70, 45]
print(solution([93, 30, 55], [1, 30, 5]))
# [5, 10, 1, 1, 20, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
