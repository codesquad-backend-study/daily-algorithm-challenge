def solution(n, lost, reserve):
    reserves = {}

    for stu in reserve:
        reserves[stu] = 1

    borrow_cnt = 0
    for stu in sorted(lost):
        if stu - 1 in reserves and stu - 1 not in lost:
            borrow_cnt += 1
            del reserves[stu - 1]
        elif stu in reserves:
            borrow_cnt += 1
            del reserves[stu]
        elif stu + 1 in reserves and stu + 1 not in lost:
            borrow_cnt += 1
            del reserves[stu + 1]

    return n - len(lost) + borrow_cnt
