from typing import List


def solution(citations: List[int]) -> int:
    N = len(citations)
    # h의 최댓값
    answer = 0

    citations.sort()

    for i, citation in enumerate(citations):
        #  저자의 H-지수는 그들의 N편의 논문 중 h편이 적어도 h번 인용되었고,
        #  나머지 (N − h)편의 논문이 h번을 초과하지 않게 인용되었을 때의 h 값을 가짐
        if citation >= N - i:
            answer = N - i
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
