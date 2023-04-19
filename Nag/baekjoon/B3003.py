standard = [1, 1, 2, 2, 2, 8]
input = list(map(int, input().split()))
answer = []
for index in range(len(input)):
    answer.append(standard[index] - input[index])
print(*answer)
