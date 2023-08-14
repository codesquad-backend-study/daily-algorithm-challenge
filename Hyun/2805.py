n, target = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    log = sum([max(0, i - mid) for i in trees])

    if log < target:
        end = mid - 1
    else:
        start = mid + 1

print(start - 1)
