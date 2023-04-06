# K층의 n호에 살기 위해
# (K - 1)층의 N호까지의 사람들의 수의 합
# DP 문제니 점화식 생각해 보자

residents_num = 0

T = int(input())

# 이건 결국 입력에 대한 for문이니 시간복잡도로 안 쳐도 될 듯??
for i in range(T):
    # K층(0층부터), N호(1호부터)
    K, N = int(input()), int(input())

    # 0층에 대한 리스트 저장(0층의 i호에는 i명이 사니까 이렇게 저장해주는 거)
    residents_num = list(i for i in range(1, N + 1))

    for _ in range(1, K + 1):  # 1층부터 K층 (0층은 이미 했잖아)
        for n in range(1, N):  # 1호부터 N - 1호까지 (0호부터 N호까지라 생각하면 됨, 그니까 인덱스로 처리)
            residents_num[n] += residents_num[n - 1]  # 바로 전 호수를 현재 호수에 계속 저장

    # 마지막 호의 사람 수
    print(residents_num[-1])
