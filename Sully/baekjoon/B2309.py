from typing import List


def solution(heights: List[int]) -> List[int]:
    sum_heights = sum(heights)
    for i in range(len(heights)):
        # set으로 하는 게 배열 중복 제거 중 가장 빠른 방법임
        for j in range(i + 1, len(heights)):
            if sum_heights - heights[i] - heights[j] == 100:
                answer = heights.copy()
                answer.remove(heights[i])
                answer.remove(heights[j])
                return sorted(answer)


array = []
for _ in range(9):
    array.append(int(input()))

print(*solution(array), sep='\n')
