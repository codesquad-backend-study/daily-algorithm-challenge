# 나무 자르기

tree_count, target_length = map(int, input().split())
trees = [*map(int, input().split())]

start, end = 1, max(trees)

while start <= end:
    mid = start + (end - start) // 2
    total_slice = sum([tree - mid for tree in trees if tree >= mid])

    if total_slice < target_length:
        end = mid - 1
    else:
        start = mid + 1

print(end)

