def solution(N, number):
    dp = []

    for i in range(1, 9):
        i_times_case = set()
        # {N}, {NN}, {NNN} ...
        i_times_case.add(int(str(N) * i))

        # 3개 사용하는 경우(i == 3) {dp[0] (사칙연산) dp[3]}, {dp[1] (사칙연산) dp[2]}
        for j in range(0, i - 1):
            for op1 in dp[j]:
                for op2 in dp[-j - 1]:
                    i_times_case.add(op1 + op2)
                    i_times_case.add(op1 - op2)
                    i_times_case.add(op1 * op2)
                    if op2 != 0:
                        i_times_case.add(op1 // op2)

        if number in i_times_case:
            return i
        dp.append(i_times_case)

    return -1


solution(5, 31168)
