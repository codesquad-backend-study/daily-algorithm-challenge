import collections
import sys
from typing import List


def solution(sang_cards: List[int], cards: List[int]) -> List[int]:
    answer = []

    card_map = collections.defaultdict(int)
    for c in sang_cards:
        card_map[c] = 1

    for c in cards:
        if c in card_map:
            answer.append(1)
            continue

        answer.append(0)

    return answer


N = int(input())  # 무쓸모
sang_cards = list(map(int, sys.stdin.readline().split()))
M = int(input())  # 무쓸모
cards = list(map(int, sys.stdin.readline().split()))

print(*solution(sang_cards, cards))
