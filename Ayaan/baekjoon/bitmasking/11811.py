N = int(input())
for _ in range(N):
    row = list(map(int, input().split()))
    answer = 0
    # 행을 모두 or 연산 하면 답이 된다. why?
    for num in row:
        answer |= num
    print(answer)
