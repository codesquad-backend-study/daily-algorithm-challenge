N = int(input())
stack = [0]
push_number = 0
result = []
for _ in range(N):
    num = int(input())
    if num > stack[-1]:
        for _ in range(num - push_number):
            push_number += 1
            stack.append(push_number)
            result.append("+")
    elif num < stack[-1]:
        print("NO")
        exit()
    stack.pop()
    result.append("-")
print(*result, sep="\n")
