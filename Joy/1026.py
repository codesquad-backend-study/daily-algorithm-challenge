import sys

n = int(input())
lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = list(map(int, sys.stdin.readline().split()))

lst1.sort()
lst2 = sorted(lst2, reverse=True)

sum = 0
for i in range(n) :
    sum += (lst1[i] * lst2[i])

print(sum)