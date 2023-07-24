# 1927번 파일은 이미 있어서 링크만 첨부할게요!
# https://github.com/codesquad-backend-study/daily-algorithm-challenge/blob/main/Sully/baekjoon/B1927.py

import heapq
import sys
from typing import List


def solution(nums: List[int]) -> List[int]:
    answer = []

    # x가 0이라면 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거
    heap = []
    for num in nums:
        if num == 0:
            if heap:
                answer.append(-heapq.heappop(heap))
                continue

            # 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력
            answer.append(0)
            continue

        heapq.heappush(heap, -num)

    return answer


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))

print(*solution(array), sep='\n')
