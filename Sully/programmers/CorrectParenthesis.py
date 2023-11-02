def solution(s: str):
    if s[0] == ')':
        return False

    stack = []

    for c in s:
        if c == '(':
            stack.append('(')
            continue

        # 사실상 stack이 비어있으면 올바르지 않은 괄호라는 뜻이니
        if stack:
            stack.pop()

    if stack:
        return False

    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
