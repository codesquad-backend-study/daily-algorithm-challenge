N, K = map(int, input().split())


def dp(n, r):
    # (n + 1) * (r + 1)인 캐시 생성
    cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # 캐시 초기화
    # (r == 0 or n == r) -> 캐시가 1이 됨
    # 조합 문제 풀 때 5C0이랑 5C5랑 1로 똑같았잖아? 그거랑 같다고 생각하면 돼
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    # 실제 값 구하는 메인 로직
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            # i개의 아이템 중, j개의 아이템을 선택하는 경우의 수: 그보다 작은 두 값의 합
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]

    return cache[n][r]


print(dp(N, K))
