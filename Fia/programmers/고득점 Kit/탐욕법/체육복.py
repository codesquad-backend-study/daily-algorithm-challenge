def solution(n, lost, reserve):
    count = n
    lost = set(lost)
    double = set(reserve)

    for l in lost:
        if l in reserve:
            continue

        if l - 1 not in lost:
            if l - 1 in double:
                double.remove(l - 1)
                continue

        if l + 1 not in lost:
            if l + 1 in double:
                double.remove(l + 1)
                continue

        count -= 1

    return count

