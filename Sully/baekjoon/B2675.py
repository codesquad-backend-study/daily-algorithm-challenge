answer = ''
T = int(input())

for _ in range(T):
    R, P = input().split()
    R = int(R)

    # R번 더해줘야 하니
    for p in P:
        answer += p * R

    print(answer)

    # 다음 출력을 위해 초기화
    answer = ''
