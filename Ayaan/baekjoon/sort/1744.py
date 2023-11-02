N = int(input())

plus_nums = []
minus_nums = []

answer = 0
for _ in range(N):
    num = int(input())
    if num > 1:
        plus_nums.append(num)
    elif num == 1:
        answer += 1
    else:
        minus_nums.append(num)

plus_nums.sort(reverse=True)
for i in range(0, len(plus_nums), 2):
    if i != len(plus_nums) - 1:
        answer += plus_nums[i] * plus_nums[i + 1]
    else:
        answer += plus_nums[i]

minus_nums.sort()
for i in range(0, len(minus_nums), 2):
    if i != len(minus_nums) - 1:
        answer += minus_nums[i] * minus_nums[i + 1]
    else:
        answer += minus_nums[i]

print(answer)
