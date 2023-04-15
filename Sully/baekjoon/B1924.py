X, Y = map(int, input().split())

day_num = 0
for x in range(1, X):
    # 28일
    if x == 2:
        day_num += 28
    # 30일
    elif x == 4 or x == 6 or x == 9 or x == 11:
        day_num += 30
    # 31일
    else:
        day_num += 31

# "일"로 다 변환
day_num += Y
# 나머지 1이면 월요일 시작
Z = day_num % 7

if Z == 1:
    print("MON")
elif Z == 2:
    print("TUE")
elif Z == 3:
    print("WED")
elif Z == 4:
    print("THU")
elif Z == 5:
    print("FRI")
elif Z == 6:
    print("SAT")
elif Z == 0:
    print("SUN")
