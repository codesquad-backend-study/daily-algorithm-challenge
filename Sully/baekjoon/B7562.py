import collections
import sys


def solution(I: int, current_x: int, current_y: int, future_x: int, future_y: int) -> int:
    graph = [[0] * I for _ in range(I)]

    dx = [-1, 1, -2, 2, -2, 2, -1, 1]
    dy = [-2, -2, -1, -1, 1, 1, 2, 2]

    dq = collections.deque()
    dq.append([current_x, current_y])

    while dq:
        current_x, current_y = dq.popleft()

        if current_x == future_x and current_y == future_y:
            return graph[current_x][current_y]

        for i in range(8):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                graph[nx][ny] = graph[current_x][current_y] + 1
                dq.append([nx, ny])

    return 0


def main():
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        I = int(sys.stdin.readline().rstrip())
        current_x, current_y = map(int, sys.stdin.readline().rstrip().split())
        future_x, future_y = map(int, sys.stdin.readline().rstrip().split())
        print(solution(I, current_x, current_y, future_x, future_y))


if __name__ == '__main__':
    main()
