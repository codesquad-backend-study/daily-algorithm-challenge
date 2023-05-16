max_num = -1
row = 0
column = 0

for i in range(1, 10):
    num_arr = input().split()
    for j in range(1, 10):
        num = int(num_arr[j-1])
        if num > max_num:
            max_num = num
            row = i
            column = j
print(max_num)
print(row, column)
