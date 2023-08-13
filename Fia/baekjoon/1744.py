# 수 묶기
import sys

# 음수와 음수를 곱해서 양수로 만들 수 있다
# 0이 존재한다면 마지막으로 남은 가장 큰 음수를 없앨 수 있다

count = int(sys.stdin.readline())

negative, positive = [], []
zero = False

for _ in range(count):
    number = int(sys.stdin.readline())
    if number > 0:
        positive.append(number)
    elif number == 0:
        zero = True
    else:
        negative.append(number)

positive.sort()
negative.sort(reverse=True)

positive_copy = [x for x in positive]
negative_copy = [x for x in negative]

result = 0

for i in range(len(positive) - 1, -1, -2):
    if i - 1 <= -1:
        break
    if positive[i] > 1 and positive[i - 1] > 1:
        result += positive_copy.pop() * positive_copy.pop()

while positive_copy:
    result += positive_copy.pop()

while len(negative_copy) > 1:
    result += negative_copy.pop() * negative_copy.pop()

if negative_copy and not zero:
    result += negative_copy.pop()

print(result)
