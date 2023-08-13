import heapq
import sys
from typing import List


# gems_list: [[무게, 가격], ...]
# max_weights: [가방에 담을 수 있는 최대 무게, ...]
# answer: 훔칠 수 있는 보석 가격의 "합의 최댓값"
def solution(gems_list: List[List[int]], max_weights: List[int]):
    answer = 0

    gems_list.sort()
    max_weights.sort()

    heap = []
    for weight in max_weights:
        # 보석이 존재한다면 -> 가방에 계속 담을 수 있다는 뜻
        while gems_list:
            current_weight = gems_list[0][0]
            current_price = gems_list[0][1]

            # 현재 가방에 들어갈 수 있는 weight의 보석이 있다면
            if current_weight <= weight:
                # 힙에 보석 정보 추가 후 (큰 가격, 작은 무게 순서로)
                heapq.heappush(heap, (-current_price, current_weight))
                # 추가한 보석은 제거
                heapq.heappop(gems_list)
                continue

            # if문을 통과하지 못했다면, 우선 순위 큐에 의해 이제 가장 가벼운 보석도 못 넣는다는 뜻
            break

        # 아직 보석이 남아있다면, 우선 순위 큐로 정련된 가장 큰 보석(index: 0, minus)을 출력
        # minus를 하는 이유는 오름차순으로 정렬 후 순회했기 때문
        # 즉, heap에 들어있는 보석은 모두 가방에 들어갈 수 있다는 뜻
        if heap:
            # 가장 가치가 높은 보석의 가격 힙에서 꺼내서 누적
            answer += -heapq.heappop(heap)[0]

    return answer


N, K = map(int, sys.stdin.readline().rstrip().split())

gems_list: List[List[int]] = []
for _ in range(N):
    gems_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_weights: List[int] = []
for _ in range(K):
    max_weights.append(int(sys.stdin.readline().rstrip()))

print(solution(gems_list, max_weights))
