import sys

answer = []
givenNum = int(sys.stdin.readline().rstrip())
givenList = list(map(int, sys.stdin.readline().rstrip().split()))
given = {i: True for i in givenList}
questionNum = int(sys.stdin.readline().rstrip())
question = list(map(int, sys.stdin.readline().rstrip().split()))
for element in question:
    if element in given:
        answer.append(1)
    else:
        answer.append(0)
for num in answer:
    print(num)

# 이건 뒤지다가 발견한 방법 비슷한데 디테일에서 더 좋다.
# import sys
#
# input = sys.stdin.readline
#
# cnt = int(input())
# given = set(input().split())
# cnt = int(input())
# for num in list(input().split()):
#     if num in given:
#         print(1)
#     else:
#         print(0)
