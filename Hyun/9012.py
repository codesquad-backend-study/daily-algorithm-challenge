n = int(input())

for _ in range(n):
    s = input()
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(1)
        else:
            if not stack:
                stack.append(1)
                break
            else:
                stack.pop()

    print("NO" if stack else "YES")

