import sys

N = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
maxDp = tmp
minDp = tmp

# maxDp, minDp 하나의 리스트만 값을 변경하면서 DP값을 구한다. 이것이 슬라이딩 윈도우??
for _ in range(N - 1):
    nums = list(map(int, sys.stdin.readline().split()))
    maxDp = [nums[0] + max(maxDp[0], maxDp[1]),
             nums[1] + max(maxDp),
             nums[2] + max(maxDp[1], maxDp[2])]
    minDp = [nums[0] + min(minDp[0], minDp[1]),
             nums[1] + min(minDp),
             nums[2] + min(minDp[1], minDp[2])]
print(max(maxDp), min(minDp))
