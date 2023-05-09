import sys

n = int(input())
s = [False for i in range(21)]

for i in range(n) :
    tmp = sys.stdin.readline().split()
    operator = tmp[0]
    if len(tmp) == 2 :
        num = int(tmp[1])
    if operator == 'add' :
        s[num] = True
        continue
    elif operator == 'remove' :
        s[num] = False
        continue
    elif operator == 'toggle' :
        s[num] = not s[num]
        continue
    elif operator == 'all' :
        s = [True for i in range(21)]
        continue
    elif operator == 'empty' :
        s = [False for i in range(21)]
        continue
    else :
        print(int(s[num] == True))
