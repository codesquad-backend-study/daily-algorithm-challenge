# 에디터

import sys

sentence = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
stack = list(sentence)
temp = []

for _ in range(M):
    command = sys.stdin.readline().strip()
    if command == 'L' and stack:
        temp.append(stack.pop())
    elif command == 'D' and temp:
        stack.append(temp.pop())
    elif command == 'B' and stack:
        stack.pop()
    elif command.startswith('P'):
        stack.append(command[2])

while temp:
    stack.append(temp.pop())

print(''.join(stack))
