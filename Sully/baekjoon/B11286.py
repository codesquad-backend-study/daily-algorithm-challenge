import heapq
import sys
from typing import List


def solution(nums: List[int]) -> List[int]:
    answer = []

    h = []
    for x in nums:
        # x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
        if x == 0:
            if h:
                # [1] -> (절댓값, 원래값)에서 (원래값)
                answer.append(heapq.heappop(h)[1])
                continue

            # 절댓값이 가장 작은 값을 출력하라고 한 경우
            answer.append(0)
            continue

        # (절댓값, 원래값) -> (절대값) 기준으로 정렬
        heapq.heappush(h, (abs(x), x))

    return answer


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))

print(*solution(array), sep='\n')
