def do(given):
    ins = given[0]
    train_num = given[1] - 1

    if ins == 1:
        seat_num = given[2] - 1
        trains[train_num] |= (1 << seat_num)
    elif ins == 2:
        seat_num = given[2] - 1
        trains[train_num] &= ~(1 << seat_num)
    elif ins == 3:
        trains[train_num] <<= 1
        trains[train_num] &= 0b11111111111111111111
    elif ins == 4:
        trains[train_num] >>= 1


train_cnt, ins_cnt = map(int, input().split())
trains = [0] * train_cnt

for _ in range(ins_cnt):
    do(list(map(int, input().split())))

print(len(set(trains)))
