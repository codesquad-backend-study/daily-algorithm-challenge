N, blu_ray_cnt = map(int, input().split())
lectures = list(map(int, input().split()))

answer = 0
start = 1
end = sum(lectures)
while start <= end:
    mid = (start + end) // 2
    if mid < max(lectures):
        start = mid + 1
        continue

    blu_ray = 0
    count = 1
    for lecture in lectures:
        if blu_ray + lecture <= mid:
            blu_ray += lecture
        else:
            count += 1
            blu_ray = lecture

    if count <= blu_ray_cnt:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)
