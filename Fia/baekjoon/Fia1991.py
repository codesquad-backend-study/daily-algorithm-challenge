import collections

N = int(input())

graph = collections.defaultdict(list)

for i in range(N):
    node, left, right = input().split()
    graph[node].append(left)
    graph[node].append(right)

preorder_result = []
inorder_result = []
postorder_result = []


def preorder_traversal(root):
    preorder_result.append(root)

    left = graph[root][0]
    right = graph[root][1]

    if left != '.':
        preorder_traversal(left)
    if right != '.':
        preorder_traversal(right)


def inorder_traversal(root):
    left = graph[root][0]
    right = graph[root][1]

    if left != '.':
        inorder_traversal(left)

    inorder_result.append(root)

    if right != '.':
        inorder_traversal(right)


def postorder_traversal(root):
    left = graph[root][0]
    right = graph[root][1]

    if left != '.':
        postorder_traversal(left)

    if right != '.':
        postorder_traversal(right)

    postorder_result.append(root)


preorder_traversal('A')
inorder_traversal('A')
postorder_traversal('A')

print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))
