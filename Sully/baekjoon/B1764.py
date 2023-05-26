import collections
import sys
from typing import List


def solution(no_listen: List[str], no_look: List[str]) -> List[str]:
    answer = []
    cnt = 0
    no_listen_look = []

    no_listen_map = collections.defaultdict(int)
    for s in no_listen:
        no_listen_map[s] = 1

    for s in no_look:
        if s in no_listen_map:
            # 그냥 카운트 안 하고 len()로 넣어주는 게 더 빠르려나?
            cnt += 1
            no_listen_look.append(s)
            # 지워줘야 중복 처리 됨
            del no_listen_map[s]

    answer.append(str(cnt))
    answer += sorted(no_listen_look)  # 이거 정렬 안 해줘서 시간 날림
    return answer


N, M = map(int, sys.stdin.readline().rstrip().split())
no_listen = []
for _ in range(N):
    no_listen.append(sys.stdin.readline().rstrip())

no_look = []
for _ in range(M):
    no_look.append(sys.stdin.readline().rstrip())

print(*solution(no_listen, no_look), sep='\n')
