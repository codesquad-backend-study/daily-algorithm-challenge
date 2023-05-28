# 보물
# 0 < N <= 50
# B를 재배열하지 말고 B에 맞춰서 A를 재배열하기

import sys
import copy
from typing import List


def S(listA: List[int], listB: List[int]):  # 함수 S 정의
    return sum([numberA * numberB for numberA, numberB in zip(listA, listB)])


count = int(sys.stdin.readline())

listA = [int(numberA) for numberA in sys.stdin.readline().split()]
listB = [int(numberB) for numberB in sys.stdin.readline().split()]

listA.sort()
newA = [-1] * count  # 초기화
copyB = copy.deepcopy(listB)

for a_index in range(count):  # A 재배열하기
    max_in_B = max(copyB)
    b_index = copyB.index(max_in_B)
    newA[b_index] = listA[a_index]
    copyB[b_index] = -1  # -1로 초기화

print(S(newA, listB))
