n, router_cnt = map(int, input().split())
routers = [int(input()) for _ in range(n)]
routers.sort()

start = 1
end = routers[-1] - routers[0]
ans = -1

while start <= end:
    mid = (start + end) // 2

    cur_cnt = 1
    cur_pos = routers[0]

    for router_pos in routers:
        if router_pos >= cur_pos + mid:
            cur_cnt += 1
            cur_pos = router_pos

    if cur_cnt >= router_cnt:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
