import collections


def solution(clothes):
    dict = collections.defaultdict(int)
    for element in clothes:
        dict[element[1]] += 1

    answer = 1
    for cnt in dict.values():
        answer *= (cnt + 1)
        
    return answer - 1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
