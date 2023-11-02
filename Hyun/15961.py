import collections

entire_dish_cnt, entire_kind_cnt, succession_cnt, coupon_no = map(int, input().split())
conveyor = [int(input()) for _ in range(entire_dish_cnt)]

queue = collections.deque(conveyor[:succession_cnt])
dish_dict = collections.defaultdict(int)

for dish in conveyor[:succession_cnt]:
    dish_dict[dish] += 1
dish_dict[coupon_no] += 1

max_val = current_val = len(dish_dict)

for dish in conveyor[succession_cnt:] + conveyor[:succession_cnt - 1]:
    out = queue.popleft()
    dish_dict[out] -= 1
    if dish_dict[out] == 0:
        current_val -= 1

    queue.append(dish)
    if dish_dict[dish] == 0:
        current_val += 1
    dish_dict[dish] += 1

    max_val = max(max_val, current_val)

print(max_val)
