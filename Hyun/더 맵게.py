import heapq


def solution(scoville, K):
    heap = []
    for each in scoville:
        heapq.heappush(heap, each)

    count = 0

    while len(heap) >= 2:
        if heap[0] >= K:
            return count

        count += 1
        pop1 = heapq.heappop(heap)
        pop2 = heapq.heappop(heap)
        new_thing = pop1 + pop2 * 2

        heapq.heappush(heap, new_thing)

    if heap[0] >= K:
        return count

    return -1
