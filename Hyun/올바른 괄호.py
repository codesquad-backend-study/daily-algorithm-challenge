def solution(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(1)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    return True

