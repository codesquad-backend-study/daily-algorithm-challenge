import sys


def solution(s1, s2, s3, s4):
    # s[0]: 내린 사람 수, s[1]: 탄 사람 수
    max_people = -sys.maxsize - 1

    # 1번
    people = s1[1]

    # 2번
    people -= s2[0]
    people += s2[1]
    max_people = max(max_people, people)

    # 3번
    people -= s3[0]
    people += s3[1]
    max_people = max(max_people, people)

    # 4번 (의미 없는 연산)
    people -= s4[0]

    return max_people


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
s4 = list(map(int, input().split()))

print(solution(s1, s2, s3, s4))
