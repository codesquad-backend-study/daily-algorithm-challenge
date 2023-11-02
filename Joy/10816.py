import sys
import collections

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
m = int(input())
nums2 = list(map(int, sys.stdin.readline().split()))

cnt= collections.defaultdict(int)

for i in nums:
    cnt[i] += 1

for i in nums2:
    print(cnt[i], end=" ")

# counter = dict(collections.Counter(nums))
# for i in nums2:
#     print(counter[i], end=" ")