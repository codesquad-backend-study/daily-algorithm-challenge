A, B = map(int, input().split())
result = 1
while A < B:
    result += 1
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        break

if A == B:
    print(result)
else:
    print(-1)
