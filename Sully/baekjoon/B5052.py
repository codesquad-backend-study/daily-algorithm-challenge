import sys
from typing import List


def solution(numbers: List[str]) -> str:
    numbers.sort()

    # (i + 1)까지니까 len(numbers) 바로 전까지 반복
    for i in range(len(numbers) - 1):
        # 그 길이의 문자열이 겹친다면 연속하지 않는다는 뜻이므로 바로 "NO" 리턴
        if numbers[i] == numbers[i + 1][0: len(numbers[i])]:
            return "NO"

    return "YES"


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    numbers = []
    for _ in range(n):
        numbers.append(sys.stdin.readline().rstrip())

    print(solution(numbers))
