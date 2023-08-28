from itertools import combinations

N = int(input())
sources = [list(map(int, input().split())) for _ in range(N)]

answer = 1000000000
for i in range(1, N + 1):
    # N개 중 i개 조합
    combi = combinations(sources, i)
    for source in combi:
        sour = 1
        bitter = 0
        for s, b in source:
            sour *= s
            bitter += b
        answer = min(answer, abs(sour - bitter))
print(answer)
