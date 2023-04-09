import sys

# 40ms (삼항연사자를 if-else로 풀어쓰면 44ms)
n = int(sys.stdin.readline())

lst = []

for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    lst.append(tmp)

for tmp in lst :
    h = tmp[0]
    w = tmp[1]
    guest = tmp[2]
    yy = (guest % h) * 100 if (guest % h) != 0 else h * 100
    xx = (guest // h) +1 if (guest % h) != 0 else (guest // h)
    print(yy+xx)