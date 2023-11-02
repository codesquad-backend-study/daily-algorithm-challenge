numbers = list(map(int, input().split()))

min_value = 101
min_idx = -1
max_value = 0
max_idx = -1

for idx, number in enumerate(numbers):
    if number <= min_value:
        min_value = number
        min_idx = idx

    if number >= max_value:
        max_value = number
        max_idx = idx

print(numbers[3 - min_idx - max_idx])


