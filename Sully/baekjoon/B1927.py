import heapq
import sys
from typing import List


def solution(nums: List[int]) -> List[int]:
    answer = []

    # x가 0이라면 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거
    h = []
    for x in nums:
        if x == 0:
            if h:
                answer.append(heapq.heappop(h))
                continue

            # 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력
            answer.append(0)
            continue

        heapq.heappush(h, x)

    return answer


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))

print(*solution(array), sep='\n')
