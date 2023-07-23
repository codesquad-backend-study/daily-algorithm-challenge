# 상근이의 여행

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())  # 국가의 수, 비행기의 종류

    for _ in range(M):
        sys.stdin.readline()

    print(N - 1)
