# 잃어버린 괄호
import sys

# -를 맨 마지막에

expression = sys.stdin.readline().split("-")

answer = sum(map(int, expression[0].split("+")))

for e in expression[1:]:
    answer -= sum(map(int, e.split("+")))

print(answer)
