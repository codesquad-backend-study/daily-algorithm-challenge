import collections


def bfs(graph, start, visited):
    q = collections.deque([start])
    visited[start] = True
    cnt = 1

    while q:
        v = q.popleft()
        for n in graph[v]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
                cnt += 1
    return cnt


def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        temp = wires[:]
        graph = collections.defaultdict(list)
        # i번째 연결을 뺀 graph를 만든다.
        for idx, node in enumerate(temp):
            if i == idx:
                continue
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        # 한쪽의 개수를 구해서 차이를 계산한다.
        cnt = bfs(graph, 1, [False] * (n + 1))
        other = n - cnt
        answer = min(answer, abs(cnt - other))

    return answer


solution(4, [[1, 2], [2, 3], [3, 4]])
