node_cnt = int(input())
edge_cnt = int(input())
graph = [[] for _ in range(node_cnt + 1)]
visit = [False] * (node_cnt + 1)

for _ in range(edge_cnt):
    node1, node2 = map(int, input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

cnt = -1


def dfs(node):
    visit[node] = True
    global cnt
    cnt += 1

    for i in graph[node]:
        if not visit[i]:
            dfs(i)


dfs(1)
print(cnt)
