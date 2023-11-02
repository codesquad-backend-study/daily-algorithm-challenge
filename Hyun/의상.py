import collections


def solution(clothes):
    closet = collections.defaultdict(int)

    for cloth, kind in clothes:
        closet[kind] += 1

    ans = 1
    for count in closet.values():
        ans *= (count + 1)

    return ans - 1
