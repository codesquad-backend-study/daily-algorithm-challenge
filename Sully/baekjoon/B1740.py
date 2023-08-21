import sys


def solution(N: int) -> int:
    answer = 0

    # bin()을 하면 0b가 붙어 나오니까
    N_binary = bin(N)[2:]
    tmp = len(N_binary) - 1

    for each in N_binary:
        # 이진수를 돌아주면서 1일 때 거듭제곱 해준 걸 더해주면 됨 그냥
        if int(each) == 1:
            answer += 3 ** tmp

        tmp -= 1

    return answer


N = int(sys.stdin.readline().rstrip())
print(solution(N))
