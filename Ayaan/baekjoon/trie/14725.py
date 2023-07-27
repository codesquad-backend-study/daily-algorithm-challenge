import collections
import sys

class TrieNode:
    def __init__(self, end=None):
        self.end = end
        self.child = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, words):
        node = self.root
        for word in words:
            node = node.child[word]
        node.end = "*"

def print_trie(node, depth):
    if node.end == "*":
        return

    sorted_child = sorted(node.child)
    for child in sorted_child:
        print("--" * depth, end="")
        print(child)
        print_trie(node.child[child], depth + 1)

# 시작
words_list = []
for _ in range(int(sys.stdin.readline())):
    input_data = sys.stdin.readline().strip()
    # 입력값 앞에 숫자 잘라서 split
    words_list.append(input_data[2:].split())

trie = Trie()
# 트라이에 모두 insert
for words in words_list:
    trie.insert(words)

# 정렬해서 프린트
print_trie(trie.root, 0)
