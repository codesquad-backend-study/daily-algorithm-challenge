import sys

N, C = map(int, sys.stdin.readline().split())
positions = []
for _ in range(N):
    positions.append(int(sys.stdin.readline()))
positions.sort()

answer = 0
start = 1
end = positions[-1]

while start <= end:
    mid = start + (end - start) // 2
    count = 1
    prev = positions[0]

    for i in range(1, len(positions)):
        if positions[i] >= prev + mid:
            count += 1
            prev = positions[i]

    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
