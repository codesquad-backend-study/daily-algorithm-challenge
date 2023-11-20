def solution(N, number):
    if N == number:
        return 1

    s = [set() for _ in range(8)]

    for idx, sub_set in enumerate(s, start=1):
        sub_set.add(int(str(N) * idx))

    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            return i + 1

    return -1
