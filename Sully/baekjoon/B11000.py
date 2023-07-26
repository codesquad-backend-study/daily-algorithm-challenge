import heapq
import sys
from typing import List


def solution(classes: List[List[int]]) -> int:
    # 시작 시간(S)를 기준으로 오름차순 정렬
    # 왜냐하면 시작 시간을 기준으로 정렬해야 최솟값을 찾을 수 있기 때문에 (직접 해봐야 됨)
    classes.sort(key=lambda x: x[0])

    # 끝나는 시간(T)이 빠른 수업이라는 점을 알아야
    # 아직 강의실에 "배치되지 않은" 수업들의 시작 시간을 끝나는 시간과 비교하여
    # 같은 강의실에서 수업을 연달아 듣을 수 있도록 함
    heap = []
    heapq.heappush(heap, classes[0][1])

    for i in range(1, len(classes)):
        # heap의 끝나는 시간, classes의 시작 시간 비교
        # 이 조건문(끝 <= 시)은 같은 강의실에 배정할 수 있다는 뜻
        # 조건에 해당하지 않는다면 다른 강의실을 배정해야 한다는 뜻
        if heap[0] <= classes[i][0]:
            heapq.heappop(heap)

        # class의 끝나는 시간을 다시 heap에 넣어줌
        heapq.heappush(heap, classes[i][1])

    # heap의 개수가 곧 강의실의 개수
    return len(heap)


N = int(sys.stdin.readline().rstrip())
classes = []
for _ in range(N):
    classes.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(classes))
