from typing import List


def solution(words: List) -> List:
    unique_words = list(set(words))
    return sorted(unique_words, key=lambda x: (len(x), x))


N = int(input())
words = []
for _ in range(N):
    words.append(input())

for word in solution(words):
    print(word)
