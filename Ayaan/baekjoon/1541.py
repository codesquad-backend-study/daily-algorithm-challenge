expression = input()

split_minus = expression.split("-")
result = 0
for num in split_minus[0].split("+"):
    result += int(num)

if len(split_minus) > 1:
    for i in range(1, len(split_minus)):
        for num in split_minus[i].split("+"):
            result -= int(num)

print(result)
