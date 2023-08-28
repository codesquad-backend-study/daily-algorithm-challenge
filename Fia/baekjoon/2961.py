# 도영이가 만든 맛있는 음식
from itertools import combinations

n = int(input())

ingredients = [[*map(int, input().split())] for _ in range(n)]

minimum_gap = 1000000001

for ingredient in (combinations(ingredients, i + 1) for i in range(n)):
    for taste in ingredient:
        sour, bitter = 1, 0
        for s, b in taste:
            sour *= s
            bitter += b

        minimum_gap = min(minimum_gap, abs(sour - bitter))

print(minimum_gap)

# 모든 조합을 찾아서 최소 차이 값을 구해야 하는 문제

# 비트 마스킹으로 풀기
'''
재료의 선택 여부를 비트 마스킹으로 표시할 수 있다.
a, b, c 총 3개의 재료가 있을 때, 다음과 같이 표시할 수 있다.
a만 사용하는 경우: 001
b만 사용하는 경우: 010
c만 사용하는 경우: 100
ab를 사용하는 경우: 011

이때 1을 3번 <<(left shift) 하면 1000이 되므로, 111(재료 3개)까지의 경우의 수만큼 반복문을 사용할 수 있다.
& 연산을 사용해서 각 재료를 사용했다면 값을 계산하면 된다.
'''
