import collections


def solution(x: str) -> str:
    # (VPS 고려 X) 1.
    # stack = collections.deque()
    #
    # for cur in x:
    #     if stack and cur != stack[-1]:
    #         stack.pop()
    #         continue
    #
    #     if cur == '(':
    #         stack.append('(')
    #     else:
    #         stack.append(')')
    #
    # return 'NO' if stack else 'YES'

    # (VPS 고려 X) 2.
    # stack = collections.deque()
    # left = right = 0
    #
    # for cur in x:
    #     if cur == '(':
    #         left += 1
    #     else:
    #         right += 1
    #
    #     if left == right:
    #         if stack == stack.reverse():
    #             stack = collections.deque()
    #             left = right = 0
    #             continue

    # return 'YES' if left == right else 'NO'

    # 집중 좀 하자 !!
    # "()" 문자열이 기본 VPS야

    # 예외 처리
    if x[0] == ')':
        return 'NO'

    check = 0

    for cur in x:
        # 무조건 '('부터 시작하니까 괜춘
        if cur == '(':
            check += 1
        else:
            check -= 1

        # 음수가 되면 불필요한 괄호가 하나 더 있다는 소리임
        if check < 0:
            return 'NO'

    return 'YES' if check == 0 else 'NO'


T = int(input())
for _ in range(T):
    print(solution(input()))
