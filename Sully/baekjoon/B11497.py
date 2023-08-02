import sys
from typing import List


def solution(heights: List[int]) -> int:
    answer = 0

    # 첫번째 통나무랑 마지막 통나무랑 인접하다는 것을 기억해야 됨
    # 그럼 큰 것을 기준으로 해서 좌, 우로 작은 것들을 계속 배치해나간다면 최소가 됨

    heights.sort()

    for i in range(2, len(heights)):
        answer = max(answer, abs(heights[i] - heights[i - 2]))

    return answer


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    heights = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(heights))
