import sys
from typing import List


def solution(N: int, length: List[int], price: List[int]) -> int:
    answer = 0

    current_price = price[0]
    for i in range(len(length)):
        # 다음 정류장까지의 가격 계산 후 계속 저장
        answer += length[i] * current_price

        # 다음 정류장에서의 가격 < 현재 리터 가격 -> 싼 가격으로 업뎅티ㅡ
        current_price = min(current_price, price[i + 1])

    return answer


N = int(sys.stdin.readline().rstrip())
cnt = list(map(int, sys.stdin.readline().rstrip().split()))
length = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(N, cnt, length))
