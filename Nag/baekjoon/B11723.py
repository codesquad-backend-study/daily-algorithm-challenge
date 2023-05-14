import sys

cnt = int(sys.stdin.readline())
things = {i: False for i in range(21)}
for _ in range(cnt):
    command = sys.stdin.readline().rstrip()
    if command == "empty":
        for key in things:
            things[key] = False
    elif command == "all":
        for key in things:
            things[key] = True
    else:
        order, element = command.split()
        element = int(element)
        if order == "check":
            print(1 if things[element] else 0)
        elif order == "add":
            things[element] = True
        elif order == "remove":
            things[element] = False
        else:
            if things[element]:
                things[element] = False
            else:
                things[element] = True
