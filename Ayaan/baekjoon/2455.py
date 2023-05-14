count = 0
max = 0
for _ in range(4):
    minus, plus = map(int, input().split())
    count = count - minus + plus
    if max < count:
        max = count
print(max)