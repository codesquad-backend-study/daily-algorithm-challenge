n = int(input())

numbers = sorted([int(input()) for _ in range(n)])

negative = []
positive = []
zero_exist = False
odd_negative = False

idx = 0
while idx < n and numbers[idx] < 0:
    negative.append(numbers[idx])
    idx += 1

if idx > 0 and idx % 2 != 0:
    odd_negative = True

while idx < n and numbers[idx] == 0:
    idx += 1
    zero_exist = True

positive = numbers[idx:]

if zero_exist and odd_negative:
    negative.pop()

ans = 0

negative = negative[::-1]

while len(negative) >= 2:
    ans += negative.pop() * negative.pop()

if negative:
    ans += negative.pop()

if positive and positive[0] == 1:
    one_index = len(positive) - 1 - positive[::-1].index(1)
    ans += one_index + 1
    positive = positive[one_index + 1:]

while len(positive) >= 2:
    ans += positive.pop() * positive.pop()

if positive:
    ans += positive.pop()

print(ans)
