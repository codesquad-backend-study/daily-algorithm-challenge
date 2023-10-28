import heapq, collections


def solution(jobs):
    heap = []
    jobs.sort()
    jobs = jobs[::-1]
    length = len(jobs)
    total_time = 0
    current_time = 0

    while jobs or heap:
        if not heap:
            heapq.heappush(heap, jobs.pop()[::-1])

        duration, start_time = heapq.heappop(heap)
        current_time = max(start_time, current_time)
        current_time += duration
        total_time += current_time - start_time

        while jobs and jobs[-1][0] < current_time:
            heapq.heappush(heap, jobs.pop()[::-1])

    return total_time // length
