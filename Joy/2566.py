import sys

max_num = -1
max_idx = [-1,-1]

for i in range(1,10) :
    lst = list(map(int, sys.stdin.readline().split()))
    tmp = max(lst)
    if tmp > max_num :
        max_num = tmp
        max_idx = [i, lst.index(tmp)+1]

print(max_num)
print(max_idx[0], end=" ")
print(max_idx[1])