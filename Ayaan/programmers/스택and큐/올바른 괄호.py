def solution(s):
    stack = []
    for p in s:
        if not stack and p == ')':
            return False
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()
        else:
            stack.append(p)

    return len(stack) == 0
