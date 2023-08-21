# 예산
count = int(input())
requests = [*map(int, input().split())]
budget = int(input())

lowest = 1
highest = max(requests)

if sum(requests) <= budget:
    print(highest)
    exit()

while lowest < highest:
    mid = lowest + (highest - lowest) // 2

    total = budget
    for request in requests:
        if request - mid <= 0:
            total -= request
        else:
            total -= mid

    if total < 0:
        highest = mid
    else:
        lowest = mid + 1

print(lowest - 1)

