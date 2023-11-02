def check(f):
    if f is True:
        return 1

    return 0


def solution(s):
    lt, rt = 0, len(s) - 1

    for i in range(len(s) // 2):
        if s[lt] != s[rt]:
            return check(False)

        lt += 1
        rt -= 1

    return check(True)


print(solution(input()))
