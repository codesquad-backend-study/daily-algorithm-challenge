import sys
from typing import List


def solution(people_list: List[int]) -> int:
    answer = 0

    tmp = 0
    for person in sorted(people_list):
        # 임시 배열에 한 사람의 시간을 계속 저장해 주고
        tmp += person
        # 그 합한 시간을 계속 저장한다
        answer += tmp

    return answer


N = int(sys.stdin.readline().rstrip())
people_list = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(people_list))
