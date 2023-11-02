while True:
    number = input()
    if number == '0':
        break
    if number[::-1] == number:
        print('yes')
    else:
        print('no')
# 솔직히 이렇게 할 수 있다. 근데 좀약간 날로 먹는거 같아서 스택활용해봤습니다.

while True:
    number = input()
    stack = []
    if number == '0':
        break
    if len(number) % 2 == 1:
        half = len(number) // 2
        number = number[:half] + number[half + 1:]
    for char in number:
        if not stack:
            stack.append(char)
            continue
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        print("no")
    else:
        print("yes")
