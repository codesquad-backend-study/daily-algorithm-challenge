import collections

N = int(input())
stack = collections.deque([num for num in range(N, 0, -1)])

while len(stack) > 1:
    stack.pop()
    if len(stack) == 1:
        break
    stack.appendleft(stack.pop())
print(stack.pop())
