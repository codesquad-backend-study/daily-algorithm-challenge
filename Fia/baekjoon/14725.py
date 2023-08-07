# 개미굴
import sys


class Node:
    def __init__(self, key=None):
        self.key = key
        self.data = None
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: list) -> None:
        current = self.head

        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)

            current = current.children[char]

        current.data = word


N = int(sys.stdin.readline())
home = Trie()
for _ in range(N):
    word = sys.stdin.readline().strip().split()
    home.insert(word[1:])


# DFS
def dfs(node, depth):
    if node.key is not None:
        print('--' * depth + node.key)
    if node.children:
        for c in sorted(node.children.values(), key=lambda x: x.key):
            dfs(c, depth + 1)


dfs(home.head, -1)
