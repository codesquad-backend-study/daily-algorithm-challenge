nums = []

for _ in range(int(input())):
    num = int(input())

    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))

