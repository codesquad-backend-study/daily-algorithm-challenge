import sys

timer = [300, 60, 10]
answer = []
seconds = int(sys.stdin.readline().rstrip())
if seconds % 10 != 0:
    print(-1)
else:
    for button in timer:
        answer.append(seconds // button)
        seconds %= button
    print(*answer)
