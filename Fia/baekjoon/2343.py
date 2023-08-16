# 기타 레슨

lecture_count, blue_count = map(int, input().split())
lectures = [*map(int, input().split())]

lowest = max(lectures)
highest = sum(lectures)

while lowest <= highest:
    mid = lowest + (highest - lowest) // 2

    count = 0
    size = 0
    for lecture in lectures:
        if size + lecture > mid:
            count += 1
            size = 0

        size += lecture

    if count + 1 <= blue_count:
        highest = mid - 1
    else:
        lowest = mid + 1

print(lowest)
