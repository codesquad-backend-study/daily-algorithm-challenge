import sys

n = int(input())
nums1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
nums2 = list(map(int, sys.stdin.readline().split()))

nums1 = {k:0 for k in nums1}

for i in nums2:
    if i in nums1:
        print(1, end=" ")
    else:
        print(0, end=" ")