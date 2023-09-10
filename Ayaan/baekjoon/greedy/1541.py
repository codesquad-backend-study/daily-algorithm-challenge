data = input()

minus_split = data.split('-')
minus_result = []
for operation in minus_split:
    operation = [*map(int, operation.split('+'))]
    minus_result.append(sum(operation))
result = minus_result[0]
for minus in minus_result[1:]:
    result -= minus

print(result)
