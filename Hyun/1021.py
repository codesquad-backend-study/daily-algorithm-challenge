import collections

given_cnt, pick_cnt = map(int, input().split())
given = collections.deque([i for i in range(1, given_cnt + 1)])
picks = list(map(int, input().split()))
cnt = 0


for pick in picks:
    if given[0] == pick:
        given.popleft()

    else:
        pick_idx = given.index(pick)

        if pick_idx <= len(given)//2:
            while pick != given[0]:
                given.append(given.popleft())
                cnt += 1
        else:
            while pick != given[0]:
                given.appendleft(given.pop())
                cnt += 1

        given.popleft()

print(cnt)
