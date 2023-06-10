import sys
import re

customInput = sys.stdin.readline

while True:
    text = customInput().rstrip()
    if text == ".":
        break
    brackets = re.findall(r'[\(\)\[\]]', text)
    stack = []
    for bracket in brackets:
        if not stack:
            stack.append(bracket)
            continue
        if (stack[-1] == '(' and bracket == ')') or (stack[-1] == '[' and bracket == ']'):
            stack.pop()
        else:
            stack.append(bracket)
    print('no' if stack else 'yes')
