import re

formula = input()

numbers = formula.split('-', maxsplit=1)

plus = sum(map(int, numbers[0].split('+')))

minus = 0
if len(numbers) == 2:
    minus = sum(map(int, re.split(r'[-+]', numbers[1])))

print(plus - minus)
