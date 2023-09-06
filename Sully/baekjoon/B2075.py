import heapq
import sys
from typing import List


def solution(N: int, nums_list: List[List[int]]) -> int:
    # 최초 힙 생성 (첫번째 리스트 객체의 원소)
    heap = []
    for num in nums_list[0]:
        heapq.heappush(heap, num)

    # 각 원소를 탐색
    for i in range(1, N):
        current_nums = nums_list[i]
        for current_num in current_nums:
            # 현재 힙의 최솟값(index: 0)보다 현재값이 더 크다면
            if heap[0] < current_num:
                # 힙에 현재값 추가
                heapq.heappush(heap, current_num)
                # 힙의 최솟값 제거 -> 최대 N개의 원소만 유지
                heapq.heappop(heap)

    return heap[0]


N = int(sys.stdin.readline().rstrip())
nums_list: List[List[int]] = []
for _ in range(N):
    nums_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, nums_list))
