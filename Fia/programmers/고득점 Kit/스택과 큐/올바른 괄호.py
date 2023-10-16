def solution(s):
    stack = []

    for char in s:
        if not stack and char == ')':
            return False
        elif stack and char == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0
