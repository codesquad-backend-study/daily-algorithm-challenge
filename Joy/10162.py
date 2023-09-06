import sys

t = int(sys.stdin.readline())

def cal(t) :
    if (t % 10) > 0 :
        return [-1]

    result = []
    button = [300, 60, 10]

    for i in range(3) :
        if t >= button[i] :
            result.append(t//button[i])
            t = t % button[i]
        else :
            result.append(0)

    return result

result = cal(t)

for i in result :
    print(i, end=" ")