paper = [[False for j in range(100)] for i in range(100)]

count = int(input())

for i in range(count):
    points = list(map(int, input().split()))
    for column in range(points[0], points[0] + 10):
        for row in range(points[1], points[1] + 10):
            paper[column][row] = True

answer = sum(element for row in paper for element in row)

print(answer)
