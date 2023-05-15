import sys

maximum = 0
# 계속 틀려서 뭐가 틀린지 몰랐는데 모든 입력이 0이면 index가 비어서 나온다. 초기화 안시켜줘서 계속 틀렸다
index = [1, 1]
for row in range(9):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    if maximum < max(numbers):
        maximum = max(numbers)
        index = [row + 1, numbers.index(maximum) + 1]
print(maximum)
print(*index)
