# 쇠막대기

string = input().replace('()', 'R')

stack = []
count = 0

for s in string:
    if s == '(':
        stack.append(s)
    elif s == 'R':
        count += len(stack)
    else:
        stack.pop()
        count += 1

print(count)

