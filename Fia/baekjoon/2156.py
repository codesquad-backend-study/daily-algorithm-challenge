# 포도주 시식
import sys

count = int(sys.stdin.readline())
glasses = [int(sys.stdin.readline()) for _ in range(count)]

if count == 1 or count == 2:
    print(sum(glasses))
    exit()

accumulated_wine = [[0] * 2 for _ in range(count)]

accumulated_wine[0][0] = glasses[0]  # 순서 1 : 마신 경우
accumulated_wine[0][1] = 0  # 순서 1 : 마시지 않은 경우

accumulated_wine[1][0] = glasses[0] + glasses[1]  # 순서 2 : 마신 경우
accumulated_wine[1][1] = glasses[0]  # 순서 2 : 마시지 않은 경우

for index in range(2, count):
    # 순서 index : 마신 경우
    # 조건 : 1. 전에 마시지 않은 값  2. 전전에 마신 값  3. 전전에 마시지 않았으면서 전에 마신 값
    accumulated_wine[index][0] = max(accumulated_wine[index - 1][1], accumulated_wine[index - 2][0], accumulated_wine[index - 2][1] + glasses[index - 1]) + glasses[index]
    # 순서 index : 마시지 않은 경우
    # 조건 : 전에 마시지 않은 값과 전에 마신 값 중 큰 값
    accumulated_wine[index][1] = max(accumulated_wine[index - 1])

print(max(accumulated_wine[-1]))


