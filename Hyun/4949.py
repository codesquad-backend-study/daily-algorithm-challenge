import re

table = {")": "(", "]": "["}

s = input()

while s != '.':
    stack = []
    s = re.sub(r'[^\[()\]]', '', s)

    for ch in s:
        if ch in table:
            if stack and table[ch] == stack[-1]:
                stack.pop()
            else:
                stack.append("x")
                break
        else:
            stack.append(ch)

    print('yes') if not stack else print('no')

    s = input()
