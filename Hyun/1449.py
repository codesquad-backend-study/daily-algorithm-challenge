n, tape_length = map(int, input().split())
leak_points = sorted(list(map(int, input().split())))

current_length = 0
tape_cnt = 1
current_point = leak_points.pop()
while leak_points:
    current_length += (current_point - leak_points[-1])
    if current_length >= tape_length:
        current_length = 0
        tape_cnt += 1
    current_point = leak_points.pop()

print(tape_cnt)
