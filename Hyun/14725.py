import collections


class Node:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(None, None)

    def insert(self, words):
        current = self.root

        depth = 0
        for word in words:
            if (word, depth) not in current.children:
                current.children[(word, depth)] = Node(word, depth)

            current = current.children[(word, depth)]
            depth += 1

    def print(self):

        def dfs(node):
            if not node.children:
                self.draw(node.val, node.depth)
                return

            self.draw(node.val, node.depth)

            for _, child in sorted(node.children.items()):
                dfs(child)

        for _, child in sorted(self.root.children.items()):
            dfs(child)

    def draw(self, val, depth):
        for _ in range(depth):
            print("--", end='')
        print(val)


trie = Trie()
n = int(input())
for _ in range(n):
    given = input().split()[1:]
    trie.insert(given)

trie.print()
