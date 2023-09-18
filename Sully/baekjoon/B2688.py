import sys


def solution(n: int) -> int:
    # 자릿수(0 ~ 9)의 개수 저장
    dp = [1] * 10

    for i in range(n - 1):
        # 0부터 9까지의 숫자에 대해서
        # 현재의 다음 자릿수부터 끝까지의 값의 합들을 현재 자릿수에 저장
        # 즉, 각 자릿수에 대한 숫자의 개수를 계산
        for j in range(10):
            dp[j] = sum(dp[j:])

    # 즉, 저장된 자릿수의 개수의 합을 출력하면 끝
    return sum(dp)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(solution(n))
