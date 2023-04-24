K = int(input())

# 스택 구하기
stack = []
for i in range(K):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

# 합 구하기
answer = 0
for s in stack:
    answer += s

print(answer)