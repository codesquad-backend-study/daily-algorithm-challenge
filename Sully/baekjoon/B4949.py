import sys
from typing import List


def solution(strs: List[str]) -> List[str]:
    answer = []

    for st in strs:  # 이건 시간 복잡도로 안 침
        stack = []
        for s in st:
            if s == '(' or s == '[':
                stack.append(s)
                continue

            if s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue

                stack.append(s)

            if s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                    continue

                stack.append(s)

        if stack:
            answer.append('no')
        else:
            answer.append('yes')

    return answer


array = []
while True:
    inp = sys.stdin.readline().rstrip()
    if inp == '.':
        break

    array.append(inp)

print(*solution(array), sep='\n')
