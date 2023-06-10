import collections
import sys

n = int(input())
givens = collections.deque([int(input()) for _ in range(n)])
stack = []
ans = []

i = 1
while givens:
    while i <= givens[0]:
        stack.append(i)
        ans.append("+")
        i += 1

    if stack[-1] != givens[0]:
        print("NO")
        sys.exit(0)

    givens.popleft()
    stack.pop()
    ans.append("-")

print('\n'.join(ans))
