import sys


def solution(K: str) -> int:
    answer = 0

    for k in K:
        if k == '1':
            answer += 1

    return answer


N = int(sys.stdin.readline().rstrip())
K = sys.stdin.readline().rstrip()

print(solution(K))
