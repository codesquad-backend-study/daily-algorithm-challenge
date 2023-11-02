import sys
# 얘는 안되네요. 왜 안되지? 아시는 분있으면 알려주시면 감사하겠습니다.
maximum = 0
for _ in range(4):
    minus, plus = map(int, sys.stdin.readline().rstrip().split())
    temp = plus - minus
    # 얘가 문제인거 같은데 뭐가 문제일까...
    maximum = max(maximum, maximum + temp)
print(maximum)



import sys

passengers = []
total = 0
for _ in range(4):
    minus, plus = map(int, sys.stdin.readline().rstrip().split())
    total = total + plus - minus
    passengers.append(total)
print(max(passengers))
