def solution(sizes):
    small = []
    big = []

    for size in sizes:
        small.append(min(size))
        big.append(max(size))

    small.sort()
    big.sort()

    return small[-1] * big[-1]
