import sys


def solution(s: str) -> int:
    answer = 0
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
            continue

        # case: s[i] == ')'
        if s[i - 1] == '(':  # ')'가 나왔는데 그 전이 '('인 경우 stack의 개수로 카운팅
            stack.pop()
            answer += len(stack)
        else:  # ')'는 막대기 추가
            stack.pop()
            answer += 1

    return answer


print(solution(sys.stdin.readline().rstrip()))
