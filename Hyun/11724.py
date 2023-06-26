node, edge = map(int, input().split())

graph = [[] for _ in range(node + 1)]
visit = [False] * (node + 1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visit[node] = True

    for i in graph[node]:
        if not visit[i]:
            dfs(i)


cnt = 0

for i in range(1, node + 1):
    if not visit[i]:
        cnt += 1
        dfs(i)

print(cnt)
