N = int(input())
weights = list(map(int, input().split()))
weights.sort()

possible_range = [0, 0]
for weight in weights:
    plus_range = [possible_range[0] + weight, possible_range[1] + weight]
    if possible_range[1] + 1 < plus_range[0]:
        break
    possible_range[1] = plus_range[1]
print(possible_range[1] + 1)
