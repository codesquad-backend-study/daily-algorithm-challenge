import collections
import sys
from typing import List


def solution(n: int, nums: List[int]) -> int:
    answer = 0
    # 1부터 n까지의 deque 초기화
    circular_queue = collections.deque(i for i in range(1, n + 1))

    for num in nums:
        while True:
            # 첫번째와 현재의 넘버가 같으면 다음 넘버로
            if circular_queue[0] == num:
                circular_queue.popleft()
                break

            if circular_queue.index(num) > len(circular_queue) // 2:
                circular_queue.appendleft(circular_queue.pop())
                answer += 1
                continue

            circular_queue.append(circular_queue.popleft())
            answer += 1

    return answer


N, M = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(N, array))
