# import collections
# import sys
#
#
# n = int(input())
#
# graph = collections.defaultdict(list)
# parent = collections.defaultdict(list)
#
# for i in range(1, n):
#     a, b = map(int, sys.stdin.readline().split())
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# visit = [False] * (n + 1)
# queue = collections.deque([(1, [])])
# visit[1] = True
#
# while queue:
#     node, sub_parent = queue.popleft()
#     parent[node] = sub_parent + [node]
#
#     for i in graph[node]:
#         if not visit[i]:
#             visit[i] = True
#             queue.append((i, sub_parent + [node]))
#
# for _ in range(int(input())):
#     n1, n2 = map(int, sys.stdin.readline().split())
#
#     for each in parent[n1][::-1]:
#         if each in parent[n2]:
#             print(each)
#             break

### ↑ ↑ 메모리 초과 풀이 ↑ ↑


# import collections
# import sys
#
# n = int(input())
#
# graph = collections.defaultdict(list)
# parent = collections.defaultdict(list)
#
# for i in range(1, n):
#     a, b = map(int, sys.stdin.readline().split())
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# visit = [False] * (n + 1)
# queue = collections.deque([(1, -1)])
# visit[1] = True
#
# while queue:
#     node, p = queue.popleft()
#     parent[node] = p
#
#     for i in graph[node]:
#         if not visit[i]:
#             visit[i] = True
#             queue.append((i, node))
#
# for _ in range(int(input())):
#     n1, n2 = map(int, sys.stdin.readline().split())
#
#     current_node = n1
#     n1_family = collections.defaultdict(int)
#     while current_node != -1:
#         n1_family[current_node] = 0
#         current_node = parent[current_node]
#
#     current_node = n2
#     while current_node != -1:
#         if current_node in n1_family:
#             sys.stdout.write(str(current_node) + "\n")
#             break
#         current_node = parent[current_node]


### ↑ ↑ 시간 초과 풀이 ↑ ↑

# import collections
# import sys
#
# n = int(input())
#
# graph = collections.defaultdict(list)
# parent = collections.defaultdict(int)
# depth = collections.defaultdict(int)
#
# for i in range(1, n):
#     a, b = map(int, sys.stdin.readline().split())
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# visit = [False] * (n + 1)
# queue = collections.deque([(1, 0)])
# visit[1] = True
#
# while queue:
#     node, d = queue.popleft()
#     depth[node] = d
#
#     for i in graph[node]:
#         if not visit[i]:
#             visit[i] = True
#             parent[i] = node
#             queue.append((i, d + 1))
#
#
# def find(n1, n2):
#     while depth[n1] != depth[n2]:
#         if depth[n1] > depth[n2]:
#             n1 = parent[n1]
#         else:
#             n2 = parent[n2]
#
#     while n1 != n2:
#         n1 = parent[n1]
#         n2 = parent[n2]
#
#     return n1
#
#
# for _ in range(int(input())):
#     n1, n2, = map(int, sys.stdin.readline().split())
#
#     print(find(n1, n2))

### ↑ ↑ 시간 초과 풀이, collections.defaultdict() 를 사용하면 시간초과발생 ↑ ↑

import collections
import sys

n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)
depth = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n + 1)
queue = collections.deque([(1, 0)])
visit[1] = True

while queue:
    node, d = queue.popleft()
    depth[node] = d

    for i in graph[node]:
        if not visit[i]:
            visit[i] = True
            parent[i] = node
            queue.append((i, d + 1))


def find(n1, n2):
    while depth[n1] != depth[n2]:
        if depth[n1] > depth[n2]:
            n1 = parent[n1]
        else:
            n2 = parent[n2]

    while n1 != n2:
        n1 = parent[n1]
        n2 = parent[n2]

    return n1


for _ in range(int(input())):
    n1, n2, = map(int, sys.stdin.readline().split())

    print(find(n1, n2))
