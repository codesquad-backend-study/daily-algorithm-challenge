from typing import List


def solution(N: int, patterns: List) -> str:
    answer = ''
    q = False

    length = len(patterns[0])
    for i in range(length):
        s = patterns[0][i]
        for j in range(N):
            if s != patterns[j][i]:
                q = True
                break

        if q:
            answer += '?'
        else:
            answer += s

        q = False

    return answer


N = int(input())
patterns = []
for _ in range(N):
    patterns.append(input())

print(solution(N, patterns))
