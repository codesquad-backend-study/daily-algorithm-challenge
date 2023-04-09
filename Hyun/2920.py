numbers = list(map(int, input().split()))

flag = "ascending" if numbers[0] == 1 and numbers[-1] == 8 else "descending"

for i in range(7):
    if abs(numbers[i] - numbers[i+1]) > 1:
        flag = "mixed"

print(flag)

