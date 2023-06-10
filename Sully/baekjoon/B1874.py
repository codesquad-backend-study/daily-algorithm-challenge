import sys
from typing import List


def solution(nums: List[int]) -> List[str]:
    answer = []
    stack = []

    cur = 1
    for num in nums:
        while cur <= num:
            stack.append(cur)
            cur += 1
            answer.append('+')

        if stack[-1] != num:
            return ['NO']

        stack.pop()
        answer.append('-')

    return answer


n = int(input())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline().strip()))

print(*solution(array), sep='\n')
