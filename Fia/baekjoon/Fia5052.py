# 전화번호 목록
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    numbers = sorted([sys.stdin.readline().strip() for _ in range(n)])

    answer = "YES"


    def is_consistent(order, number):
        if numbers[order + 1][0:len(number)] == number:
            global answer
            answer = "NO"


    for i in range(len(numbers) - 1):
        is_consistent(i, numbers[i])

        if answer == "NO":
            break

    print(answer)
