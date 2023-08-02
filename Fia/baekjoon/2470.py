# 두 용액
import sys

N = int(sys.stdin.readline())

liquid = sorted(list(map(int, sys.stdin.readline().split())))

liquid1, liquid2 = None, None
value = 20000000000
head, tail = 0, N - 1

while head < tail:
    current_value = liquid[head] + liquid[tail]
    if abs(current_value) < value:
        value = abs(current_value)
        liquid1, liquid2 = liquid[head], liquid[tail]
    if current_value < 0:
        head += 1
    else:
        tail -= 1

print(liquid1, liquid2)
