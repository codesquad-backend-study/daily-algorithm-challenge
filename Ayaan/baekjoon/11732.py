import sys

S = 0
for _ in range(int(sys.stdin.readline())):
    operation = sys.stdin.readline().rstrip()
    if operation == "all":
        S = (1 << 20) - 1
        continue
    elif operation == "empty":
        S = 0
        continue
        
    operation, num = operation.split()
    num = int(num) - 1
    
    if operation == "add":
        S |= (1 << num)
    elif operation == "remove":
        S &= ~(1 << num)
    elif operation == "toggle":
        S ^= (1 << num)
    else:
        if S & (1 << num) == 0:
            print(0)
        else:
            print(1)