# 킹: 1, 퀸: 1, 룩: 2, 비숍:2, 나이트: 2, 폰: 8

white_chess = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(len(white_chess)):
    answer.append(chess[i] - white_chess[i])

print(' '.join(map(str,answer)))