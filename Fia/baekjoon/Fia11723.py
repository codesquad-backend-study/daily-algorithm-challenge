# count = int(input())
# numbers = set()
#
# for _ in range(count):
#     operation = input()
#     o = operation.split()[0]
#     if o == "all":
#         numbers.update(list(range(1, 21)))
#         continue
#     if o == "empty":
#         numbers.clear()
#         continue
#     number = int(operation.split()[1])
#     if o == "add":
#         numbers.add(number)
#         continue
#     if o == "check":
#         print(1 if number in numbers else 0)
#         continue
#     if o == "remove" and number in numbers:
#         numbers.remove(number)
#         continue
#     if o == "toggle":
#         if number in numbers:
#             numbers.remove(number)
#             continue
#         else:
#             numbers.add(number)
#             continue

# 비트 마스크 : 각 자리의 비트를 이용해 boolean list처럼 사용하는 것
# 메모리 절약을 위해 사용
# [True, True, False, False, False] = 11000

import sys

count = int(sys.stdin.readline())
bit = 0

for _ in range(count):
    operation = sys.stdin.readline()
    o = operation.split()[0]
    if o == "all":
        bit = (1 << 20) - 1
        # 모든 비트를 1로 변경
        # (1 << 5) - 1 = 10000 - 00001 = 1111
        continue
    if o == "empty":
        bit = 0
        continue
    number = int(operation.split()[1]) - 1
    if o == "add":
        bit |= (1 << number)
        # | 연산을 사용하면 있어도 1 없어도 1이 된다
        # 0000 | (1 << 2) = 0100
        continue
    if o == "check":
        print(0 if bit & (1 << number) == 0 else 1)
        # 시프트 연산으로 이동 후 & 연산을 통해 0이 맞는지 확인
        continue
    if o == "remove":
        bit &= ~(1 << number)
        # 시프트 연산으로 해당 자리까지 이동한 후 ~ 연산자를 사용하여 비트를 반전시키고 & 연산
        # 0100 & ~(1 << 2) = 0110 & 1011 = 0010
        continue
    if o == "toggle":
        bit = bit ^ (1 << number)
        # 해당 비트의 값을 반전
        # xor 연산 : 0 ^ 1 = 1 / 1 ^ 1 = 0
        # 0100 ^ < (1 << 2) = 0000

# and 연산(&)
# 대응하는 두 비트가 모두 1일 때 1을 반환

# or 연산(|)
# 대응하는 두 비트 중 하나라도 1일 때 1을 반환

# xor 연산(^)
# 대응하는 두 비트가 서로 다르면 1을 반환

# not 연산(~)
# 비트의 값을 반전하여 반환

# shift 연산(>>, <<)
# 왼쪽 또는 오른쪽으로 비트 이동
