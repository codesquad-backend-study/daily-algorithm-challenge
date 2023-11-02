# 딕셔너리 이용해서 값이 있는지 확인하기
N = int(input())
nums = {}
for num in input().split():
    nums[num] = 0
M = int(input())
result = []
for num in input().split():
    if num in nums:
        result.append(1)
    else:
        result.append(0)
print(*result)
