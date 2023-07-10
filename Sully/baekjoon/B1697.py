import collections
import sys


def solution(n: int, k: int) -> int:
    max_n = 100000
    visited = [0] * (max_n + 1)

    dq = collections.deque()
    dq.append(n)  # 수빈이 출발

    while dq:
        X = dq.popleft()
        if X == k:
            return visited[X]

        tp = [X - 1, X + 1, 2 * X]
        for i in tp:
            if 0 <= i <= max_n and not visited[i]:
                visited[i] = visited[X] + 1
                dq.append(i)

    return 0


N, K = map(int, sys.stdin.readline().rstrip().split())
print(solution(N, K))
