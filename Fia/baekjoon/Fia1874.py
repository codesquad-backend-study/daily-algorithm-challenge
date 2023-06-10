# 스택 수열

count = int(input())
sequence = [int(input()) for _ in range(count)]

stack = [1]
result = ["+"]

number = 2
for target in sequence:
    if stack and stack[-1] > target:
        print("NO")
        exit()
    while number <= target:
        stack.append(number)
        result.append("+")
        number += 1
    stack.pop()
    result.append("-")

print(*result, sep='\n')
