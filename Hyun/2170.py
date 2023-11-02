import sys

n = int(input())

lines = []

for _ in range(n):
    d1, d2 = map(int, sys.stdin.readline().rstrip().split())

    if d1 <= d2:
        lines.append((d1, d2))
    else:
        lines.append((d2, d1))

lines.sort(key=lambda x: (x[0], x[1]))

start = lines[0][0]
end = lines[0][1]

ans = 0
for line in lines[1:]:
    if line[0] <= end < line[1]:                  # 연결되고, 연장되는 경우
        end = line[1]
    elif start <= line[0] and line[1] <= end:      # 포함되는 경우
        continue
    else:                                        # 끊어진 경우
        ans += end - start
        start = line[0]
        end = line[1]
ans += end - start

print(ans)
