# 게임 닉네임
import sys


class Node:
    def __init__(self, key=None):
        self.key = key
        self.data = None
        self.nickname = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: list) -> None:
        current = self.head
        made = False

        origin_word = ''.join(word)
        for index, char in enumerate(word):
            if char not in current.children:
                current.children[char] = Node(char)
                substring = ''.join(word[:index + 1])
                if not made and current.children[char].nickname == 0:
                    current.children[char].nickname = 1
                    made = True
                    print(substring)
            current = current.children[char]
            if index == len(word) - 1 and not made:
                if not current.data:
                    current.nickname = 1
                    print(origin_word)
                elif current.nickname > 0:
                    current.nickname += 1
                    new_nickname = origin_word + str(current.nickname)
                    print(new_nickname)
                elif current.data and current.nickname == 0:
                    current.nickname = 2
                    print(origin_word + str(current.nickname))

        current.data = origin_word


N = int(sys.stdin.readline())
home = Trie()
for _ in range(N):
    word = list(sys.stdin.readline().strip())
    if len(word) >= 1:
        home.insert(word)


