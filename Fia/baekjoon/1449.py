# 수리공 항승

leak_count, tape_length = map(int, input().split())
locations = sorted([*map(int, input().split())])

last = [locations[0]]
for location in locations[1:]:
    if location - last[-1] < tape_length:
        continue
    if location - last[-1] >= tape_length:
        last.append(location)

print(len(last))
