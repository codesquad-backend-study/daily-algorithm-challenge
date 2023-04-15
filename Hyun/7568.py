n = int(input())

people = [tuple(map(int, input().split())) for _ in range(n)]
# [(몸무게, 키), (몸무게, 키), ... ] 로 저장 (피아 전용 주석)

ranks = []

for i in range(n):
    fivot_weight, fivot_height = people[i]
    rank = 1

    for j in range(n):
        compare_weight, compare_height = people[j]

        if fivot_weight < compare_weight and fivot_height < compare_height:     # 나보다 덩치 큰 사람 있으면
            rank += 1                                                           # 랭크 증가

    ranks.append(rank)

print(*ranks)

