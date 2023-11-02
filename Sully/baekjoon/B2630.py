import sys
from typing import List


def solution(N: int, papers_list: List[List[int]]) -> List[int]:
    answer: List[int] = []

    def quad_tree(papers_node, x, y, n):
        first_node = papers_node[y][x]

        for j in range(y, y + n):
            for i in range(x, x + n):
                if papers_node[j][i] == first_node:
                    continue

                mid = n // 2
                quad_tree(papers_node, x, y, mid)
                quad_tree(papers_node, x, y + mid, mid)
                quad_tree(papers_node, x + mid, y, mid)
                quad_tree(papers_node, x + mid, y + mid, mid)
                return

        if first_node == 0:
            answer.append(0)
            return

        answer.append(1)

    quad_tree(papers_list, 0, 0, N)

    # [하얀색 개수, 파란색 개수]
    return [answer.count(0), answer.count(1)]


N = int(sys.stdin.readline().rstrip())
papers_list: List[List[int]] = []
for _ in range(N):
    papers_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(*solution(N, papers_list), sep='\n')
