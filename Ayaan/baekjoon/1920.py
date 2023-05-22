N = int(input())
nums = {num: 0 for num in input().split()}
M = int(input())
num_data = input().split()
for num in num_data:
    if num in nums:
        print(1)
    else:
        print(0)
