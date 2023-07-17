import collections

N = int(input())
tree = collections.defaultdict(list)
for _ in range(N):
    node_list = input().split()
    tree[node_list[0]].append(node_list[0])
    tree[node_list[0]].append(node_list[1])
    tree[node_list[0]].append(node_list[2])

def preorder(node):
    print(node[0], end="")
    if node[1] != '.':
        preorder(tree[node[1]])
    if node[2] != '.':
        preorder(tree[node[2]])
def inorder(node):
    if node[1] != '.':
        inorder(tree[node[1]])
    print(node[0], end="")
    if node[2] != '.':
        inorder(tree[node[2]])
def postorder(node):
    if node[1] != '.':
        postorder(tree[node[1]])
    if node[2] != '.':
        postorder(tree[node[2]])
    print(node[0], end="")


preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
