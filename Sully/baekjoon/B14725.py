import sys
from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.answer: List[str] = []

    def insert(self, food):
        current_node = self.root

        for each in food:
            if each not in current_node:
                current_node[each] = {}

            # 예전에 했던 딕셔너리 안에 딕셔너리 넣는 방식
            current_node = current_node[each]

        # 0으로 찾는 거임 그때처럼
        current_node[0] = True

    def appendlist(self, cnt, current_node):
        if 0 in current_node:
            return

        for each in current_node:
            self.answer.append('--' * cnt + each)
            self.appendlist(cnt + 1, current_node[each])


def solution(foods: List[List[str]]) -> List[str]:
    t = Trie()

    for food in sorted(foods):
        t.insert(food)

    t.appendlist(0, t.root)

    return t.answer


N = int(sys.stdin.readline().rstrip())

foods = []
for _ in range(N):
    foods.append(list(sys.stdin.readline().rstrip().split())[1:])

print(*solution(foods), sep='\n')
