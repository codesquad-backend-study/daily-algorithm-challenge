class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    consistency = 'YES'

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            if curr_node.data:
                self.consistency = 'NO'

        curr_node.data = string


t = int(input())

for _ in range(t):
    trie = Trie()
    n = int(input())

    numbers = [input() for _ in range(n)]
    numbers.sort(key=len)

    for number in numbers:
        trie.insert(number)

    print(trie.consistency)
