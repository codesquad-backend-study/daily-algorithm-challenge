import sys

lst = list(map(int,sys.stdin.readline().split()))
lst.remove(max(lst))
print(max(lst))