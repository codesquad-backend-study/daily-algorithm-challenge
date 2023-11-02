import collections
from typing import List


def solution(clothes: List[List[str]]) -> int:
    # answer에 곱해줘야 하니 1로 설정
    answer = 1
    type_name_map = collections.defaultdict(int)

    for c in clothes:
        current_type = c[1]
        type_name_map[current_type] += 1

    # 하나만 입는 경우
    ONLY_ONE = 1
    for current_name in type_name_map.values():
        # 경우 조합 -> 전부 곱하면 나옴
        answer *= current_name + ONLY_ONE

    # 처음에 answer를 1로 설정해 주었으니 1 빼주기
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
