def push_button(time: int):
    A = 5 * 60
    B = 60
    C = 10

    count = [0] * 3
    if time >= A:
        count[0] = time // A
        time = time % A

    if time >= B:
        count[1] = time // B
        time = time % B

    if time >= C:
        count[2] = time // C
        time = time % C

    print(*count) if time == 0 else print(-1)


push_button(int(input()))
