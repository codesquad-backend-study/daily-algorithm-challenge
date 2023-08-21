import sys
from typing import List


def solution(A_list: List[int], B_list: List[int]) -> int:
    answer = 0

    A_list.sort()
    B_list.sort()

    # A 하나하나씩 돌아주면서 B_list랑 비교하는 로직
    for A in A_list:
        tmp_sum = -1
        lt, rt = 0, len(B_list) - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            # 즉, A보다 작은 수들 중에 -> 제일 큰 수의 index를 찾으면 됨
            if B_list[mid] < A:
                tmp_sum = mid
                lt = mid + 1
                continue

            rt = mid - 1

        answer += tmp_sum + 1

    return answer


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    A_list = list(map(int, sys.stdin.readline().rstrip().split()))
    B_list = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(A_list, B_list))
