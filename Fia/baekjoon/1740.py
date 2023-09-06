# 거듭제곱

n = int(input())

binary = bin(n)[2:][::-1]

power, answer = 1, 0

for bit in binary:
    answer += int(bit) * power
    power *= 3

print(answer)
