import sys
from typing import List


# 계속 A[i] * B[i]의 최솟값을 구하는 건지 알고 시간 낭비함
# 그러면 당연히 최솟값이 0이 될 텐데.. 라면서
def solution(A: List[int], B: List[int]) -> int:
    S = 0

    # A의 수만 재배열, B는 재배열하면 안 됨
    # 오름차순으로 해주는 이유는 결국 두 배열의 곱의 최솟값은 [최소 * 최대]이기 때문
    A.sort()

    # 이제 B의 가장 큰 값부터 A 배열의 순서대로 곱해주면 되는데
    # 핵심은 "B는 재배열하면 안 된다는 거"
    # 그럼 그냥 max 구하고 그 값을 지워주면 되지 (index 굳이 구할 필요 없음)

    for a in A:
        tmp_max = max(B)
        B.remove(tmp_max)
        S += (a * tmp_max)

    return S


N = int(input())  # 무쓸모
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

print(solution(A, B))
