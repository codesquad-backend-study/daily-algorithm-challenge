import collections

N, K = map(int, input().split())
count = [0] * 100001
q = collections.deque([N])

# 갈 수 있는 경우의 수를 bfs로 탐색한다.
def bfs():
    while q:
        now = q.popleft()
        if now == K:
            print(count[now])
            return
        for x in (now - 1, now + 1, 2 * now):
            if 0 <= x < 100001 and count[x] == 0:
                count[x] = count[now] + 1
                q.append(x)

bfs()
