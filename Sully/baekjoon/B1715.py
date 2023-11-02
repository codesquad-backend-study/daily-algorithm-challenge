import heapq
import sys
from typing import List


def solution(cards: List[int]) -> int:
    answer = 0

    heap = []
    for card in cards:
        heapq.heappush(heap, card)

    # heap의 길이가 1 이하가 됐을 때부터는 계산할 가치가 없음
    # 최소 힙이니 루트 노드가 작은 값부터 정렬되는 것
    while len(heap) > 1:
        A = heapq.heappop(heap)
        B = heapq.heappop(heap)

        _sum = A + B
        answer += _sum

        heapq.heappush(heap, _sum)

    return answer


N = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(N):
    cards.append(int(sys.stdin.readline().rstrip()))

print(solution(cards))
