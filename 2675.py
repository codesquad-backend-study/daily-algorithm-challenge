import sys

n = int(sys.stdin.readline())

for i in range(n) :
    repeat, word = sys.stdin.readline().split()
    repeat = int(repeat)
    for s in word :
        print(s*repeat, end="")
    print()
    