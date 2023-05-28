import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums = {k:0 for k in nums}
m = int(input())
nums2 = list(map(int, sys.stdin.readline().split()))

for i in nums2:
    if i in nums:
        print(1)
    else:
        print(0)