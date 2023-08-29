import collections
import sys


def solution(S: int, P: int, DNA: str, A: int, C: int, G: int, T: int) -> int:
    # 만들 수 있는 비밀번호의 종류의 수
    answer = 0
    # 알파벳 개수 계산을 위한 딕셔너리
    password = collections.defaultdict(int)

    for i in range(P):
        password[DNA[i]] += 1

    if password['A'] >= A and password['C'] >= C and password['G'] >= G and password['T'] >= T:
        answer += 1

    for i in range(P, S):
        password[DNA[i]] += 1
        password[DNA[i - P]] -= 1

        if password['A'] >= A and password['C'] >= C and password['G'] >= G and password['T'] >= T:
            answer += 1

    return answer


S, P = map(int, sys.stdin.readline().rstrip().split())
DNA = sys.stdin.readline().rstrip()
A, C, G, T = map(int, sys.stdin.readline().rstrip().split())

print(solution(S, P, DNA, A, C, G, T))
