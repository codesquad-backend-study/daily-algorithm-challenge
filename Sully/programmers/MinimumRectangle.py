from typing import List


def solution(sizes: List[List[int]]) -> int:
    widths, heights = [], []

    for size in sizes:
        width, height = size[0], size[1]

        # 양쪽의 경우를 모두 생각할 필요는 없음
        # 한쪽의 경우가 큰 것만 생각하면 됨
        if width < height:
            width, height = height, width

        widths.append(width)
        heights.append(height)

    return max(widths) * max(heights)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
