# 단지 번호 붙이기
def dfs(row, column):
    if row >= size or row < 0 or \
            column >= size or column < 0 or \
            graph[row][column] == '0':
        return

    graph[row][column] = '0'
    global count
    count += 1

    dfs(row, column + 1)
    dfs(row, column - 1)
    dfs(row + 1, column)
    dfs(row - 1, column)


size = int(input())
graph = [list(input()) for _ in range(size)]

apartment = []
global count

for row in range(size):
    for column in range(size):
        if graph[row][column] == '1':
            count = 0
            dfs(row, column)
            apartment.append(count)

apartment.sort()

print(len(apartment))
print(*apartment, sep='\n')
