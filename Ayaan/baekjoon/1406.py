import sys
import collections

# 구글링 풀이
# 커서를 기준으로 왼쪽과 오른쪽으로 나눈다.
cursor_left = list(sys.stdin.readline().rstrip())
cursor_right = collections.deque()
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if cursor_left:
            cursor_right.appendleft(cursor_left.pop())
    elif command[0] == 'D':
        if cursor_right:
            cursor_left.append(cursor_right.popleft())
    elif command[0] == 'B':
        if cursor_left:
            cursor_left.pop()
    else:
        cursor_left.append(command[1])
print("".join(cursor_left + list(cursor_right)))
