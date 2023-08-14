N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 1
end = max(heights)
while start <= end:
    cut = start + (end - start) // 2
    slice_len = 0
    for height in heights:
        if height > cut:
            slice_len += height - cut

    if slice_len < M:
        end = cut - 1
    elif M <= slice_len:
        start = cut + 1
print(end)
