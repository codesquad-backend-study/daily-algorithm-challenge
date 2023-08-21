n, blueray_cnt = map(int, input().split())
videos = list(map(int, input().split()))

start = 1
end = sum(videos)
ans = 1

while start <= end:
    mid = (start + end) // 2

    current_record = 0
    current_blueray_cnt = 1
    for video in videos:
        if current_record + video <= mid:
            current_record += video
        elif current_record + video > mid >= video:
            current_record = video
            current_blueray_cnt += 1
        else:
            current_blueray_cnt += 200000

    if current_blueray_cnt <= blueray_cnt:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
