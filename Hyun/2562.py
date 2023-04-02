max_val = 0
idx = 0

for i in range(9):
    val = int(input())
    if max_val < val:
        idx = i + 1
        max_val = val

print(max_val)
print(idx)

