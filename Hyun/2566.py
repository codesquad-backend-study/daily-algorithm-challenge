arr = [list(map(int, input().split())) for _ in range(9)]

maximum = [-1, (0, 0)]
for y in range(9):
    for x in range(9):
        if maximum[0] < arr[y][x]:
            maximum[0] = arr[y][x]
            maximum[1] = (y+1, x+1)


print(maximum[0])
print(*maximum[1])

