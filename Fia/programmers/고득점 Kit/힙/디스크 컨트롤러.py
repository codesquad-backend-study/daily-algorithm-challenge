import heapq


def solution(jobs):
    length = len(jobs)
    jobs.sort(reverse=True)

    end_time = 0
    total = 0
    job_heap = []

    while jobs or job_heap:
        while jobs and jobs[-1][0] <= end_time:
            request, time = jobs.pop()
            heapq.heappush(job_heap, (time, request))

        if not job_heap:
            request, time = jobs.pop()
            end_time = request + time
            total += time
        else:
            time, request = heapq.heappop(job_heap)
            total += end_time - request + time
            end_time += time

    return total // length

# 테스트 1 〉	통과 (0.73ms, 10.3MB)
# 테스트 2 〉	통과 (0.43ms, 10.2MB)
# 테스트 3 〉	통과 (0.42ms, 10.3MB)
# 테스트 4 〉	통과 (0.39ms, 10.2MB)
# 테스트 5 〉	통과 (0.53ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.35ms, 10.3MB)
# 테스트 8 〉	통과 (0.29ms, 10.2MB)
# 테스트 9 〉	통과 (0.17ms, 10.3MB)
# 테스트 10 〉	통과 (0.75ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.4MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
