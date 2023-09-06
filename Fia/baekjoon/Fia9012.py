# 시간 제한 : 1초
# 입력 데이터의 수 T의 범위 : 알 수 없음
# 괄호 문자열의 길이 L : 2 <= L <= 50

def is_valid_ps():
    def parse_parenthesis(parenthesis: str):
        if parenthesis.startswith(')') or parenthesis.endswith('('):
            return "NO"

        stack = []
        for char in parenthesis:
            if char == '(':
                stack.append(char)
            elif char == ')' and len(stack) > 0 and stack[len(stack) - 1] == '(':
                stack.pop()
            else:
                return "NO"

        if len(stack) > 0:
            return "NO"

        return "YES"

    count = int(input())

    for _ in range(count):
        print(parse_parenthesis(input()))
