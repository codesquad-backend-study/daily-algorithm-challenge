import collections
import sys
from typing import List


def solution(books: List[str]) -> str:
    book_dict = collections.defaultdict(int)

    for book in books:
        book_dict[book] += 1

    dict_to_list = list(book_dict.items())
    return sorted(dict_to_list, key=lambda x: (-x[1], x[0]))[0][0]


books = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    books.append(sys.stdin.readline().rstrip())

print(solution(books))
