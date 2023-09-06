import sys
from typing import List


def solution(students: List[List[str]]) -> List[str]:
    answer = []

    # [이름, 국어, 영어, 수학] 순서
    students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for i in range(len(students)):
        answer.append(students[i][0])

    return answer


N = int(input())
array = []
for _ in range(N):
    array.append(sys.stdin.readline().split())

print(*solution(array), sep='\n')
