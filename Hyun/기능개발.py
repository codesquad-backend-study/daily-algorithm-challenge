def solution(progresses, speeds):
    schedule = []

    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        day = rest // speeds[i]
        if rest % speeds[i] > 0:
            day += 1

        schedule.append(day)

    ans = []
    schedule = schedule[::-1]

    deploy_cnt = 0
    while schedule:
        day = schedule.pop()
        deploy_cnt += 1

        while schedule and day >= schedule[-1]:
            schedule.pop()
            deploy_cnt += 1

        ans.append(deploy_cnt)
        deploy_cnt = 0

    return ans
