t = int(input())
for _ in range(t):
    height, _, order = map(int, input().split())

    print(str(order % height if order % height != 0 else height) +                  # 나눠서 딱 떨어지는 경우엔 층을 그대로 반환
          "0" +
          str(order // height + 1 if order % height != 0 else order // height))     # 나눠서 딱 떨어지는 경우엔 1을 더하지 않는다.


# 실패하는데 반례가 무엇일까 ?
###########################################################

t = int(input())
for _ in range(t):
    height, _, order = map(int, input().split())

    hundred = order % height if order % height != 0 else height
    one = order // height + 1 if order % height != 0 else order // height

    print(hundred * 100 + one)
