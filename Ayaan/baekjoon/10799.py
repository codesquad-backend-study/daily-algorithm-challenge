input_data = input()
result = 0
height = 0
laser = False
for brace in input_data:
    if brace == '(':
        height += 1
        laser = True
    else:
        height -= 1
        if laser:
            result += height
            laser = False
        else:
            result += 1
print(result)
