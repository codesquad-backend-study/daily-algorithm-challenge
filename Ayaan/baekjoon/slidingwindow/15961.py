import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())
dishes = []
for _ in range(N):
    dishes.append(int(sys.stdin.readline()))

# 초밥의 가짓수
count_of_sushi = defaultdict(int)
# 쿠폰은 포함한 상태로 계산
count_of_sushi[c] += 1
# k개 먼저 추가
for i in range(k):
    count_of_sushi[dishes[i]] += 1

answer = 0
left = 0
right = k - 1

while left < N:
    answer = max(answer, len(count_of_sushi))

    # left 이동
    count_of_sushi[dishes[left]] -= 1
    if count_of_sushi[dishes[left]] == 0:
        del count_of_sushi[dishes[left]]
    left += 1

    # right 이동
    right += 1
    count_of_sushi[dishes[right % N]] += 1

print(answer)
