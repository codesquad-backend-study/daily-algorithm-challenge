answer = 0
num = int(input())

# 첫트에 성공하니 기분이 묘하다..
for _ in range(num):
    H, W, N = map(int, input().split())

    # 걷는 거리가 같을 때는 아래층 방으로 예외처리 해주자
    tmp = 1
    cnt = 0
    for i in range(N):
        # 오른쪽으로 이동한다는 뜻
        # W가 필요 없네?
        if i % H == 0:
            cnt += 1
            tmp = cnt

        tmp += 100
        answer = tmp

    print(answer)
