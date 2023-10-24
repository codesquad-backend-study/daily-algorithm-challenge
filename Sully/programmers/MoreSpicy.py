import heapq
from typing import List


def solution(scoville: List[int], K: int):
    answer = 0
    heap = []

    for s in scoville:
        # 최소힙으로 가장 작은 값이 상단(heap[0])에 위치하도록 함
        heapq.heappush(heap, s)

    # 2개의 음식이 필요
    while heap[0] < K and len(heap) > 1:
        # 힙에 요소가 2개만 남았을 경우
        if len(heap) == 2:
            # 그 두 요소를 합하고, 합쳐진 값이 K보다 여전히 작다면 만족 X
            if heapq.heappop(heap) + heapq.heappop(heap) * 2 < K:
                return -1

            # if문에 걸리지 않는다면 이번 연산을 더해서 반환
            return answer + 1

        # 2개 이상의 요소가 있는 경우, 가장 작은 두 값을 똑같이 pop하고 다시 넣어줌
        new = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, new)

        # 연산 다 끝나고 answer를 1씩 증가
        answer += 1

    # while문이 종료되었다는 것은 힙의 모든 요소가 K 이상이라는 의미
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
