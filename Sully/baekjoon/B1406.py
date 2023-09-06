import sys
from typing import List


def solution(init: str, commands: List[str]) -> List[str]:
    left = list(init)
    right = []

    for command in commands:
        if command[0] == 'L' and left:
            right.append(left.pop())
            continue

        if command[0] == 'D' and right:
            left.append(right.pop())
            continue

        if command[0] == 'B' and left:
            left.pop()
            continue

        if command[0] == 'P':
            left.append(command[-1])

    left += reversed(right)
    return left


s = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline().rstrip())
array = []
for _ in range(M):
    array.append(sys.stdin.readline().rstrip())

print(*solution(s, array), sep='')
