import sys

nodes = []

while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break


def post_traversal(start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start + 1, end + 1):
        if nodes[start] < nodes[i]:
            mid = i
            break

    post_traversal(start + 1, mid - 1)  # 왼쪽 먼저 탐색
    post_traversal(mid, end)  # 오른쪽 탐색
    print(nodes[start])  # 노드 출력


post_traversal(0, len(nodes) - 1)
