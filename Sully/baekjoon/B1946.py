import sys
from typing import List


def solution(newcomers: List[List[int]]) -> int:
    # 서류 순위와 면접 순위 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
    # 15번째 줄 봐봐. 첫번째 서류가 어차피 제일 높으니까 당연히 합격
    answer = 1

    # [서류 순위, 면접 순위]의 2차원 배열
    # 일단 보기 편하게 서류순으로 정렬 (서류가 더 높으면 다른 면접은 볼 필요 X)
    newcomers.sort(key=lambda x: x[0])

    # highest: 면접 순위 비교 (가장 좋은 성적 저장)
    # 반복문 돌아줘야 되니 처음 요소로 저장 (서류가 젤 높다는 거 기억 -> 1부터 돌아준다)
    highest = newcomers[0][1]
    for i in range(len(newcomers)):
        cur = newcomers[i][1]
        if highest > cur:
            highest = cur
            answer += 1

    return answer


T = int(input())
for _ in range(T):
    N = int(input())
    array = []
    for _ in range(N):
        array.append(list(map(int, sys.stdin.readline().split())))

    print(solution(array))
