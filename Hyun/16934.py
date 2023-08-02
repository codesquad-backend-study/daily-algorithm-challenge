import sys


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        current = self.root

        nickname = None

        for idx, ch in enumerate(word):
            if ch not in current.children:
                current.children[ch] = Node(ch)
                current.children[ch].data = (word[:idx + 1], 0)
                if not nickname:
                    nickname = word[:idx + 1]

            current = current.children[ch]

        if nickname:
            current.data = (word, 1)
        else:
            current.data = (current.data[0], current.data[1] + 1)
            nickname = current.data[0] + (str(current.data[1]) if current.data[1] > 1 else "")

        print(nickname)


n = int(input())
trie = Trie()

for _ in range(n):
    trie.insert(sys.stdin.readline().rstrip())
