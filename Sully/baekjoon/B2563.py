"""
N = int(input())
# 기본 300으로 두고 겹치는 부분만 빼면 돼
area = 300
s = [[] for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    # s -> [제자리, 오른쪽, 위, 대각선] 순서
    s[i] = [(x, y), (x + 1, y), (x, y + 1), (x + 10, y + 10)]

# 이제 x좌표나 y좌표가 같은 게 존재하면 빼주고 가로, 세로 곱해주자
for i in range(len(s)):
    # 각 튜플의 x와 y좌표 비교해주려곤 하는데 불가능할 듯
    if s[i][0]

print(area)

# 때려쳐 이건 평생 해도 안 되는 로직
"""
black_area = 0
N = int(input())
area = [[False] * 100 for i in range(100)]

for i in range(N):
    x, y = map(int, input().split())

    for j in range(x, x + 10):
        for k in range(y, y + 10):
            area[j][k] = True

for a in area:
    for w in a:
        if w is True:
            black_area += 1

print(black_area)
