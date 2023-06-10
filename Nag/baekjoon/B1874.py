import sys

input = sys.stdin.readline

maxNumber = int(input())
stack = []
pointer = 1
answer = []
for _ in range(maxNumber):
    number = int(input())
    while pointer <= number:
        stack.append(pointer)
        answer.append('+')
        pointer += 1
    if stack[-1] == number:
        stack.pop()
        answer.append('-')
    else:
        answer = ['NO']
        break
print('\n'.join(answer))
