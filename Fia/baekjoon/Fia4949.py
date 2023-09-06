# 균형잡힌 세상

sentence = input()
while sentence != ".":
    stack = []
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif char == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif char == ')' or char == ']':
            stack.append(char)
    print("yes" if not stack else "no")
    sentence = input()
