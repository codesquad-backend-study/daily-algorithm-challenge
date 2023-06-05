height_list = []
for i in range(9):
    height_list.append(int(input()))
total = sum(height_list)
height_list.sort()

target = total - 100
# 뒤에서부터 2개를 더해서 target이 되는 값 2개를 뺴면 100이 된다.
for i in range(8, 0, -1):
    for j in range(i-1, -1, -1):
        if height_list[i] + height_list[j] == target:
            height_list.pop(i)
            height_list.pop(j)
            break
    if len(height_list) == 7:
        break
print(*height_list, sep="\n")
