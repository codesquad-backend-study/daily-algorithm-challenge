cnt = int(input())
answer = []
for i in range(cnt):
    height, width, order = map(int, input().split())
    order = order - 1
    room = order // height + 1
    floor = order % height + 1
    answer.append(floor * 100 + room)
for element in answer:
    print(element)
