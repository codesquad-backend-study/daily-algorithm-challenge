# 홀: 1/1
# 짝: 1/2
# 홀: 2/1
# 짝: 3/1
# 홀: 2/2
# 짝: 1/3
# 홀: 1/4
# 짝: 2/3
# 홀: 3/2

# 분자: ja, 분모: mo
# 짝: ja: +1, mo: -1
# 홀: ja: -1, mo: +1

# 지그재그 가다가 더 이상 대각선에 분수가 없으면 "아래"로 이동 (아래를 잘 기억하고 있자)

X = int(input())

ja, mo = 0, 0
# X가 1부터 시작하니까 1로 초기화
cnt_line = 1

# 여기서 line의 개수를 세주는 거임 (시간 초과 땜에)
while cnt_line < X:
    # cnt_line이 이미 1이니 바로 빼주고
    X -= cnt_line
    # 1씩 증가시키자 (라인이 증가한다는 의미로)
    cnt_line += 1

# 라인이 홀수일 때
if cnt_line % 2 == 1:
    # 홀수 -> ja: -1, mo: +1

    # 분모에 X를 저장함
    mo = X
    ja = 1 + (cnt_line - X)
# 짝수일 때
elif cnt_line % 2 == 0:
    # 짝수 -> ja: +1, mo: -1

    # 분자에 X를 저장함
    ja = X
    mo = 1 + (cnt_line - X)

print(str(ja) + '/' + str(mo))
