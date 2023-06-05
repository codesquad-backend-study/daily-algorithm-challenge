import sys

customInput = sys.stdin.readline

maximum = int(customInput().rstrip())
numbers = [i for i in range(1, maximum + 1)]
while len(numbers) > 1:
    if len(numbers) % 2 == 0:
        numbers = numbers[1::2]
    else:
        last = numbers[-1]
        numbers = numbers[1::2]
        numbers.insert(0, last)
print(numbers[0])
