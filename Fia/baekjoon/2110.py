# 공유기 설치
import sys

house_count, share_count = map(int, input().split())
houses = sorted([int(sys.stdin.readline()) for _ in range(house_count)])
minimum = 1
maximum = houses[-1] - houses[0]

while minimum < maximum:
    mid = (minimum + maximum) // 2

    count = 1
    previous_install = houses[0]

    for house in houses[1:]:
        if house - previous_install >= mid:
            count += 1
            previous_install = house

    if count < share_count:
        maximum = mid
    else:
        minimum = mid + 1

print(minimum - 1)
