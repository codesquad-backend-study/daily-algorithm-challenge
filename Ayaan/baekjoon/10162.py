T = int(input())
A, B, C = 0, 0, 0
if T // 300 > 0:
    A = T // 300
    T = T % 300
if T // 60 > 0:
    B = T // 60
    T = T % 60
if T // 10 > 0:
    C = T // 10
    T = T % 10
if T == 0:
    print(A, B, C, sep=" ")
else:
    print(-1)
