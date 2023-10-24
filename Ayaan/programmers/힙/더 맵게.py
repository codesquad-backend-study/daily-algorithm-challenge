import heapq


def solution(scoville, K):
    hq = []
    for scov in scoville:
        heapq.heappush(hq, scov)

    cnt = 0
    while hq[0] < K:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        heapq.heappush(hq, a + b * 2)
        cnt += 1
    return cnt


solution([1, 2, 3, 9, 10, 12], 7)
