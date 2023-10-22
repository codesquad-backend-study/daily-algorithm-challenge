def solution(progresses, speeds):
    answer = []

    cnt = 1
    prev_finish = 0
    if (100 - progresses[0]) % speeds[0] == 0:
        prev_finish = (100 - progresses[0]) // speeds[0]
    else:
        prev_finish = (100 - progresses[0]) // speeds[0] + 1

    for i in range(1, len(progresses)):
        finish = 0
        if (100 - progresses[i]) % speeds[i] == 0:
            finish = (100 - progresses[i]) // speeds[i]
        else:
            finish = (100 - progresses[i]) // speeds[i] + 1

        # 이전 작업 완료일보다 현재 작업 완료일이 오래 걸리면 이전까지의 왼료 작업을 배포한다.
        if prev_finish < finish:
            answer.append(cnt)
            cnt = 1
            prev_finish = finish
        # 오래 걸리지 않으면 완료 작업 개수를 추가한다.
        else:
            cnt += 1
    if cnt > 0:
        answer.append(cnt)

    return answer


solution([93, 30, 55], [1, 30, 5])
