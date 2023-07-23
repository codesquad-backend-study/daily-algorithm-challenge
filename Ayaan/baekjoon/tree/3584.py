import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    parents = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parents[b] = a

    x, y = map(int, input().split())
    x_parents = [x]
    y_parents = [y]
    # x와 y의 부모 노드들을 루트까지 올라가면서 저장
    while parents[x]:
        x_parents.append(parents[x])
        x = parents[x]
    while parents[y]:
        y_parents.append(parents[y])
        y = parents[y]

    x_level = len(x_parents) - 1
    y_level = len(y_parents) - 1
    # 루트부터 내려오면서 부모가 달라지는 위치를 구한다.
    while x_parents[x_level] == y_parents[y_level]:
        x_level -= 1
        y_level -= 1
    # 부모가 달라지는 위치 + 1 이 가장 가까운 공통 조상
    print(x_parents[x_level + 1])
