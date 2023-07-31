import sys

class TrieNode:
    def __init__(self, keyname=None):
        self.keyname = keyname
        self.child = {}
        self.is_exist = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, nickname):
        node = self.root
        key = nickname[0]
        for char in nickname:
            if node.is_exist:
                key += char
                node.is_exist = False
            # 닉네임이 없는 경우 별칭은 첫번째 문자 그대로
            if char not in node.child:
                node.child[char] = TrieNode(key)
                node = node.child[char]
            # 닉네임이 있는 경우 별칭을 더 길게 만든다.
            else:
                node = node.child[char]
                node.is_exist = True
        # 닉네임의 개수
        node.count += 1

        if node.is_exist:
            if node.count == 1:
                print(nickname)
            else:
                print(nickname + str(node.count))
        else:
            print(node.keyname)

trie = Trie()
for _ in range(int(sys.stdin.readline())):
    nickname = sys.stdin.readline().rstrip()
    trie.insert(nickname)
