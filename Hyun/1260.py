import collections

node_cnt, edge_cnt, start_node = map(int, input().split())

graph = [[] for _ in range(node_cnt + 1)]

for _ in range(edge_cnt):
    node1, node2 = map(int, input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, node_cnt + 1):
    graph[i].sort()


def dfs(node):
    ans.append(node)
    visit[node] = True

    for i in graph[node]:
        if not visit[i]:
            dfs(i)


def bfs(node):
    queue = collections.deque([node])
    visit[node] = True

    while queue:
        cur = queue.popleft()
        ans.append(cur)

        for i in graph[cur]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)


ans = []
visit = [False] * (node_cnt + 1)
dfs(start_node)
print(*ans)

ans = []
visit = [False] * (node_cnt + 1)
bfs(start_node)
print(*ans)
