list = [int(input()) for i in range(9)]
temp = 0
index = 0
for i in range(0, 9):
    if temp <= list[i]:
        temp = list[i]
        index = i + 1
print(temp)
print(index)
