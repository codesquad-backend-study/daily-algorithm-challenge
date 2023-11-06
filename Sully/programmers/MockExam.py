from typing import List


def solution(answers: List[int]) -> List[int]:
    answer: List[int] = []

    # 세 수포자들의 정답 패턴 정의
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 수포자들이 맞힌 정답의 수
    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            # 패턴이 나누어떨어지면 이 패턴에 맞는 수포자란 뜻이므로
            # 그 수포자에 맞는 index(j)의 score를 1 추가
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1

    max_score = max(scores)
    # 1을 더해줘야 0번째가 1번째 수포자가 됨
    return [i + 1 for i, score in enumerate(scores) if score == max_score]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
