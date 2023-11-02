import sys
from typing import List


def solution(N: int) -> List[str]:
    answer: List[str] = []
    star = ["***", "* *", "***"]
    cnt = 0

    while N > 3:
        N /= 3
        cnt += 1

    for _ in range(cnt):
        # 만들어진 현재의 별 모양을 기반으로 계속 다음 단계의 별 모양을 생성
        # 이때 당연히 3배가 늘어나게 됨
        star = make_star(star)

    return star


def make_star(star) -> List[str]:
    tmp_star = []

    # 별을 3배로 확장해서 새로운 패턴 생성
    for i in range(3 * len(star)):
        current_length = len(star)

        if i // current_length == 1:
            tmp_star.append(
                star[i % current_length] +
                # 공백을 삽입해서 패턴 확장
                " " * current_length +
                star[i % current_length]
            )
            continue

        tmp_star.append(star[i % current_length] * 3)

    return tmp_star


N = int(sys.stdin.readline().rstrip())
print(*solution(N), sep='\n')
