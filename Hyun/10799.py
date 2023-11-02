given = input().replace("()", "*")

stack = []
count = 0
for ch in given:
    if ch == "(":
        stack.append(1)
    elif ch == "*":
        count += len(stack)
    else:
        count += 1
        stack.pop()
print(count)
