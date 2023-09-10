import sys


def solution(s: str) -> int:
    answer = 0
    minus_s = s.split('-')

    for m in minus_s[0].split('+'):
        answer += int(m)

    for m in minus_s[1:]:
        for p in m.split('+'):
            answer -= int(p)

    return answer


s = sys.stdin.readline().rstrip()
print(solution(s))
