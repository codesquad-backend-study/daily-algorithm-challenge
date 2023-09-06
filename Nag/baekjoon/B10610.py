import sys

customInput = sys.stdin.readline

marco = list(map(int, customInput().rstrip()))
marco.sort(reverse=True)
if marco[-1] == 0 and sum(marco) % 3 == 0:
    print(*marco, sep="")
else:
    print(-1)
