# 기차가 어둠을 헤치고 은하수를

'''
기차는 20개의 일렬로 된 자석이 있고, 1개의 좌석에는 1명의 사람이 탈 수 있다.
명령의 종류는 4가지이다.
1 <= i <= N
1 <= x <= 20
1 i x : i번째 기차에 x번째 좌석에 사람을 태워라. 이미 사람이 있다면 아무런 행동을 하지 않는다.
2 i x : i번째 기차에 x번째 좌석에 앉은 사람은 하차한다. 자리에 아무도 없다면 아무런 행동을 하지 않는다.
3 i : i번째 기차에 앉아 있는 승객들이 모두 한 칸씩 뒤로 간다. 만약 20번째에 사람이 앉아 있었다면 그 사람은 하차한다.
4 i : i번째 기차에 앉아 있는 승객들이 모두 한칸씩 앞으로 간다. 만약 1번째에 사람이 앉아 있었다면 그 사람은 하차한다.
'''

train_count, command_count = map(int, input().split())

trains = [0 for _ in range(train_count)]

for _ in range(command_count):
    command = [*map(int, input().split())]
    command_type = command[0]
    train_number = command[1] - 1

    if command_type == 1:
        seat_number = command[2] - 1
        trains[train_number] |= 1 << seat_number
    elif command_type == 2:
        seat_number = command[2] - 1
        trains[train_number] &= ~(1 << seat_number)
    elif command_type == 3:
        trains[train_number] <<= 1
        binary = bin(trains[train_number])[2:]
        if len(binary) > 20:
            trains[train_number] = int(binary[-20:], 2)
    elif command_type == 4:
        trains[train_number] >>= 1

print(len(set(trains)))

# 이거 왤케 느림?
