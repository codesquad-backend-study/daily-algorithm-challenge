order = int(input())

n = 1                               # n 번째 대각선
max_idx = 1
while max_idx < order:               # 대각선에서 사용할 정보를 구한다.
    n += 1
    last_max_idx = max_idx
    max_idx += n

if n == 1:
    print("1/1")
else:
    cnt = order - last_max_idx - 1
    if n % 2 == 1:                                  # 홀수번째 대각선
        print(str(n-cnt) + "/" + str(1+cnt))
    else:                                           # 짝수번째 대각선
        print(str(1+cnt) + "/" + str(n-cnt))