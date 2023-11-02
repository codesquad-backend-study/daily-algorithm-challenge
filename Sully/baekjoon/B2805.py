import sys
from typing import List


# M: 집으로 가져가려고 하는 "나무의 길이"
# heights: 나무의 높이 >= target
def solution(M: int, heights: List[int]) -> int:
    heights.sort()

    # sorting -> [4, 26, 40, 42, 46]
    # M -> 20
    # cutting -> [4 - answer, 26 - answer, 40 - answer, 42 - answer, 46 - answer]
    # cutting에서의 answer의 합의 최댓값 -> M(20)
    answer = 0
    lt, rt = 0, heights[-1]
    while lt <= rt:
        mid = (lt + rt) // 2

        cutting = []
        for height in heights:
            if height - mid > 0:
                cutting.append(height - mid)

        if sum(cutting) >= M:
            answer = mid
            lt = mid + 1
            continue

        rt = mid - 1

    return answer


N, M = map(int, sys.stdin.readline().rstrip().split())
heights = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(M, heights))
