import collections
import sys
from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        # 기본 값으로 원래 0이 세팅되어 있는데 그 디폴트 value를 1로 바꾼 것
        self.name = collections.defaultdict(lambda: 1)

    def insert(self, nickname: str) -> None:
        current_node = self.root
        # 닉네임이 등장할 때마다 닉네임 횟수를 1씩 증가
        self.name[nickname] += 1

        for c in nickname:
            if c not in current_node:
                current_node[c] = {}

            current_node = current_node[c]

        # 여기서 늘 하던 것처럼 current_node[0]으로 flag를 달아줄 필요가 없음

    def search(self, nickname: str) -> str:
        current_node = self.root

        each_answer = ''
        for c in nickname:
            each_answer += c

            if c not in current_node:
                break

            # 닉네임을 트라이에서 검색하여 중복된 닉네임이라면 중복 횟수를 출력
            current_node = current_node[c]

        name_cnt = self.name[nickname]
        # 닉네임의 길이와 현재까지 탐색한 문자의 수가 같은 경우 -> 중복된 닉네임이 존재한다는 것
        # 그 중복 횟수를 출력하기 위해 each_answer에 저장
        if len(nickname) == len(each_answer) and name_cnt > 1:
            each_answer += str(name_cnt)

        return each_answer


def solution(nicknames: List[str]) -> List[str]:
    answer: List[str] = []
    t = Trie()

    for nickname in nicknames:
        answer.append(t.search(nickname))
        t.insert(nickname)

    return answer


N = int(sys.stdin.readline().rstrip())
nicknames = []
for _ in range(N):
    nicknames.append(sys.stdin.readline().rstrip())

print(*solution(nicknames), sep='\n')
