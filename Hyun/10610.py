numbers = sorted(input(), reverse=True)
number = int(''.join(numbers))

if number % 30 != 0:
    print(-1)
else:
    print(number)
