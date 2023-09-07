import heapq
import sys
from typing import List


def solution(cards: List[int]) -> int:
    answer = 0

    heap = []
    for card in cards:
        heapq.heappush(heap, card)

    # heap의 길이가 1 이하가 되기 전까지만
    while len(heap) > 1:
        A = heapq.heappop(heap)
        B = heapq.heappop(heap)

        current_sum = A + B
        answer += current_sum

        # 최소힙으로 정렬
        heapq.heappush(heap, current_sum)

    return answer


N = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(N):
    cards.append(int(sys.stdin.readline().rstrip()))

print(solution(cards))
