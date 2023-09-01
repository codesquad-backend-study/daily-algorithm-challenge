n, x = map(int, input().split())
views = list(map(int, input().split()))

sum_view = sum(views[:x])
max_view = [sum_view, 1]

start = 1
while start <= n - x:
    sum_view -= views[start - 1]
    sum_view += views[start + x - 1]
    if sum_view == max_view[0]:
        max_view[1] += 1
    elif sum_view > max_view[0]:
        max_view = [sum_view, 1]
    start += 1

if max_view[0] == 0:
    print("SAD")
else:
    print(*max_view, sep="\n")
