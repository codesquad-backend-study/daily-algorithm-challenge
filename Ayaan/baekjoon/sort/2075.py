import heapq

N = int(input())
nums_hq = []

for num in input().split():
    heapq.heappush(nums_hq, int(num))

for _ in range(N - 1):
    for num in input().split():
        heapq.heappush(nums_hq, int(num))
    # N개가 넘어가면 N개 빼서 N개 유지
    for _ in range(N):
        heapq.heappop(nums_hq)

print(heapq.heappop(nums_hq))
