def solution(l1, l2, l3):
    check(sum(l1))
    check(sum(l2))
    check(sum(l3))


def check(s):
    # s는 배가 몇 개인지
    if s == 3:
        print("A")
    elif s == 2:
        print("B")
    elif s == 1:
        print("C")
    elif s == 0:
        print("D")
    elif s == 4:
        print("E")


solution(list(map(int, input().split())),
         list(map(int, input().split())),
         list(map(int, input().split())))
