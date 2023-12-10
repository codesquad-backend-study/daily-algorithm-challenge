def solution(n, computers):
    graph = [[] for _ in range(n)]

    for i, each in enumerate(computers):
        for idx, connect in enumerate(each):
            if i == idx:
                continue

            if connect == 1:
                graph[i].append(idx)

    visit = [False] * n

    def dfs(node):
        visit[node] = True

        for i in graph[node]:
            if not visit[i]:
                dfs(i)

    ans = 0

    for start in range(n):
        if not visit[start]:
            ans += 1
            dfs(start)

    return ans
