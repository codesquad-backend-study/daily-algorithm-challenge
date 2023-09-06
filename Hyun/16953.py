start, target = map(int, input().split())

cnt = 1
while target > start:
    if (target - 1) % 10 == 0:
        target -= 1
        target //= 10

    elif target % 2 == 0:
        target //= 2

    else:
        cnt = -1
        break

    cnt += 1

print(cnt if target == start else -1)
