N, r, c = map(int, input().split())


def check_order(r, c, width, start):
    mid = width // 2
    if r < mid:
        # 1사분면
        if c < mid:
            if mid == 1:
                print(start)
                return
            check_order(r, c, mid, start)
        # 2사분면
        elif c >= mid:
            if mid == 1:
                print(start + 1)
                return
            check_order(r, c - mid, mid, start + mid ** 2)
    elif r >= mid:
        # 3사분면
        if c < mid:
            if mid == 1:
                print(start + 2)
                return
            check_order(r - mid, c, mid, start + (mid ** 2) * 2)
        # 4사분면
        elif c >= mid:
            if mid == 1:
                print(start + 3)
                return
            check_order(r - mid, c - mid, mid, start + (mid ** 2) * 3)


check_order(r, c, 2 ** N, 0)
