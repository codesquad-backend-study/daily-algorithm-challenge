s = input()
n = int(input())

front = list(s)
back = []
for _ in range(n):
    ins = input().split()

    if ins[0] == 'L':
        if front:
            back.append(front.pop())

    elif ins[0] == 'D':
        if back:
            front.append(back.pop())
    elif ins[0] == 'B':
        if front:
            front.pop()
    elif ins[0] == 'P':
        front.append(ins[1])

print(''.join(front + back[::-1]))
