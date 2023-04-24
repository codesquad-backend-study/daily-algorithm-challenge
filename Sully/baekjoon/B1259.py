# 맨앞에 무의미한 0이 안 오니 그냥 문자열로 처리하면 되는 문제
while True:
    n = input()
    if n == '0':
        break

    # 또 이거 바깥으로 빼줘서 시간 날림
    flag = True
    for i in range(len(n) // 2):
        lt, rt = n[i], n[len(n) - i - 1]
        if lt != rt:
            flag = False

    if flag:
        print('yes')
    else:
        print('no')