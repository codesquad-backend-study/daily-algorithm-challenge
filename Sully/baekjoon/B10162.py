def solution(T):
    if T % 10 != 0:
        print(-1)
        return

    score = {'A': 300, 'B': 60, 'C': 10}
    A = T // score['A']
    B = (T % score['A']) // score['B']
    C = (T % score['A']) % score['B'] // score['C']

    # 쓰레기 코드
    # A, B, C = 0, 0, 0
    # tmp = 0
    # while tmp <= T:
    #     if score['A'] + tmp < T:
    #         tmp += score['A']
    #         A += 1
    #     elif score['B'] + tmp < T:
    #         tmp += score['B']
    #         B += 1
    #     elif score['C'] + tmp < T:
    #         tmp += score['C']
    #         C += 1
    #
    #     if tmp == T:
    #         print(A, B, C)
    #         break
    #     elif tmp > T:
    #         break

    print(A, B, C)


T = int(input())
solution(T)
