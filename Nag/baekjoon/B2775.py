import math

cnt = int(input())
answer = []
for i in range(cnt):
    floor = int(input())
    floor = floor
    room = int(input())
    answer.append(math.comb(floor + room, room - 1))
for element in answer:
    print(element)
