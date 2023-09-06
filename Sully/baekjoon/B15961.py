import collections
import sys
from typing import List


def solution(d: int, k: int, c: int, sushi: List[int]) -> int:
    answer = 0
    # lt와 rt의 간격을 k만큼
    lt, rt = 0, k

    sushi += sushi[:k]

    sushi_dict = collections.defaultdict(int)
    # 딕셔너리는 항상 c를 1개 포함하게끔
    sushi_dict[c] += 1

    for each in sushi[lt:rt]:
        sushi_dict[each] += 1

    while rt < len(sushi):
        # sushi_dict의 최대 길이로 answer 초기화
        answer = max(answer, len(sushi_dict))

        # 왼쪽 값은 빼주고
        sushi_dict[sushi[lt]] -= 1
        # 오른쪽 값은 더해주고
        sushi_dict[sushi[rt]] += 1

        # 빼준 왼쪽 값이 0이면 딕셔너리에서 제거
        if sushi_dict[sushi[lt]] == 0:
            del sushi_dict[sushi[lt]]

        lt += 1
        rt += 1

    return answer


N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
sushi: List[int] = []
for _ in range(N):
    sushi.append(int(sys.stdin.readline().rstrip()))

print(solution(d, k, c, sushi))
