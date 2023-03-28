n = int(input())

for _ in range(n):
    a = input().split("X")

    score = 0
    for each in a:
        for i in range(1, len(each)+1):
            score += i

    print(score)

