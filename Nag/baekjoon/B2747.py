n = int(input())
before = 1
answer = 1
if n < 3:
    print(1)
else:
    for cnt in range(n - 2):
        temp = answer
        answer += before
        before = temp
    print(answer)
