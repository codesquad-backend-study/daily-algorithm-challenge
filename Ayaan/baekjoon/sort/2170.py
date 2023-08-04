import sys

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().rstrip().split())))

points.sort()

max_len = 0
start = points[0][0]
end = points[0][1]
for point in points[1:]:
    if point[0] <= end:
        end = max(end, point[1])
    else:
        max_len += (end - start)
        start = point[0]
        end = point[1]
max_len += (end - start)
print(max_len)
