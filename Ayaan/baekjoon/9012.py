T = int(input())
for _ in range(T):
    stack = []
    str_data = input()
    for i in range(len(str_data)):
        if str_data[i] == ")":
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
        else:
            stack.append(str_data[i])
        if i == len(str_data) - 1:
            if len(stack) == 0:
                print("YES")
            else:
                print("NO")
