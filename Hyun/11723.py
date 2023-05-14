import sys

s = [False] * 21

n = int(input())
for _ in range(n):
    ins = sys.stdin.readline().split()

    if ins[0] == "all":
        s = [True] * 21

    elif ins[0] == "empty":
        s = [False] * 21

    elif ins[0] == "add":
        s[int(ins[1])] = True

    elif ins[0] == "remove":
        s[int(ins[1])] = False

    elif ins[0] == "check":
        sys.stdout.write("1\n" if s[int(ins[1])] else "0\n")

    elif ins[0] == "toggle":
        s[int(ins[1])] = not s[int(ins[1])]



