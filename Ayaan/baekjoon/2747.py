n = int(input())

first = 0
second = 1

for _ in range(1, n):
    temp = second
    second = first + second
    first = temp

print(second)