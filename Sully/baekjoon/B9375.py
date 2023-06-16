import collections
import sys
from typing import List


def solution(clothes: List[str]) -> int:
    answer = 1
    count_map = collections.defaultdict(int)

    for cloth in clothes:
        # 같은 이름을 가진 의상은 존재하지 않으니 [0]은 사용할 필요가 없음
        count_map[cloth.split()[1]] += 1

    # for k in count_map:
    #     if count_map[k] > 1:
    #         answer += count_map[k]
    #         continue
    #
    # if len(count_map) != 1:
    #     answer += len(clothes)

    for k in count_map:
        # count_map[k] 종류를 안 입을 수 있으니 그 경우를 +1
        answer *= count_map[k] + 1

    # 아무것도 안 입는 알몸인 경우를 -1
    return answer - 1


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    array = []
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        array.append(sys.stdin.readline().rstrip())

    print(solution(array))
