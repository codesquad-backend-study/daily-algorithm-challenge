cnt = int(input())
stack = []
for _ in range(cnt):
    number = int(input())
    if number == 0:
        stack.pop()
        continue
    stack.append(number)
print(sum(stack))
