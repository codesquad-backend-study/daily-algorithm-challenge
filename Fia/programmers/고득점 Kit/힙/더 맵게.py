import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 1:
        lowest = heapq.heappop(scoville)

        if lowest >= K:
            return count

        heapq.heappush(scoville, lowest + heapq.heappop(scoville) * 2)
        count += 1

    return count if heapq.heappop(scoville) >= K else -1

# 결과
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.47ms, 10.2MB)
# 테스트 7 〉	통과 (0.41ms, 10.2MB)
# 테스트 8 〉	통과 (0.10ms, 10.2MB)
# 테스트 9 〉	통과 (0.09ms, 10.2MB)
# 테스트 10 〉	통과 (0.32ms, 10.3MB)
# 테스트 11 〉	통과 (0.20ms, 10.1MB)
# 테스트 12 〉	통과 (0.72ms, 10.3MB)
# 테스트 13 〉	통과 (0.37ms, 10.4MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.66ms, 10.3MB)
# 테스트 16 〉	통과 (0.00ms, 10.4MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.00ms, 10.4MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.00ms, 10.3MB)
# 테스트 22 〉	통과 (0.00ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (174.23ms, 16.3MB)
# 테스트 2 〉	통과 (403.21ms, 21.9MB)
# 테스트 3 〉	통과 (1769.11ms, 49.7MB)
# 테스트 4 〉	통과 (136.09ms, 14.9MB)
# 테스트 5 〉	통과 (1891.20ms, 51.8MB)

import collections


def solution(scoville, K):
    scoville.sort(reverse=True)
    mixed = collections.deque([])
    count = 0

    while scoville:
        lowest = scoville.pop() if not mixed or scoville and scoville[-1] <= mixed[0] else mixed.popleft()

        if lowest >= K:
            return count

        lower = scoville.pop() if not mixed or scoville and scoville[-1] <= mixed[0] else mixed.popleft()
        mixed.append(lowest + lower * 2)
        count += 1

    while len(mixed) > 1:
        lowest = mixed.popleft()

        if lowest >= K:
            return count

        lower = mixed.popleft()
        mixed.append(lowest + lower * 2)
        count += 1

    return count if mixed.popleft() >= K else -1

# 결과
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.25ms, 10.2MB)
# 테스트 7 〉	통과 (0.21ms, 10.3MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.18ms, 10.2MB)
# 테스트 11 〉	통과 (0.12ms, 10.4MB)
# 테스트 12 〉	통과 (0.38ms, 10.3MB)
# 테스트 13 〉	통과 (0.22ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.27ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.00ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.3MB)
# 테스트 22 〉	통과 (0.01ms, 10.3MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10.4MB)
# 테스트 26 〉	통과 (0.01ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (115.91ms, 16.1MB)
# 테스트 2 〉	통과 (157.47ms, 21.6MB)
# 테스트 3 〉	통과 (655.49ms, 49.7MB)
# 테스트 4 〉	통과 (58.80ms, 14.9MB)
# 테스트 5 〉	통과 (694.63ms, 51.8MB)
