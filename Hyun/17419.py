# def calculate(bit, digit):
#     if bit == 0:
#         return 0
#
#     mask = 1
#     for i in range(digit - 1):
#         mask <<= 1
#         mask += 1
#
#     cnt = calculate(bit - (bit & ((bit ^ mask) + 1)), digit)
#
#     return cnt + 1
#
#
# digit = int(input())
#
# print(calculate(int(input(), 2), digit))


#### 51점짜리 풀이

input()
print(input().count('1'))

#### 100점 풀이

