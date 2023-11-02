import collections

N = int(input())
tree = collections.defaultdict(list)

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

answer = [0] * (N + 1)
answer[1] = -1
q = collections.deque([1])
while q:
    node = q.popleft()
    for child in tree[node]:
        # 한번 갔던 길은 가지 않도록 조건을 줘야 했다..
        if answer[child] == 0:
            answer[child] = node
            q.append(child)

for i in range(2, len(answer)):
    print(answer[i])
