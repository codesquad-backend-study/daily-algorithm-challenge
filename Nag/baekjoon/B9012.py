answer = []
cnt = int(input())
for _ in range(cnt):
    stack = []
    ps = list(input())
    for element in ps:
        if not stack:
            stack.append(element)
            continue
        if stack[-1] == "(" and element == ")":
            stack.pop()
        else:
            stack.append(element)
    answer.append("YES" if not stack else "NO")
for result in answer:
    print(result)
