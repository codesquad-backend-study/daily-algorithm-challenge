def bin_search(target):
    start = 0
    end = len(b) - 1

    while start <= end:
        mid = (start + end) // 2

        if b[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start


t = int(input())
for _ in range(t):
    a_cnt, b_cnt = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    cnt = 0
    for each in a:
        cnt += bin_search(each)

    print(cnt)
