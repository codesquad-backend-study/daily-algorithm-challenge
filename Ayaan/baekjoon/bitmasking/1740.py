N = int(input())
idx = 0
answer = 0
while N != 0:
    if N % 2 == 1:
        answer += 3 ** idx
    N = N // 2
    idx += 1

print(answer)
