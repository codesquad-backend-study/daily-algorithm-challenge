for _ in range(3):
    yut = list(map(int, input().split()))
    count = 0
    for val in yut:
        if val == 0:
            count += 1
    if count == 0:
        print("E")
    else:
        print(chr(ord("A") + (count - 1)))
    