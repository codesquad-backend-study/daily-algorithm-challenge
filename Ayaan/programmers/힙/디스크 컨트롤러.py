import heapq


def solution(jobs):
    start = -1
    current, total, i = 0, 0, 0
    hq = []
    # 작업 개수 만큼 반복
    while i < len(jobs):
        # 현재 시간에 처리할 수 있는 작업을 힙에 작업 시간이 짧은 순으로 추가
        for job in jobs:
            if start < job[0] <= current:
                heapq.heappush(hq, (job[1], job[0]))

        # 힙에서 작업 시간이 가장 짧은 작업을 꺼내서 작업
        if hq:
            work = heapq.heappop(hq)
            # 작업한 만큼 현재 시간 증가
            start = current
            current += work[0]
            total += current - work[1]
            i += 1
        else:
            current += 1

    print(total // len(jobs))
    return total // len(jobs)


solution([[0, 3], [1, 9], [2, 6]])
