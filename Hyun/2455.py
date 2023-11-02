max_val = 0
cur_val = 0

for _ in range(4):
    deboard, board = map(int, input().split())

    cur_val -= deboard
    cur_val += board

    max_val = max(max_val, cur_val)

print(max_val)
