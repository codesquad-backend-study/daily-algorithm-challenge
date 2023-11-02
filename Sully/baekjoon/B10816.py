import collections
import sys
from typing import List


def solution(sang_cards: List[int], cards: List[int]) -> List[int]:
    answer = []

    sang_card_map = collections.defaultdict(int)
    for card in sang_cards:
        sang_card_map[card] += 1

    for card in cards:
        answer.append(sang_card_map[card])

    return answer


N = int(input())  # 무쓸모
array1 = list(map(int, sys.stdin.readline().split()))
M = int(input())  # 무쓸모
array2 = list(map(int, sys.stdin.readline().split()))

print(*solution(array1, array2))
