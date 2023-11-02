import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n) :
    num = int(sys.stdin.readline())
    if num == 0 :
        lst.pop()
    else :
        lst.append(num)
print(sum(lst))