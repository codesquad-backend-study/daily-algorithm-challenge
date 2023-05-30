# 숫자 카드 2

import sys
from collections import Counter

sys.stdin.readline()
counter = Counter(sys.stdin.readline().split())

sys.stdin.readline()
M = sys.stdin.readline().split()

for number in M:
    if number in counter:
        print(counter[number], end=" ")
    else:
        print(0, end=" ")
