import sys


def solution(A: int, B: int) -> int:
    answer = 0

    while B > A:
        # B의 마지막 숫자가 1이면 그 1을 없애주기
        if B % 10 == 1:
            B //= 10
            answer += 1
            continue

        # B가 짝수면 2로 나눠줌
        if B % 2 == 0:
            B //= 2
            answer += 1
            continue

        # 위 두가지 경우가 아닌 경우는 더 봐줄 이유가 없으므로 반복문 탈출
        break

    # 반복문 후 A와 B가 같지 않다면 A를 B로 바꿀 수 없다는 의미
    if A != B:
        return -1

    # answer가 연산의 최솟값이니 이에 1을 더한 값을 출력
    return answer + 1


A, B = map(int, sys.stdin.readline().rstrip().split())
print(solution(A, B))
